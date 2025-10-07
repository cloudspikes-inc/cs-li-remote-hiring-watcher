"""Keyword filtering for jobs."""

import re
from pathlib import Path
from typing import Dict, List, Tuple

import yaml


def load_keywords(path: str = "config/keywords.yaml") -> Dict[str, List[str]]:
    """
    Load keywords from a YAML file and normalize them to lowercase.

    Args:
        path (str): Path to the YAML file containing role, remote, and
            exclude keywords.

    Returns:
        dict: Dictionary of keyword categories with lowercase word lists.
    """
    data = yaml.safe_load(Path(path).read_text(encoding="utf-8"))
    return {k: [w.lower() for w in v] for k, v in data.items()}


def match_job(text: str, kw: Dict[str, List[str]]) -> Tuple[bool, int]:
    """
    Match a job text against configured keywords.

    Args:
        text (str): The full job description or post text.
        kw (dict): Keyword dictionary with 'roles', 'remote', and
            'exclude' lists.

    Returns:
        tuple(bool, int): A tuple indicating whether the job matches and
            its keyword score.
    """
    t = text.lower()

    role_hit = any(w in t for w in kw.get("roles", []))
    remote_hit = any(w in t for w in kw.get("remote", []))
    exclude_hit = any(w in t for w in kw.get("exclude", []))

    score = sum(
        bool(re.search(rf"\b{re.escape(w)}\b", t))
        for w in (kw.get("roles", []) + kw.get("remote", []))
    )

    return role_hit and remote_hit and not exclude_hit, score
