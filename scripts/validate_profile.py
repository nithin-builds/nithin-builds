from __future__ import annotations

import re
import os
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"

REQUIRED_FILES = (
    "README.md",
    "CASE_STUDY.md",
    "PROJECT_BLUEPRINTS.md",
    "SECURITY.md",
    "CONTRIBUTING.md",
    "CHANGELOG.md",
    "LICENSE",
    ".github/CODEOWNERS",
    ".github/ISSUE_TEMPLATE/work-request.yml",
    ".github/workflows/metrics.yml",
    ".github/workflows/profile-ci.yml",
    "reference/bounty-evidence-validator/README.md",
    "reference/bounty-evidence-validator/src/bounty_evidence/validator.py",
)

REQUIRED_SECTIONS = (
    "Nithin Kumar",
    "Verified Engineering Work",
    "Bounty Autopilot",
    "Bounty Evidence Validator",
    "Public Engineering Signals",
    "Engineering Standards",
)

FORBIDDEN_COPY = re.compile(r"\b(TODO|TBD|lorem ipsum)\b", re.IGNORECASE)
ERROR_MARKERS = re.compile(
    r"unexpected error|bad credentials|insufficient token scopes|rate limit",
    re.IGNORECASE,
)


def local_markdown_targets(text: str) -> list[str]:
    targets = re.findall(r"(?:src=|\]\()[\"']?(\./[^\"')# >]+)", text)
    return sorted(set(targets))


def main() -> None:
    partial_checkout = os.environ.get("PROFILE_VALIDATE_PARTIAL_CHECKOUT") == "1"
    missing = [name for name in REQUIRED_FILES if not (ROOT / name).is_file()]
    if missing and not partial_checkout:
        raise SystemExit(f"Missing required profile files: {missing}")

    readme = README.read_text(encoding="utf-8")
    absent = [section for section in REQUIRED_SECTIONS if section not in readme]
    if absent:
        raise SystemExit(f"README is missing required sections: {absent}")
    if FORBIDDEN_COPY.search(readme):
        raise SystemExit("README contains unfinished placeholder copy")
    if "n8n" in readme.lower():
        raise SystemExit("README claims n8n before a verified integration exists")
    if "github-readme-activity-graph" in readme:
        raise SystemExit("README uses the paused third-party activity graph")
    if "github-readme-stats" in readme:
        raise SystemExit("README uses volatile third-party statistics cards")

    broken = []
    for target in local_markdown_targets(readme):
        path = ROOT / target.removeprefix("./")
        if not path.exists() and not partial_checkout:
            broken.append(target)
    if broken:
        raise SystemExit(f"Broken local README targets: {broken}")

    metrics = ROOT / "github-metrics.svg"
    if metrics.is_file() and ERROR_MARKERS.search(metrics.read_text(encoding="utf-8")):
        raise SystemExit("github-metrics.svg contains an embedded provider error")

    print("Profile contract validated")


if __name__ == "__main__":
    main()
