---
name: codex-usage-chart
description: Fetch current Codex usage and show the five-hour and weekly limits as a bar chart when the user asks for a Codex usage chart or sends beep on its own.
---

# Codex usage chart

Find and call the current Codex usage-limits tool. Use live values and the tool's actual window names and reset times. Keep used and remaining percentages distinct. If a window is unavailable, label it unavailable. If live usage cannot be retrieved, report the blocker instead of reusing old figures.

Show the current five-hour and weekly windows as labeled bars on a common 0–100% scale, with numeric values and reset times when available. Use the user's timezone when formatting reset times. If rendering a PNG, save it as outputs/codex-usage.png in the active workspace and replace only that chart on refresh. Display the chart inline. If image rendering is unavailable, use text bars in the reply.
