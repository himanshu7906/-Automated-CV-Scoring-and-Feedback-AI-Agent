from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from modules.extractor import extract_text, extract_contact_info
from modules.scoring import calculate_scores
from modules.feedback import generate_feedback
from modules.emailer import send_feedback
from modules.logger import log_processing
from langchain_agent import generate_ai_feedback

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

@app.post("/upload/")
async def upload_resume(resume: UploadFile = File(...), jd: UploadFile = File(...)):
    resume_path = f"/tmp/{resume.filename}"
    jd_path = f"/tmp/{jd.filename}"
    with open(resume_path, "wb") as f:
        f.write(await resume.read())
    with open(jd_path, "wb") as f:
        f.write(await jd.read())

    resume_text = extract_text(resume_path)
    jd_text = extract_text(jd_path)

    contact = extract_contact_info(resume_text, resume.filename)
    scores = calculate_scores(resume_text, jd_text)
    classic_feedback = generate_feedback(scores, contact['name'])
    ai_feedback = generate_ai_feedback(resume_text, jd_text)

    send_feedback(contact['email'], contact['name'], classic_feedback + "\n\nAI Analysis:\n" + ai_feedback)
    log_processing(contact, scores, "log.csv")

    return {"message": "Feedback sent", "scores": scores, "ai_feedback": ai_feedback}
