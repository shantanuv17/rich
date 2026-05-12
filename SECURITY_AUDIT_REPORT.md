# Security Audit Report — shantanuv17/rich
Generated: 2026-05-12

## CI/CD Secret Inventory
- `CODECOV_TOKEN`
- `GHP_README_WORKFLOW`

## Contributor Intelligence
| Name | Email | Commit count (last 20) |
|---|---|---:|
| shantanuv17 | 48430514+shantanuv17@users.noreply.github.com | 6 |
| Shantanu Verma | shantanu.verma@orange.com | 6 |
| Will McGugan | willmcgugan@gmail.com | 8 |

## Branch & Dependency Config
### Dependabot
- Ecosystems monitored:
  - `pip` (directory: `/`)
  - `github-actions` (directory: `/`)
- Schedule: `daily` for both ecosystems

### Branch protection details
- Not discoverable via the available repository content/tooling in this analysis run.
- Observed default branch usage in workflows: `master`.

## Exposure Summary
- `GHP_README_WORKFLOW`: High impact if exfiltrated. It is used as a `GITHUB_TOKEN` for `gh api graphql` to post a discussion comment; compromise could enable unauthorized actions permitted by that token’s scopes (e.g., writing to discussions / repository resources depending on granted permissions).
- `CODECOV_TOKEN`: Medium impact. Primarily allows uploading coverage reports to Codecov for this repository; compromise could allow poisoning coverage uploads/metadata, but is generally lower impact than a broadly scoped GitHub token.
