import sys
from pathlib import Path

RESUME_FILE = Path("resume.txt")
KEYWORDS_FILE = Path("keywords.txt")


def load_keywords():
    if not KEYWORDS_FILE.exists():
        print("❌ keywords.txt not found.")
        sys.exit(1)
    lines = KEYWORDS_FILE.read_text(encoding="utf-8").splitlines()
    return [l.strip() for l in lines if l.strip()]


def read_resume():
    if not RESUME_FILE.exists():
        print("❌ resume.txt not found.")
        sys.exit(1)
    return RESUME_FILE.read_text(encoding="utf-8")


def check_keywords(text: str, required_keywords):
    missing = [kw for kw in required_keywords if kw.lower() not in text.lower()]
    if missing:
        print("❌ Missing important keywords:")
        for kw in missing:
            print(f" - {kw}")
        sys.exit(1)
    else:
        print("✅ All required keywords are present!")


if __name__ == "__main__":
    resume_text = read_resume()
    required = load_keywords()
    check_keywords(resume_text, required)
