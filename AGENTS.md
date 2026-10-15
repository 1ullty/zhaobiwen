# AGENTS.md

Static HTML/CSS coursework site for the class 《高级网页设计》 (student 赵壁文).
No build system, no package manager, no tests, and **not a git repo**.

`node_modules/` and the `opencode*`, `pnpm*`, `cnpm*`, `pn*`, `pnx*` files are only the
OpenCode CLI and package-manager shims — they are **not** project dependencies. Do not run
installs or treat this as a Node project.

## Layout
- `index.html` — hand-written catalog page linking every lesson; also embeds the original prompt. This is the entrypoint.
- `N-M 描述.html` — one self-contained native HTML/CSS lesson page (`2-1.html` … `10-4.html`).
- `CSS.css` — shared stylesheet referenced by `5-1 层叠与继承.html`.
- `img/` — images (`1.jpg`–`6.jpg`) used by lesson pages.
- `_backup/` — old `index-v1.html` plus `_verify_links.py` (link checker).
- `_shots/` — reference screenshots `index_desktop.png`, `index_mobile.png`.

## Project Rules
- **命名规则**：所有 CSS 类名、id 名、JS 变量名都必须以 `zhao_` 开头。
- **提示词存档**：执行任何任务前，先把本次提示词以**追加**方式写入 `zhao_prompt.md`（不覆盖已有内容）。写入内容包含：
  - 时间（格式 `yyyy-mm-dd-hh-mm`）
  - 使用的模型
  - 提示词原文

## Conventions
- Native HTML/CSS only; no CDN or external resources (the page's original prompt requires this). Keep pages self-contained.
- Lesson filenames contain spaces and Chinese characters. In `index.html` every `href` must stay URL-encoded (`%20`, percent-encoded CJK). Do not rename files or "fix" the encoding.
- All files are UTF-8. Chinese can show as mojibake in some terminals; the files themselves are fine.

## Known gotchas
- `index.html` is stale: it lists 13 lessons (`2-1`…`9-1`), but `10-1 animation.html`, `10-2.html`, `10-3.html`, `10-4.html` exist on disk and are unlinked. When adding a lesson, add a card and update the `共 N 个实践作品` count.
- `5-1 层叠与继承.html` references `css.css` (lowercase) while the file is `CSS.css`; works on Windows, breaks on case-sensitive hosts.
- Lesson pages are student work with legacy malformed markup (e.g. duplicated `</body></html>` in `5-1`, `<from>` typo in `3-1 form.html`). Do not silently rewrite lesson content.

## Verifying links
Use the real Python launcher (`python` is the Windows Store stub and silently does nothing):
```
py -3 _backup\_verify_links.py
```
It prints all links, any missing target, and any on-disk lesson not linked from `index.html`.
The path inside the script is hardcoded to `E:\vscode`.
