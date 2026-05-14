# Security Audit Report — rich
Generated: 2026-05-14

## CI/CD Secret Inventory
The following GitHub Actions secrets are referenced in workflow files:
- `CODECOV_TOKEN` (in `.github/workflows/pythonpackage.yml`)
- `GHP_README_WORKFLOW` (in `.github/workflows/readmechanged.yml`)

## Contributor Intelligence
Most recent 20 commits (author | email | commit count in sample):
- shantanuv17 | 48430514+shantanuv17@users.noreply.github.com | 20

## Branch & Dependency Config
### Dependabot
Configured in `.github/dependabot.yml`:
- Ecosystems: `pip` (directory `/`), `github-actions` (directory `/`)
- Schedule: daily updates for both ecosystems

### Branch health / protection
- `master`: protected; last commit: today
- `dependabot/*`: 3 stale branches (>30 days, no activity)
Recommendation: delete stale dependabot branches if no longer needed.

## Exposure Summary
- `GHP_README_WORKFLOW`: likely a GitHub token with permissions to post to Discussions via `gh api graphql`; if exfiltrated could allow spam / unauthorized comments depending on granted scopes.
- `CODECOV_TOKEN`: could allow an attacker to upload spoofed coverage reports to Codecov for this repo.

Overall, secrets exposure risk depends on scopes granted to each secret. Prefer fine-grained tokens with least privilege, rotate periodically, and restrict workflow permissions where possible.
