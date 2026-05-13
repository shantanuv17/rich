# Security Audit Report — rich
Generated: 2026-05-13

## CI/CD Secret Inventory
- `secrets.CODECOV_TOKEN` (referenced in `.github/workflows/pythonpackage.yml`)
- `secrets.GHP_README_WORKFLOW` (referenced in `.github/workflows/readmechanged.yml`)

## Contributor Intelligence
| Name | Email | Commit count (last 20 commits) |
|---|---|---:|
| shantanuv17 | 48430514+shantanuv17@users.noreply.github.com | 20 |

## Branch & Dependency Config
### Dependabot
- File: `.github/dependabot.yml`
- Update interval: `daily`
- Ecosystems:
  - `pip` (directory: `/`)
  - `github-actions` (directory: `/`)

### Branch health / protection
- Default branch: `master`
- `master`: protected; last commit: today
- Stale branches: 3 `dependabot/*` branches with >30 days inactivity
- Open PRs: 1 (no blocking reviews per branch health report)

## Exposure Summary
- `CODECOV_TOKEN`: if exfiltrated, could allow an attacker to upload/overwrite coverage results, potentially hiding test/coverage regressions or poisoning CI reporting.
- `GHP_README_WORKFLOW`: appears to be a GitHub token (or PAT) used to post to Discussions via `gh api graphql`. If exfiltrated, impact could include unauthorized repository/discussion interactions (posting comments, potentially broader scope depending on token permissions). This is likely the higher-impact secret and should be tightly scoped and rotated if exposure is suspected.
