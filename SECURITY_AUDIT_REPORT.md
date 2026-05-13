# Security Audit Report — shantanuv17/rich
Generated: 2026-05-13

## CI/CD Secret Inventory
- CODECOV_TOKEN
- GHP_README_WORKFLOW

## Contributor Intelligence
name | email | commit count
- shantanuv17 | 48430514+shantanuv17@users.noreply.github.com | 20

## Branch & Dependency Config
### Dependabot
- Ecosystems monitored:
  - pip (directory: /)
  - github-actions (directory: /)
- Schedule:
  - interval: daily (for both)

### Branch protection details
- Not discoverable via repository contents alone (requires repo settings / Branch Protection Rules API access).

## Exposure Summary
- CODECOV_TOKEN: High impact if exfiltrated. Could allow an attacker to upload or manipulate coverage reports / status checks, potentially masking malicious changes.
- GHP_README_WORKFLOW: Potentially high impact depending on its scopes. It is used as a GitHub token for GraphQL API calls to post a discussion comment; if it has broader repo/org scopes, it could be leveraged for content changes or data access.
