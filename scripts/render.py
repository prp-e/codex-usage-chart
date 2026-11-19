"""Render a personalized Codex usage snapshot from JSON on stdin."""
import argparse
import json
from pathlib import Path
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def render(snapshot, output):
    windows = snapshot["windows"]
    if len(windows) != 2:
        raise ValueError("Expected the five-hour and weekly windows.")

    ink = "#122238"
    muted = "#4c6077"
    accent = "#176c64"
    track = "#e7edf3"

    fig = plt.figure(figsize=(8, 6), facecolor="#f6f8fb")
    name = snapshot.get("name")
    if name:
        fig.text(0.09, 0.911, name, color=accent, fontsize=16, weight="semibold",
                 parse_math=False)
    fig.text(0.09, 0.824, "Codex usage", color=ink, fontsize=35, weight="bold")

    ax = fig.add_axes([0.09, 0.153, 0.82, 0.61], facecolor=fig.get_facecolor())
    ax.set(xlim=(0, 100), ylim=(0, 2), yticks=[])
    ticks = range(0, 101, 25)
    ax.set_xticks(ticks, [f"{tick}%" for tick in ticks], color=muted, fontsize=10)
    ax.tick_params(axis="x", length=0, pad=9)
    for spine in ax.spines.values():
        spine.set_visible(False)
    for tick in ticks:
        ax.vlines(tick, 0, 1.55, color="#d8e1eb", linewidth=0.8, zorder=0)

    for window, y in zip(windows, (1.37, 0.40)):
        used = window.get("used")
        ax.text(0, y + 0.25, window["label"], color=ink, fontsize=15,
                weight="bold", parse_math=False)
        if used is None:
            ax.barh(y, 100, height=0.17, color=track, hatch="//", edgecolor="#d0dae6")
            summary = "Usage unavailable"
        else:
            if not 0 <= used <= 100:
                raise ValueError("Used percentage must be between 0 and 100.")
            ax.barh(y, 100, height=0.17, color=track)
            ax.barh(y, used, height=0.17, color=accent)
            summary = f"{used:.12g}% used  ·  {100 - used:.12g}% remaining"
        ax.text(100, y + 0.25, summary, ha="right", color=muted, fontsize=11)
        if window.get("reset"):
            ax.text(0, y - 0.26, f'Resets {window["reset"]}', color=muted,
                    fontsize=11, parse_math=False)

    output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output, dpi=160)
    plt.close(fig)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path("outputs/codex-usage.png"))
    render(json.load(sys.stdin), parser.parse_args().output)
