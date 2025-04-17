#from langchain.chat_models import ChatOpenAI
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.3)

prompt_template = ChatPromptTemplate.from_template("""
You are an expert HR reviewer. Given a candidate's resume and a job description, evaluate the candidate and generate feedback.

Resume:
{resume}

Job Description:
{jd}

Respond with:
- A professional summary of the candidate's fit
- Strengths
- Areas for improvement
""")

def generate_ai_feedback(resume, jd):
    prompt = prompt_template.format_messages(resume=resume[:2000], jd=jd[:2000])
    return llm(prompt).content
