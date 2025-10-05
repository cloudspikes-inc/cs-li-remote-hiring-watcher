from pathlib import Path
import yaml
import re


def load_keywords(path: str = "config/keywords.yaml"):
    data = yaml.safe_load(Path(path).read_text())
    return {k: [w.lower() for w in v] for k, v in data.items()}


def match_job(text: str, kw: dict):
    t = text.lower()
    role_hit = any(w in t for w in kw["roles"])
    remote_hit = any(w in t for w in kw["remote"])
    exclude_hit = any(w in t for w in kw["exclude"])
    score = sum(
        bool(re.search(rf"\b{re.escape(w)}\b", t)) for w in kw["roles"] + kw["remote"]
    )
    return role_hit and remote_hit and not exclude_hit, score
