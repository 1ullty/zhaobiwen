---
name: "commit-and-push-github"
description: "Commit all pending changes and push the current project to GitHub. Invoke when the user asks to 提交到github/推送到github/push to github."
---

# Commit and Push to GitHub

Push the current project (`E:\vscode`) to the GitHub remote:
`https://github.com/1ullty/zhaobiwen.git`

## Prerequisite

If the `github` remote does not exist yet, add it first:
```
git remote add github https://github.com/1ullty/zhaobiwen.git
```

## Workflow

1. **Inspect** — run `git status`, `git diff`, `git diff --staged`, and `git log --oneline -10` (all in `E:\vscode`).
2. **Stage** — stage only intended files. Never stage secrets, `node_modules/`, or the `opencode*`/`pnpm*`/`cnpm*`/`pn*`/`pnx*` CLI shims (these are not project dependencies).
3. **Commit** — use a concise commit message that matches the repo style. Do not include secrets or credentials.
4. **Push** — `git -c http.sslVerify=false push github master`. If the remote branch doesn't exist yet, use `git -c http.sslVerify=false push -u github HEAD`.
5. **Never amend / force-push / create empty commits** unless the user explicitly asks.

## Notes

- The repo is a static HTML/CSS/JS coursework site. There is no build system or test suite — nothing to run before committing.
- User name for git config is 赵壁文.
- Gitee remote is named `origin` (`https://gitee.com/zhao-biwen/zhaobiwen109`); GitHub remote is named `github`.
- GitHub uses HTTPS (SSH port 22 is blocked by firewall). SSL verification is skipped due to certificate issues.
