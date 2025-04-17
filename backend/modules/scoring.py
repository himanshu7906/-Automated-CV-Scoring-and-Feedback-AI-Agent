import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

AI_KEYWORDS = {'machine learning', 'ai', 'deep learning', 'nlp', 'neural networks', 'computer vision'}

def calculate_scores(cv_text, jd_text):
    tfidf = TfidfVectorizer().fit_transform([cv_text, jd_text])
    jd_score = cosine_similarity(tfidf[0], tfidf[1])[0][0] * 100
    experience = sum(map(int, re.findall(r"(\\d+)\\+?\\s+(?:years?|yrs?)", cv_text)))
    ai_count = sum(1 for kw in AI_KEYWORDS if re.search(rf"\\b{kw}\\b", cv_text, re.I))
    formatting = sum(1 for section in ["education", "experience", "skills"] if section in cv_text.lower())
    total = jd_score * 0.4 + min(experience, 10) * 2 + ai_count * 5 + formatting * 10
    return {
        "jd_score": round(jd_score, 1),
        "experience": experience,
        "ai_count": ai_count,
        "formatting": formatting * 10,
        "total": round(total, 1)
    }
