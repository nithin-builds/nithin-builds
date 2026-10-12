from __future__ import annotations

import sys
import unittest
from dataclasses import FrozenInstanceError
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT / "src"))

from bounty_evidence import Evidence, evaluate  # noqa: E402


def valid_evidence(**overrides: object) -> Evidence:
    values: dict[str, object] = {
        "issue_state": "open",
        "unfinished_scope_confirmed": True,
        "external_contributions_allowed": True,
        "reward_amount": "250",
        "reward_currency": "USD",
        "reward_quote": "$250 paid after accepted merge",
        "competing_pull_requests": 0,
        "payment_status_only": False,
    }
    values.update(overrides)
    return Evidence(**values)  # type: ignore[arg-type]


class EvidenceValidatorTests(unittest.TestCase):
    def test_complete_evidence_is_eligible_for_human_review(self) -> None:
        decision = evaluate(valid_evidence())
        self.assertTrue(decision.eligible)
        self.assertEqual(decision.reasons, ())

    def test_closed_issue_fails_closed(self) -> None:
        decision = evaluate(valid_evidence(issue_state="closed"))
        self.assertFalse(decision.eligible)
        self.assertIn("issue_not_open", decision.reasons)

    def test_missing_reward_quote_is_rejected(self) -> None:
        decision = evaluate(valid_evidence(reward_quote=None))
        self.assertIn("reward_unverified", decision.reasons)

    def test_invalid_or_nonpositive_reward_is_rejected(self) -> None:
        for amount in ("0", "-5", "not-a-number"):
            with self.subTest(amount=amount):
                self.assertIn(
                    "reward_unverified",
                    evaluate(valid_evidence(reward_amount=amount)).reasons,
                )

    def test_payment_request_is_not_available_work(self) -> None:
        decision = evaluate(valid_evidence(payment_status_only=True))
        self.assertIn("payment_status_request", decision.reasons)

    def test_competing_pull_request_is_rejected(self) -> None:
        decision = evaluate(valid_evidence(competing_pull_requests=1))
        self.assertIn("competing_work_detected", decision.reasons)

    def test_missing_scope_and_eligibility_return_both_reasons(self) -> None:
        decision = evaluate(
            valid_evidence(
                unfinished_scope_confirmed=False,
                external_contributions_allowed=False,
            )
        )
        self.assertEqual(
            decision.reasons,
            ("unfinished_scope_unverified", "external_contributions_unverified"),
        )

    def test_evidence_is_immutable(self) -> None:
        evidence = valid_evidence()
        with self.assertRaises(FrozenInstanceError):
            evidence.issue_state = "closed"  # type: ignore[misc]


if __name__ == "__main__":
    unittest.main()
