# Codex Usage Chart

**Type `beep` in Codex to see how much usage you have left and when it resets.**

Codex Usage Chart is a skill that turns your live five-hour and weekly limits into a personalized Matplotlib chart. It shows both windows on the same 0–100% scale, with your display name above the chart and reset times in your timezone.

## Quick start

Clone the skill into your personal Codex skills directory.

```sh
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
git clone https://github.com/prp-e/codex-usage-chart.git \
  "${CODEX_HOME:-$HOME/.codex}/skills/codex-usage-chart"
```

Use a Python environment with Matplotlib available if you want the PNG chart. Then open Codex and send:

```text
beep
```

You can also ask **“Show my Codex usage chart”** or invoke **`$codex-usage-chart`** directly. This skill requires a Codex session with access to the live usage-limits tool.

## What you’ll see

| Window | Used | Remaining | Resets |
| :-- | --: | --: | :-- |
| Five-hour | 17% | 83% | Today at 17:31 |
| Weekly | 3% | 97% | Nov 26 at 12:31 |

*Illustrative values. Each request fetches a fresh snapshot.*

The 4:3 chart is displayed inline and saved to `outputs/codex-usage.png` in the active workspace. A refresh replaces that PNG. If an individual usage window is unavailable, the chart labels it accordingly. If PNG rendering is unavailable, the skill returns the live figures as text bars.

## Repository

- [`SKILL.md`](SKILL.md) defines the live lookup, personalization, and fallback behavior.
- [`scripts/render.py`](scripts/render.py) turns the usage snapshot into a 1280 × 960 PNG.
