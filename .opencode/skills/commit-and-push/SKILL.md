---
name: commit-and-push
description: Commit all pending changes and push the current project to the Gitee remote (https://gitee.com/zhao-biwen/zhaobiwen109). Use when the user asks to 提交/推送/commit/push the project.
---

# Commit and Push to Gitee

Push the current project (`E:\vscode`) to the Gitee remote:
`https://gitee.com/zhao-biwen/zhaobiwen109`

## Workflow

1. **Inspect** — run `git status`, `git diff`, `git diff --staged`, and `git log --oneline -10` (all in `E:\vscode`).
2. **Stage** — stage only intended files. Never stage secrets, `node_modules/`, or the `opencode*`/`pnpm*`/`cnpm*`/`pn*`/`pnx*` CLI shims (these are not project dependencies).
3. **Commit** — use a concise commit message that matches the repo style. Do not include secrets or credentials.
4. **Push** — `git push` to the tracked remote. If the remote branch doesn't exist yet, use `git push -u origin HEAD`.
5. **Never amend / force-push / create empty commits** unless the user explicitly asks.

## Notes

- The repo is a static HTML/CSS coursework site. There is no build system or test suite — nothing to run before committing.
- User name for git config is 赵壁文.
- Current model ID: `opencode/longcat-2.5-preview-free` (use as author when none configured).
