# keyword_check.py
# Simple script to check if required keywords exist in resume.txt

import sys
from pathlib import Path

RESUME_FILE = Path("resume.txt")

# You can change this list anytime
REQUIRED_KEYWORDS = [
    "Power Platform",
    "Power Apps",
    "Power Automate",
    "Power BI",
    "Dataverse",
    "Dynamics 365",
    "SharePoint",
    "Microsoft 365",
    "Azure DevOps",
    "GitHub"
]


def read_resume():
    if not RESUME_FILE.exists():
        print("❌ resume.txt not found.")
        sys.exit(1)
    return RESUME_FILE.read_text(encoding="utf-8")


def check_keywords(text: str):
    missing = [kw for kw in REQUIRED_KEYWORDS if kw.lower() not in text.lower()]
    if missing:
        print("❌ Missing important keywords:")
        for kw in missing:
            print(f" - {kw}")
        sys.exit(1)
    else:
        print("✅ All required keywords are present!")


if __name__ == "__main__":
    resume_text = read_resume()
    check_keywords(resume_text)
