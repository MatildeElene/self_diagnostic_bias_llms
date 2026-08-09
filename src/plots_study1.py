# =========================================================
# Publication-style plotting script for Study 1
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
# 3. PROXY DISTRIBUTIONS
# =========================================================

PROXY_GENDER_DIST = {
    "ADHD-I": {"MEN": 0.4076, "WOMEN": 0.5924},
    "ADHD-HI": {"MEN": 0.2727, "WOMEN": 0.7273},
    "ADHD-C": {"MEN": 0.3869, "WOMEN": 0.6131},
}

# =========================================================
# 4. DATA LOADING
# =========================================================

def load_data(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    df["is_meaningful"] = df["pairing_clean"].isin({"MEN", "WOMEN"})
    return df[df["is_meaningful"]].copy()

# =========================================================
# COLOR PALETTE (publication-ready, warm tones)
# =========================================================

MEN_COLOR = "#c9cba3" 
WOMEN_COLOR = "#ffe1a8"    
PROXY_COLOR = "#e26d5c"    # Bittersweet (dark)

# =========================================================
# 6. PANEL FUNCTION
# =========================================================

def _draw_panel(
    ax,
    df,
    subtype,
    proxy_dist,
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

    # Expected lines
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

    # Percentage labels only
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
    ax.set_ylim(0, 100)

    if show_ylabel:
        ax.set_ylabel("Observed percentage")

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
# 7. MAIN 2x2 FIGURE
# =========================================================

def plot_2x2(df_exp, df_imp, proxy_dist, out_path: Path):
    fig, axes = plt.subplots(2, 2, figsize=(7.0, 5.2), sharey=True)
    subtypes = ["ADHD-I", "ADHD-HI"]

    for j, st in enumerate(subtypes):
        axes[0, j].set_title(st, fontweight="bold", pad=6)

    for j, st in enumerate(subtypes):
        _draw_panel(
            axes[0, j],
            df_exp,
            st,
            proxy_dist,
            show_ylabel=(j == 0),
            row_label="Explicit" if j == 0 else None
        )

    for j, st in enumerate(subtypes):
        _draw_panel(
            axes[1, j],
            df_imp,
            st,
            proxy_dist,
            show_ylabel=(j == 0),
            row_label="Implicit" if j == 0 else None
        )

    legend_handles = [
        Line2D([0], [0], color=MEN_COLOR, lw=6, label="Men"),
        Line2D([0], [0], color=WOMEN_COLOR, lw=6, label="Women"),
        Line2D([0], [0], color=PROXY_COLOR, lw=1.0, linestyle=(0, (3, 2)),
               label="Expected (proxy)")
    ]

    fig.legend(
        handles=legend_handles,
        loc="lower center",
        bbox_to_anchor=(0.5, -0.01),
        ncol=3,
        handlelength=1.8,
        columnspacing=1.8
    )

    plt.tight_layout(rect=[0, 0.05, 1, 0.92])
    fig.savefig(out_path)
    plt.close(fig)
    print(f"Saved: {out_path}")

# =========================================================
# 8. OPTIONAL APPENDIX FIGURE
# =========================================================

def plot_within_subtype(df, proxy_dist, out_path: Path, task_label="Implicit"):
    subtypes = ["ADHD-I", "ADHD-HI"]
    genders = ["MEN", "WOMEN"]

    fig, ax = plt.subplots(figsize=(5.5, 3.7))
    x = np.arange(len(subtypes))
    width = 0.32

    gender_colors = {
        "MEN": MEN_COLOR,
        "WOMEN": WOMEN_COLOR,
    }

    for i, g in enumerate(genders):
        offset = -width / 2 if i == 0 else width / 2

        heights = []
        for st in subtypes:
            sub = df[df["subtype"] == st]
            counts = sub["pairing_clean"].value_counts().reindex(genders, fill_value=0)
            total = counts.sum()
            heights.append((counts[g] / total) * 100 if total > 0 else np.nan)

        bars = ax.bar(
            x + offset,
            heights,
            width=width,
            label=g.title(),
            color=gender_colors[g],
            edgecolor="none",
            linewidth=0.00,
            zorder=3
        )

        for b, h in zip(bars, heights):
            if np.isnan(h):
                continue
            ax.text(
                b.get_x() + b.get_width() / 2,
                h + 1.3,
                f"{h:.1f}%",
                ha="center",
                va="bottom",
                fontsize=8.0
            )

        for j, st in enumerate(subtypes):
            exp = proxy_dist[st][g] * 100
            ax.hlines(
                y=exp,
                xmin=(x[j] + offset) - width * 0.45,
                xmax=(x[j] + offset) + width * 0.45,
                linestyle=(0, (3, 2)),
                linewidth=1.0,
                color=PROXY_COLOR,
                alpha=0.85,
                zorder=4
            )

    ax.set_xticks(x)
    ax.set_xticklabels(subtypes)
    ax.set_ylim(0, 100)
    ax.set_ylabel("Observed percentage within subtype")


    ax.grid(axis="y", color="#BDBDBD", alpha=0.25, zorder=0)
    ax.grid(axis="x", visible=False)

    legend_handles = [
        Line2D([0], [0], color=MEN_COLOR, lw=6, label="Men"),
        Line2D([0], [0], color=WOMEN_COLOR, lw=6, label="Women"),
        Line2D([0], [0], color=PROXY_COLOR, lw=1.0, linestyle=(0, (3, 2)),
               label="Expected (proxy)")
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

# =========================================================
# 9. RUN
# =========================================================

if __name__ == "__main__":
    df_imp = load_data(
        BASE / "data/S1_implicit_pairings_true.csv"
    )

    df_exp = load_data(
        BASE / "data/S1_explicit_pairings.csv"
    )

    plot_2x2(
        df_exp,
        df_imp,
        PROXY_GENDER_DIST,
        out_path=PLOT_DIR / "figure_main_s1.pdf"
    )

    plot_within_subtype(
        df_imp,
        PROXY_GENDER_DIST,
        out_path=PLOT_DIR / "figure_appendix_s1_implicit.pdf",
        task_label="Implicit"
    )

    plot_within_subtype(
        df_exp,
        PROXY_GENDER_DIST,
        out_path=PLOT_DIR / "figure_appendix_s1_explicit.pdf",
        task_label="Explicit"
    )