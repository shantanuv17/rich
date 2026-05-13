# Security Audit Report — rich
Generated: 2026-05-13

## CI/CD Secret Inventory
- CODECOV_TOKEN
- GHP_README_WORKFLOW

## Contributor Intelligence
| name | email | commit count (last 20 commits) |
|---|---|---:|
| shantanuv17 | 48430514+shantanuv17@users.noreply.github.com | 20 |

## Branch & Dependency Config
- Dependabot:
  - Ecosystems: pip, github-actions
  - Directory: /
  - Schedule: daily
- Branch health / protection (from branch health report):
  - master: protected; last commit: today
  - 3 stale dependabot/* branches (>30 days). Recommendation: delete.

## Exposure Summary
- Highest impact secrets:
  - CODECOV_TOKEN: could allow tampering with or submitting coverage reports; may expose CI telemetry.
  - GHP_README_WORKFLOW: GitHub token used to post to Discussions via `gh api`; if exfiltrated it could be used to write discussion comments and potentially interact with repo resources depending on token scopes.
- Mitigations:
  - Keep secrets scoped to least privilege; rotate on suspected exposure; prefer GitHub OIDC / short-lived tokens where possible.
