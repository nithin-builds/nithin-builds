# Security Policy

## Supported surface

The public profile automation and the bounty evidence validator on the default branch are maintained. Architecture blueprints are design documents and are not supported software releases.

## Reporting a vulnerability

Do not open a public issue containing secrets, private data, exploit details, or credentials. Use GitHub's private vulnerability reporting feature when it is available for this repository. Otherwise, open a minimal issue requesting a private security channel without including sensitive details.

Please include:

- Affected file or workflow
- Reproduction conditions
- Security impact
- Suggested mitigation, if known

## Security principles

- No secrets in source, logs, badges, generated telemetry, or examples
- Minimal GitHub Actions permissions
- Third-party Actions pinned to immutable commit SHAs
- Consequential bounty actions require explicit human approval
- Missing evidence and failed authentication fail closed
