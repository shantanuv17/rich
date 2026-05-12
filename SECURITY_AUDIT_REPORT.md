# Security Audit Report — shantanuv17/rich
Generated: 2026-05-12

## CI/CD Secret Inventory
- CODECOV_TOKEN
- GHP_README_WORKFLOW

## Contributor Intelligence
name | email | commit count
- shantanuv17 | 48430514+shantanuv17@users.noreply.github.com | 14
- Shantanu Verma | shantanu.verma@orange.com | 6

## Branch & Dependency Config
- Default branch observed: `master`
- Branch protection (from API branch listing): `master` protected = false

Dependabot (`.github/dependabot.yml`):
- Ecosystems monitored:
  - `pip` (directory `/`)
  - `github-actions` (directory `/`)
- Schedule:
  - interval: `daily` (for both ecosystems)

## Exposure Summary
- `CODECOV_TOKEN`: would allow uploading/altering coverage reports in Codecov for this repository, potentially masking test failures/coverage regressions or poisoning CI signals.
- `GHP_README_WORKFLOW`: a GitHub token used by the README-changed workflow to post a Discussion comment via the GitHub CLI (`gh api graphql`). If exfiltrated, could be abused to comment in GitHub Discussions (and potentially other scopes granted to that token), enabling spam/social engineering or workflow abuse depending on its permissions.

Overall highest impact depends on `GHP_README_WORKFLOW` scopes; broadly, GitHub-scoped tokens with write permissions tend to be more damaging than third-party service tokens because they can alter repository-facing content.
