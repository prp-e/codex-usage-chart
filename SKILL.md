---
name: codex-usage-chart
description: Fetch live Codex usage and show the five-hour and weekly limits as a personalized Matplotlib bar chart when the user asks for a Codex usage chart or sends beep on its own.
---

# Codex usage chart

1. Find and call the current Codex usage-limits tool. Use its live window names, usage percentages, and reset timestamps. If the live lookup fails, report the blocker. If an individual window is absent, show it as unavailable.
2. Use the user's stated display name, a display name from a connected profile, or the local account's full name (`id -F` on macOS) if it looks like a real name. Prefer an explicit name over local account information. If none is available, omit the name and keep the chart title. Use the user's timezone for reset times.
3. Run [the Matplotlib renderer](scripts/render.py) using a Python environment with Matplotlib. Pass the skill directory's absolute script path and run from the active workspace so the default output is `outputs/codex-usage.png`. Embed that PNG inline using its absolute path. Each refresh replaces only that chart.

Pass a JSON object on stdin with `name` and exactly two `windows` entries (five-hour first, weekly second). Each entry takes `label`, `used` (a percentage from 0 to 100, or null), and optional `reset` (a locally formatted string including the timezone). The renderer places the name above the title, keeps all bars on a shared 0–100% scale, and distinguishes used from remaining.

If Matplotlib is missing, look for a Python environment that already has it or install it into an isolated workspace environment if available. If rendering is unavailable, report the blocker and present labeled text bars with live percentages and reset times.
