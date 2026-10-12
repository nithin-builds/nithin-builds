# Senior-Level Project Blueprints

These are build specifications, not claims of completed work. Each metric below is an acceptance target that must be measured before it appears as a result on the public profile.

## 1. BountyGrid — Multi-tenant serverless execution orchestrator

**Domain:** Infrastructure / DevOps

### Problem

External evidence collectors and review workers fail unpredictably: duplicate deliveries, expired jobs, provider rate limits, noisy retries, and cross-tenant leakage can make an automation platform unreliable and expensive.

### Solution

Build a control plane that schedules isolated jobs across serverless workers using durable leases, idempotency keys, bounded retries, tenant-aware quotas, and append-only execution events. Use a Postgres-backed state machine, an outbox for reliable event publication, OpenTelemetry traces, and policy gates that keep discovery separate from external actions.

### Architecture

- API gateway with signed tenant requests and request-level idempotency
- Scheduler that issues expiring leases instead of assuming exactly-once execution
- Worker pools with backpressure, retry budgets, and dead-letter handling
- Postgres control plane plus append-only audit events
- OpenTelemetry traces, structured logs, and SLO dashboards
- GitHub Actions deployment with migration, smoke-test, and rollback stages

### Metrics to publish after measurement

| Metric | Acceptance target |
|---|---:|
| Duplicate externally visible executions | 0 across a 100,000-job fault-injection run |
| Scheduler p95 dispatch latency | Under 250 ms at 1,000 queued jobs |
| Worker recovery after forced termination | Under 30 seconds |
| Tenant isolation tests | 100% passing |
| Availability objective | 99.9% over a measured 30-day window |

### Profile block after completion

> **Problem:** Multi-tenant automation workers produced duplicate jobs and weak recovery under provider failure.  
> **Solution:** Designed a lease-based serverless control plane with idempotency, quota isolation, durable retries, and traceable execution events.  
> **Measured results:** Replace this sentence only with benchmark output produced by the repository's load and chaos tests.

---

## 2. ReviewMesh — Local-first CRDT engineering review workspace

**Domain:** Advanced full-stack / distributed systems

### Problem

Distributed reviewers lose context when multiple people annotate requirements, evidence, and implementation risks concurrently. Traditional last-write-wins APIs overwrite edits and become unusable during intermittent connectivity.

### Solution

Build a local-first review workspace using a CRDT document model, WebSocket synchronization, optimistic local persistence, awareness cursors, and deterministic conflict resolution. Separate ephemeral presence from durable document state, compact historical updates, and expose replayable change events for auditability.

### Architecture

- React or Next.js client with a CRDT-backed local document
- WebSocket synchronization gateway with authenticated rooms
- Redis fan-out for horizontally scaled gateways
- Postgres snapshots plus compressed update log
- Offline mutation queue and deterministic reconnect merge
- Playwright multi-browser concurrency suite and property-based merge tests

### Metrics to publish after measurement

| Metric | Acceptance target |
|---|---:|
| Same-region synchronization p95 | Under 50 ms for 20 concurrent editors |
| Convergence failures | 0 across 1 million randomized operation sequences |
| Offline reconnect data loss | 0 in the published fault suite |
| Browser E2E concurrency scenarios | At least 30 passing scenarios |
| Compressed document replay | Under 500 ms for 100,000 operations |

### Profile block after completion

> **Problem:** Concurrent technical review lost edits and failed whenever collaborators moved offline.  
> **Solution:** Built a local-first CRDT workspace with deterministic merges, snapshot compaction, authenticated real-time rooms, and replayable audit events.  
> **Measured results:** Publish synchronization, convergence, and recovery numbers from reproducible benchmark artifacts.

---

## 3. EvidenceRAG — Streaming provenance-first AI ingestion pipeline

**Domain:** Data / AI engineering

### Problem

RAG systems often index stale or duplicated documents, lose citation lineage, waste embedding spend, and return answers that cannot be traced back to a specific source revision.

### Solution

Build an event-driven ingestion pipeline that fingerprints source revisions, performs content-defined chunking, deduplicates embeddings, applies semantic caching, and stores citation lineage alongside vectors. Retrieval should combine lexical and vector search, enforce freshness policies, and return source-level evidence for every answer.

### Architecture

- Change-data ingestion with source revision fingerprints
- Content-defined chunking and deterministic document IDs
- Queue-driven embedding workers with rate-aware batching
- Postgres metadata plus pgvector hybrid retrieval
- Semantic cache keyed by query intent and corpus revision
- Evaluation harness for retrieval quality, freshness, cost, and citation accuracy

### Metrics to publish after measurement

| Metric | Acceptance target |
|---|---:|
| Duplicate embedding reduction | At least 60% on the published evaluation corpus |
| Incremental update visibility p95 | Under 10 seconds |
| Citation lineage completeness | 100% for returned passages |
| Retrieval recall@10 | At least 0.90 on a labeled dataset |
| Cached-query cost reduction | At least 50% with no measured quality regression |

### Profile block after completion

> **Problem:** Conventional RAG ingestion created duplicate vectors, stale search results, and untraceable answers.  
> **Solution:** Implemented revision-aware streaming ingestion, deterministic chunking, hybrid retrieval, semantic caching, and end-to-end citation lineage.  
> **Measured results:** Add recall, freshness, deduplication, and cost figures only from the checked-in evaluation report.

## Publication rule

A target becomes a result only when the repository contains the benchmark command, raw output, environment details, and a repeatable CI job. Until then, the public profile must label it as a target.
