<p align="center">
  <img width="100%" src="./assets/header.svg" alt="Nithin Kumar — Verification-first automation and reliability engineering" />
</p>

<p align="center">
  <code>Python</code> · <code>JavaScript</code> · <code>GitHub Actions</code> · <code>REST APIs</code> · <code>Git</code>
</p>

<p align="center">
  <a href="https://github.com/nithin-builds/nithin-builds/actions/workflows/profile-ci.yml"><img src="https://github.com/nithin-builds/nithin-builds/actions/workflows/profile-ci.yml/badge.svg" alt="Profile CI" /></a>
  <a href="https://github.com/nithin-builds/nithin-builds/actions/workflows/metrics.yml"><img src="https://github.com/nithin-builds/nithin-builds/actions/workflows/metrics.yml/badge.svg" alt="Profile Metrics" /></a>
</p>

<h2 align="center">I build verification-first automation that converts noisy external signals into testable decisions while keeping consequential actions under explicit human control.</h2>

<p align="center"><strong>Current focus:</strong> Python workflow reliability, GitHub Actions, secure API integration, evidence validation, and human-controlled AI automation.</p>

<p align="center">
  <a href="#verified-engineering-work">Verified work</a> ·
  <a href="#public-engineering-signals">Live signals</a> ·
  <a href="#engineering-standards">Standards</a> ·
  <a href="./PROJECT_BLUEPRINTS.md">System blueprints</a> ·
  <a href="../../issues/new?template=work-request.yml">Work with me</a>
</p>

---

## Verified Engineering Work

### 01 — Bounty Autopilot · Evidence and Reliability System

[![Status](https://img.shields.io/badge/runtime-owner--private-0F172A)](https://bounty-autopilot-hub.blondharp2.chatgpt.site)
[![Tests](https://img.shields.io/badge/safety_suite-5%2F5_passing-16A34A)](./CASE_STUDY.md#worker-verification)

| Dimension | Verified detail |
|---|---|
| **Problem** | Keyword-only discovery promotes solved work, payment-status threads, duplicate efforts, and unverifiable rewards. |
| **System** | Fail-closed discovery and evidence validation with authenticated worker heartbeats, source-quality gates, quota-limited review, and notification deduplication. |
| **Control boundary** | Discovery and review may be automated. Claims, comments, builds, pull requests, submissions, and payouts require explicit human approval. |
| **Evidence** | The private worker passes five safety tests and reports authenticated health signals to an owner-private dashboard. No earnings or coverage percentage is claimed. |

[Architecture and verified case study →](./CASE_STUDY.md)

### 02 — Bounty Evidence Validator · Public Reference Implementation

This repository now includes a small, dependency-free Python package that demonstrates the core fail-closed decision model publicly.

| Dimension | Implementation |
|---|---|
| **Input contract** | Typed evidence covering issue state, unfinished scope, contribution eligibility, reward evidence, competing work, and payment-status exclusions. |
| **Decision model** | A deterministic validator returns an immutable decision with machine-readable rejection reasons. Missing proof fails closed. |
| **Quality gate** | Standard-library unit tests cover eligible work, closed issues, ambiguous rewards, payment requests, existing competing PRs, invalid amounts, and immutability. |
| **Run locally** | `python -m unittest discover -s reference/bounty-evidence-validator/tests -v` |

[Read the implementation →](./reference/bounty-evidence-validator/README.md)

---

## Public Engineering Signals

The telemetry below is generated inside this repository. Volatile third-party statistics and activity-graph services are intentionally excluded.

<p align="center">
  <img width="100%" src="./github-metrics.svg" alt="Repository-owned public GitHub telemetry" />
</p>

<details>
<summary><strong>Telemetry contract</strong></summary>

- The workflow uses public GitHub data only.
- Plugin failures fail the workflow instead of being silently embedded in the SVG.
- The known-broken recent-activity plugin is disabled.
- The action is pinned to an immutable commit.
- CI rejects generated telemetry containing embedded error markers.
- Private clients, payouts, secrets, and coverage are never rendered.

</details>

---

## Engineering Standards

| Standard | Operating rule |
|---|---|
| **CI/CD** | Every change must pass documentation contracts and executable tests before it is considered healthy. |
| **Testing** | Acceptance criteria become deterministic tests; output is reported exactly as observed. |
| **Versioning** | Stable public contracts use Semantic Versioning; experiments are not presented as releases. |
| **Security** | Minimal workflow permissions, immutable action references, secret scanning, and fail-closed authentication. |
| **Observability** | Runtime claims require timestamps, structured evidence, and a reproducible health signal. |
| **Pull requests** | Small scope, linked rationale, actual test output, risk notes, and rollback guidance where applicable. |

Repository policies: [Security](./SECURITY.md) · [Contributing](./CONTRIBUTING.md) · [Changelog](./CHANGELOG.md) · [License](./LICENSE)

---

## Architecture Queue

These are specifications, not completed-product claims:

1. **BountyGrid** — multi-tenant serverless execution orchestrator with leases, idempotency, quota isolation, and fault injection.
2. **ReviewMesh** — local-first CRDT review workspace with deterministic convergence and offline recovery.
3. **EvidenceRAG** — revision-aware ingestion, hybrid retrieval, semantic caching, and citation lineage.

[Read the project blueprints and acceptance targets →](./PROJECT_BLUEPRINTS.md)

---

## Work With Me

I am available for clearly scoped work involving automation reliability, API integrations, evidence pipelines, GitHub Actions, Python, JavaScript, or technical system validation.

**[Open a structured work request →](../../issues/new?template=work-request.yml)**

Please include the repository, exact issue, acceptance criteria, deadline, and budget terms. A request starts a scope review; it is not an automatic delivery commitment.

<p align="center">
  <img width="100%" src="./assets/footer.svg" alt="End of Nithin Kumar's GitHub profile" />
</p>
