from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal, InvalidOperation


@dataclass(frozen=True, slots=True)
class Evidence:
    issue_state: str
    unfinished_scope_confirmed: bool
    external_contributions_allowed: bool
    reward_amount: str | None
    reward_currency: str | None
    reward_quote: str | None
    competing_pull_requests: int = 0
    payment_status_only: bool = False


@dataclass(frozen=True, slots=True)
class Decision:
    eligible: bool
    reasons: tuple[str, ...]


def _valid_reward(amount: str | None, currency: str | None, quote: str | None) -> bool:
    if not amount or not currency or not quote or not quote.strip():
        return False
    try:
        return Decimal(amount) > 0
    except (InvalidOperation, ValueError):
        return False


def evaluate(evidence: Evidence) -> Decision:
    """Evaluate public evidence without guessing missing facts.

    The decision is deliberately fail-closed: every required proof must be
    present and positive before a task is eligible for human review.
    """

    reasons: list[str] = []
    if evidence.issue_state.lower() != "open":
        reasons.append("issue_not_open")
    if not evidence.unfinished_scope_confirmed:
        reasons.append("unfinished_scope_unverified")
    if not evidence.external_contributions_allowed:
        reasons.append("external_contributions_unverified")
    if not _valid_reward(
        evidence.reward_amount,
        evidence.reward_currency,
        evidence.reward_quote,
    ):
        reasons.append("reward_unverified")
    if evidence.competing_pull_requests > 0:
        reasons.append("competing_work_detected")
    if evidence.payment_status_only:
        reasons.append("payment_status_request")

    return Decision(eligible=not reasons, reasons=tuple(reasons))
