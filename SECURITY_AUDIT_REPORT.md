# Security Audit Report — shantanuv17/rich
Generated: 2026-05-12

## CI/CD Secret Inventory
- `CODECOV_TOKEN` (referenced in `.github/workflows/pythonpackage.yml`)
- `GHP_README_WORKFLOW` (referenced in `.github/workflows/readmechanged.yml`)

## Contributor Intelligence
| name | email | commit count (last 20 commits) |
|---|---|---:|
| shantanuv17 | 48430514+shantanuv17@users.noreply.github.com | 10 |
| Shantanu Verma | shantanu.verma@orange.com | 6 |
| Will McGugan | willmcgugan@gmail.com | 3 |
| GitHub | noreply@github.com | 1 |

## Branch & Dependency Config
### Dependabot
From `.github/dependabot.yml`:
- Ecosystems monitored:
  - `pip` (directory `/`)
  - `github-actions` (directory `/`)
- Schedule: `daily` for both ecosystems

### Branch protection
Branch protection rules were not inspected via the available tooling in this run. If required, confirm in the repository settings for `master` (required status checks, required reviews, admin enforcement, and restrictions).

## Exposure Summary
- **Highest impact**: `CODECOV_TOKEN` — could allow an attacker to upload/alter coverage reports, potentially masking failing tests/coverage regressions in reports or corrupting project analytics.
- **High impact**: `GHP_README_WORKFLOW` — used as a GitHub token for GraphQL API calls to post discussion comments; if it has elevated scopes, it could be abused to post or modify content (and, depending on scopes, access additional repo/org resources).

General notes:
- Secrets are referenced only in GitHub Actions workflows; ensure they are scoped to least privilege, rotated periodically, and protected from exposure in PRs from forks.
