- Security & Auth
  - Validate and verify OAuth/OIDC JWTs at API gateway; enforce scopes for user/admin/agent.
  - Map directory identities to application roles and enforce RBAC for all endpoints.
  - Store secrets in a secrets manager; rotate keys and restrict access to service principals.
  - Use PrivateLink / VPC endpoints for sensitive services; deny public DB access.

- Agent safety & policies
  - Implement an agent policy layer: allowed actions, rate limits, and forbidden operations.
  - Sanitize and validate all agent inputs; redact PII before storage or model calls.
  - Limit agent privileges (least privilege) and separate human vs automated capabilities.
  - Require human approval/escalation path for destructive or high-risk actions.

- Data consistency & storage
  - Keep authoritative state in durable DB; use Redis only for caches or ephemeral leases.
  - Implement backups, multi-AZ replicas, and point-in-time restore for the DB.
  - Define retention/GC and redaction policies for conversational/context data.

- Concurrency & ticket handling
  - Add explicit ticket claim/lock (DB optimistic versioning or Redis lease) to prevent races.
  - Implement idempotency keys for agent-driven operations.
  - Use optimistic locking or transactional updates for multi-step ticket changes.

- Queueing & task reliability
  - Configure visibility timeout, DLQ, retries, and exponential backoff for queue consumers.
  - Make agent tasks idempotent and include retry-safe checkpoints.

- Streaming & long-running work
  - Choose a supported pattern for streaming (WebSockets, server-sent events, or streaming HTTP).
  - Provide progress notifications and timeouts for long-running agent workflows.

- Observability & audit
  - Add structured logging, request tracing (OpenTelemetry), and metrics for agent actions.
  - Keep immutable audit trails for ticket changes and agent decisions.
  - Monitor model usage, errors, and queue/backlog metrics.

- Testing & validation
  - Unit + integration tests for agent logic, authorization, and ticket workflows.
  - E2E tests that include concurrency/locking scenarios and failure injection.
  - Automated security scans and dependency checks.

- Deployment & operations
  - Use health checks, readiness/liveness endpoints, and canary/blue-green deployments.
  - Automate infra as code, CI/CD pipelines, and deployment rollback procedures.
  - Limit blast radius with service isolation and environment separation (dev/stage/prod).

- Cost & resource controls
  - Enforce per-agent and per-user quotas for model/API usage.
  - Monitor and alert on unexpected cost spikes (model calls, queue depth, DB IOPS).

- Compliance & privacy
  - Classify stored data, document retention policies, and support deletion/exports.
  - Ensure auditability of automated decisions for compliance needs.

If you want, produce a one-page prioritised implementation plan from this checklist.
