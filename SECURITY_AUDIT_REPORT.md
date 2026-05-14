# Security Audit Report — rich
Generated: 2026-05-14

## CI/CD Secret Inventory
- CODECOV_TOKEN (from .github/workflows/pythonpackage.yml)
- GHP_README_WORKFLOW (from .github/workflows/readmechanged.yml)

## Contributor Intelligence
name | email | commit count (last 20 commits)
- shantanuv17 | 48430514+shantanuv17@users.noreply.github.com | 20

## Branch & Dependency Config
### Dependabot
- File: .github/dependabot.yml
- Ecosystems:
  - pip (directory: /) — schedule: daily
  - github-actions (directory: /) — schedule: daily

### Branch protection / health
- master: protected; last commit: today
- dependabot/*: 3 stale branches (>30 days, no activity)
- Recommendation: delete 3 stale dependabot branches

## Exposure Summary
- CODECOV_TOKEN: could allow unauthorized uploads / manipulation of coverage reporting; moderate risk.
- GHP_README_WORKFLOW: likely a fine-grained token used to post to GitHub Discussions via GraphQL; could enable spam or unauthorized discussion comments; potentially higher repo/community-impact risk.
