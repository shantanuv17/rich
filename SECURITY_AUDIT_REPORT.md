# Security Audit Report — rich
Generated: 2026-05-13

## CI/CD Secret Inventory
- CODECOV_TOKEN (referenced in .github/workflows/pythonpackage.yml)
- GHP_README_WORKFLOW (referenced in .github/workflows/readmechanged.yml)

## Contributor Intelligence
| name | email | commit count (last 20 commits) |
|---|---|---:|
| shantanuv17 | 48430514+shantanuv17@users.noreply.github.com | 20 |

## Branch & Dependency Config
### Dependabot
- Ecosystems: pip, github-actions
- Directory: /
- Schedule: daily (both)

### Branch protection
Not assessed via API in this session.

## Exposure Summary
- **GHP_README_WORKFLOW**: GitHub token used to post GraphQL discussion comments; if exfiltrated it could enable unauthorized GitHub API actions within the token’s scope.
- **CODECOV_TOKEN**: Used to upload coverage reports to Codecov; exposure could permit uploading spoofed coverage data and potentially read/alter coverage reporting for the project.
