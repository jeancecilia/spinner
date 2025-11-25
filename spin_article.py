import random
import re
from pathlib import Path

ARTICLE_PATH = Path("article")
OUTPUT_PATH = Path("article_versions.txt")

# A small synonym map for lightweight spinning. More entries can be added as needed.
SYNONYMS = {
    "company": ["firm", "business", "enterprise", "organization"],
    "companies": ["firms", "businesses", "enterprises", "organizations"],
    "investors": ["backers", "shareholders", "stakeholders", "financiers"],
    "thai": ["Thai", "Thailand-based", "Thailand"],
    "business": ["venture", "operation", "commercial endeavor", "enterprise"],
    "legal": ["statutory", "lawful", "regulatory", "compliance"],
    "process": ["procedure", "workflow", "step-by-step approach", "method"],
    "requirements": ["obligations", "criteria", "conditions", "needs"],
    "registration": ["enrollment", "sign-up", "recording", "filing"],
    "shareholders": ["partners", "owners", "members", "stakeholders"],
    "directors": ["board members", "managers", "leaders", "executives"],
    "foreign": ["international", "overseas", "non-domestic", "external"],
    "local": ["domestic", "local market", "in-country", "within Thailand"],
    "income": ["revenue", "earnings", "takings", "turnover"],
    "tax": ["taxation", "levy", "fiscal", "tax-related"],
    "documents": ["paperwork", "records", "filings", "forms"],
    "steps": ["stages", "phases", "milestones", "checkpoints"],
    "guide": ["handbook", "manual", "overview", "roadmap"],
    "limited": ["limited", "liability-limited", "restricted liability", "Ltd."],
}

WORD_PATTERN = re.compile(r"\b\w+\b")


def spin_word(word: str, rng: random.Random) -> str:
    base = word.lower()
    if base not in SYNONYMS:
        return word

    replacement = rng.choice(SYNONYMS[base])
    if word.isupper():
        return replacement.upper()
    if word.istitle():
        return replacement.capitalize()
    return replacement


def spin_text(text: str, seed: int) -> str:
    rng = random.Random(seed)

    def replace(match: re.Match[str]) -> str:
        return spin_word(match.group(0), rng)

    return WORD_PATTERN.sub(replace, text)


def main() -> None:
    original = ARTICLE_PATH.read_text(encoding="utf-8")
    versions = []
    for seed in range(1, 11):
        spun = spin_text(original, seed)
        versions.append(f"--- Version {seed} ---\n{spun}\n")

    OUTPUT_PATH.write_text("\n".join(versions), encoding="utf-8")


if __name__ == "__main__":
    main()
