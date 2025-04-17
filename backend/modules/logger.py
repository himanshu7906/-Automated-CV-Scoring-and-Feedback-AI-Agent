import csv
import re
from datetime import datetime

def log_processing(contact, scores, log_file):
    name = contact["name"]
    masked_name = name[0] + "***" + name[-1] if len(name) > 2 else "***"
    masked_email = re.sub(r"(\\w)[^@]*(@.*)", r"\\1***\\2", contact["email"])
    with open(log_file, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.now().isoformat(),
            masked_name,
            masked_email,
            scores["total"],
            scores["jd_score"],
            scores["experience"],
            scores["ai_count"],
            scores["formatting"]
        ])
