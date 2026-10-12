# Contributing

Contributions that improve correctness, tests, documentation, or the public evidence model are welcome.

## Workflow

1. Open or reference an issue describing the problem and acceptance criteria.
2. Create a focused branch.
3. Keep the change small and avoid unrelated formatting rewrites.
4. Run the checks:

   ```bash
   python scripts/validate_profile.py
   python -m unittest discover -s reference/bounty-evidence-validator/tests -v
   ```

5. Open a pull request with actual test output, risks, and rollback guidance when relevant.

## Standards

- Do not add fabricated metrics, clients, payouts, coverage, or performance claims.
- Never commit credentials or private recipient information.
- Preserve the human-approval boundary for claims, submissions, payments, and maintainer contact.
- Add tests for every behavior change in the validator.
