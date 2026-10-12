# Bounty Evidence Validator

A dependency-free reference implementation of a fail-closed eligibility gate for public software bounties.

## Why it exists

An issue being open does not prove that it is unfinished, funded, available to external contributors, or free of competing work. This package converts those facts into an explicit input contract and refuses eligibility when proof is missing.

## Decision boundary

The validator may mark evidence as eligible for **human review**. It does not claim, comment on, build, submit, or accept payment for a bounty.

## Run the tests

From the repository root:

```bash
python -m unittest discover -s reference/bounty-evidence-validator/tests -v
```

The test suite uses only Python's standard library.

## Example

```python
from bounty_evidence import Evidence, evaluate

decision = evaluate(
    Evidence(
        issue_state="open",
        unfinished_scope_confirmed=True,
        external_contributions_allowed=True,
        reward_amount="250",
        reward_currency="USD",
        reward_quote="$250 paid after accepted merge",
    )
)

assert decision.eligible
```

## Guarantees

- Deterministic output for identical evidence
- Immutable evidence and decisions
- Machine-readable rejection reasons
- Invalid, missing, or nonpositive rewards rejected
- Payment-status requests rejected
- Competing pull requests rejected
- No network, secret, model, or third-party dependency
