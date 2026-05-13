# Security Audit Report — rich
Generated: 2026-05-13

## CI/CD Secret Inventory
Secrets referenced in `.github/workflows/*`:
- `CODECOV_TOKEN` (from `.github/workflows/pythonpackage.yml`)
- `GHP_README_WORKFLOW` (from `.github/workflows/readmechanged.yml`)

## Contributor Intelligence
Recent commit authors (last 20 commits queried):

| name | email | commit count |
|---|---|---:|
| shantanuv17 | 48430514+shantanuv17@users.noreply.github.com | 20 |

## Branch & Dependency Config
### Dependabot
From `.github/dependabot.yml`:
- Ecosystems: `pip`, `github-actions`
- Directory: `/`
- Schedule: `daily` for both

### Branch health / protection
- Default branch: `master`
- `master` reported as protected
- 3 stale `dependabot/*` branches (>30 days, no activity)
- Open PRs: 1 (no blocking reviews)

## Exposure Summary
- `CODECOV_TOKEN`: Could allow an attacker to upload spoofed coverage reports to Codecov, potentially obscuring CI quality signals. Risk: medium.
- `GHP_README_WORKFLOW`: Used with `gh api` GraphQL calls to post discussion comments when `README.md` changes. If exfiltrated, could permit unauthorized automated posting using repo-scoped token permissions, depending on token scopes. Risk: medium to high (integrity / spam / social engineering).

Overall, the repo’s workflow secret surface appears small, but protecting the discussion-posting token is particularly important because it can affect project communications.
