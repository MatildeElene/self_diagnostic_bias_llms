
# =========================================================
# Publication-style plotting script for Study 2 (ADHD-C)
# =========================================================
from pathlib import Path
import matplotlib as mpl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# =========================================================
# 1. PATHS
# =========================================================

BASE = Path("/Users/matildeelene/Desktop/DS_PROJECTS/ADHD_LLM/adhd_llm_code")
PLOT_DIR = BASE / "out"
PLOT_DIR.mkdir(parents=True, exist_ok=True)

# =========================================================
# 2. GLOBAL STYLE
# =========================================================

def set_publication_style():
    mpl.rcParams.update({
        "font.family": "serif",
        "font.serif": ["Times New Roman", "Times", "DejaVu Serif"],
        "mathtext.fontset": "dejavuserif",

        "figure.dpi": 150,
        "savefig.dpi": 300,
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.04,

        "axes.linewidth": 0.6,
        "axes.labelsize": 9,
        "axes.titlesize": 10,

        "xtick.labelsize": 8.5,
        "ytick.labelsize": 8.5,
        "xtick.direction": "out",
        "ytick.direction": "out",
        "xtick.major.size": 3,
        "ytick.major.size": 3,

        "grid.linewidth": 0.5,
        "grid.alpha": 0.18,

        "legend.frameon": False,
        "legend.fontsize": 8,

        "axes.spines.top": False,
        "axes.spines.right": False,
    })

set_publication_style()

# =========================================================
# 3. PROXY DISTRIBUTION
# =========================================================
# Replace if needed, but this matches your thesis values:
# MEN = 38.69%, WOMEN = 61.31%

PROXY_GENDER_DIST_S2 = {
    "ADHD-C": {"MEN": 0.3869, "WOMEN": 0.6131}
}

# =========================================================
# 4. DATA LOADING
# =========================================================

def load_data(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    df["is_meaningful"] = df["pairing_clean"].isin({"MEN", "WOMEN"})
    return df[df["is_meaningful"]].copy()

# =========================================================
# 5. COLORS
# =========================================================

MEN_COLOR = "#c9cba3"
WOMEN_COLOR = "#ffe1a8"
PROXY_COLOR = "#e26d5c"

# =========================================================
# 6. SINGLE PANEL FUNCTION
# =========================================================

def _draw_panel(
    ax,
    df,
    subtype,
    proxy_dist,
    title=None,
    show_ylabel=False,
    row_label=None
):
    sub = df[
        (df["subtype"] == subtype) &
        (df["pairing_clean"].isin(["MEN", "WOMEN"]))
    ].copy()

    if sub.empty:
        ax.set_axis_off()
        return

    counts = sub["pairing_clean"].value_counts().reindex(
        ["MEN", "WOMEN"], fill_value=0
    )
    counts_arr = counts.to_numpy()
    perc = counts_arr / counts_arr.sum() * 100

    expected = np.array([
        proxy_dist[subtype]["MEN"] * 100,
        proxy_dist[subtype]["WOMEN"] * 100
    ])

    x = np.arange(2)
    labels = ["Men", "Women"]
    colors = [MEN_COLOR, WOMEN_COLOR]

    bars = ax.bar(
        x,
        perc,
        width=0.58,
        color=colors,
        edgecolor="none",
        linewidth=0,
        zorder=3
    )

    for xi, exp in zip(x, expected):
        ax.hlines(
            y=exp,
            xmin=xi - 0.29,
            xmax=xi + 0.29,
            linestyle=(0, (3, 2)),
            linewidth=1.0,
            color=PROXY_COLOR,
            alpha=0.85,
            zorder=4
        )

    for b, v in zip(bars, perc):
        ax.text(
            b.get_x() + b.get_width() / 2,
            v + 1.4,
            f"{v:.1f}%",
            ha="center",
            va="bottom",
            fontsize=8.2
        )

    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylim(0, 105)

    if show_ylabel:
        ax.set_ylabel("Observed percentage")

    if title:
        ax.set_title(title, fontweight="bold", pad=6)

    if row_label:
        ax.text(
            -0.26, 0.5, row_label,
            transform=ax.transAxes,
            rotation=90,
            va="center",
            ha="center",
            fontsize=9,
            fontweight="bold"
        )

    ax.grid(axis="y", color="#BDBDBD", alpha=0.25, zorder=0)
    ax.grid(axis="x", visible=False)

# =========================================================
# 7. MAIN STUDY 2 FIGURE
# =========================================================
def plot_study2(df_exp, df_imp, proxy_dist, out_path: Path):
    fig, axes = plt.subplots(2, 1, figsize=(4.2, 5.2), sharey=True)

    _draw_panel(
        axes[0],
        df_exp,
        subtype="ADHD-C",
        proxy_dist=proxy_dist,
        show_ylabel=True,
        row_label="Explicit"
    )

    _draw_panel(
        axes[1],
        df_imp,
        subtype="ADHD-C",
        proxy_dist=proxy_dist,
        show_ylabel=True,
        row_label="Implicit"
    )

    fig.suptitle("ADHD-C", fontsize=10, fontweight="bold", y=0.965)

    legend_handles = [
        Line2D([0], [0], color=MEN_COLOR, lw=6, label="Men"),
        Line2D([0], [0], color=WOMEN_COLOR, lw=6, label="Women"),
        Line2D([0], [0], color=PROXY_COLOR, lw=1.0,
               linestyle=(0, (3, 2)), label="Expected (proxy)")
    ]

    fig.legend(
        handles=legend_handles,
        loc="lower center",
        bbox_to_anchor=(0.5, 0.02),
        ncol=3,
        handlelength=1.8,
        columnspacing=1.8
    )

    plt.subplots_adjust(
        left=0.24,
        right=0.97,
        top=0.88,
        bottom=0.16,
        hspace=0.45
    )

    fig.savefig(out_path)
    plt.close(fig)
    print(f"Saved: {out_path}")

# =========================================================
# 8. OPTIONAL: SEPARATE FIGURES
# =========================================================

def plot_single_condition(df, proxy_dist, out_path: Path, panel_title="Explicit"):
    fig, ax = plt.subplots(figsize=(4.4, 3.8))

    _draw_panel(
        ax,
        df=df,
        subtype="ADHD-C",
        proxy_dist=proxy_dist,
        title=panel_title,
        show_ylabel=True
    )

    legend_handles = [
        Line2D([0], [0], color=MEN_COLOR, lw=6, label="Men"),
        Line2D([0], [0], color=WOMEN_COLOR, lw=6, label="Women"),
        Line2D([0], [0], color=PROXY_COLOR, lw=1.0,
               linestyle=(0, (3, 2)), label="Expected (proxy)")
    ]

    ax.legend(
        handles=legend_handles,
        ncol=3,
        loc="upper center",
        bbox_to_anchor=(0.5, 1.02),
        handlelength=1.8,
        columnspacing=1.5
    )

    plt.tight_layout()
    fig.savefig(out_path)
    plt.close(fig)
    print(f"Saved: {out_path}")


import matplotlib.pyplot as plt

# Data
metrics = ['LMS', 'MPS']
women = [89.55, 12.31]
men = [38.7, 5.33]

y_pos = range(len(metrics))

fig, ax = plt.subplots(figsize=(4.2, 2.8))

# Draw connecting lines (dumbbells)
for i in y_pos:
    ax.plot([men[i], women[i]], [i, i])

# Plot points
ax.scatter(women, y_pos, label='Women-associated prompts')
ax.scatter(men, y_pos, label='Men-associated prompts')

# Labels
ax.set_yticks(y_pos)
ax.set_yticklabels(metrics)
ax.set_xlabel('Score')

# Optional: annotate values (nice for papers)
for i in y_pos:
    ax.text(women[i] + 1, i, f'{women[i]:.1f}', va='center', fontsize=8)
    ax.text(men[i] - 1, i, f'{men[i]:.1f}', va='center', ha='right', fontsize=8)

# Clean style (publication-friendly)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.legend(frameon=False, loc='lower right')

plt.tight_layout()
plt.show()


# =========================================================

# 9. RUN
# =========================================================

if __name__ == "__main__":
    df_exp = load_data(
        BASE / "data/S2_explicit_pairings.csv"
    )

    df_imp = load_data(
        BASE / "data/S2_implicit_pairings.csv"
    )

    # Main side-by-side figure
    plot_study2(
        df_exp=df_exp,
        df_imp=df_imp,
        proxy_dist=PROXY_GENDER_DIST_S2,
        out_path=PLOT_DIR / "figure_main_s2.pdf"
    )

    # Optional single-condition figures
    plot_single_condition(
        df=df_exp,
        proxy_dist=PROXY_GENDER_DIST_S2,
        out_path=PLOT_DIR / "figure_s2_explicit.pdf",
        panel_title="Explicit"
    )

    plot_single_condition(
        df=df_imp,
        proxy_dist=PROXY_GENDER_DIST_S2,
        out_path=PLOT_DIR / "figure_s2_implicit.pdf",
        panel_title="Implicit"
    )