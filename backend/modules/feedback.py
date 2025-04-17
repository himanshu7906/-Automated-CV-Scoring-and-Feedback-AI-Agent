FEEDBACK_TEMPLATE = """Dear {name},

Thank you for submitting your resume. Here is your feedback:

- CV Score: {total}/100
- JD Match: {jd_score}%
- Experience: {experience} years
- AI Keywords: {ai_count}
- Formatting Score: {formatting}%

Best,
HR Team
"""

def generate_feedback(scores, name):
    return FEEDBACK_TEMPLATE.format(
        name=name,
        total=scores['total'],
        jd_score=scores['jd_score'],
        experience=scores['experience'],
        ai_count=scores['ai_count'],
        formatting=scores['formatting']
    )
