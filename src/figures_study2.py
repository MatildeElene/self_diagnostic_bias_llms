
#plots for study 2
from pathlib import Path
import matplotlib as mpl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# setting repository root:
BASE_DIR = Path(__file__).resolve().parent.parent

RESPONSES_DIR = BASE_DIR / "results" / "responses"

FIGURE_DIR = BASE_DIR / "out" / "figures"
FIGURE_DIR.mkdir(parents=True, exist_ok=True)

out_path = 

# setting global style
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

# Clinically informed proxy gender distributions derived from
# Platania et al. (2025).
PROXY_GENDER_DIST = {
    "ADHD-I": {"MEN": 0.4076, "WOMEN": 0.5924},
    "ADHD-HI": {"MEN": 0.2727, "WOMEN": 0.7273},
    "ADHD-C": {"MEN": 0.3869, "WOMEN": 0.6131},
}

#loading data
def load_data(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(
            f"Required response file not found: {path}"
        )

    df = pd.read_csv(path)

    required_columns = {"pairing_clean", "subtype"}
    missing = required_columns - set(df.columns)

    if missing:
        raise ValueError(
            f"{path.name} is missing required columns: {sorted(missing)}"
        )

    df["is_meaningful"] = df["pairing_clean"].isin({"MEN", "WOMEN"})

    return df[df["is_meaningful"]].copy()

# color palette (as in R)
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
    ax.set_ylim(0, 105)

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

# main study 2 figure
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

# optional appendix figures
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


# run main: 
if __name__ == "__main__":
    df_exp = load_data(
        RESPONSES_DIR / "s2_ex_responses.csv"
    )

    df_imp = load_data(
        RESPONSES_DIR / "s2_im_responses.csv"
    )

    # Main side-by-side figure
    plot_study2(
        df_exp,
        df_imp,
        proxy_dist=PROXY_GENDER_DIST,
        out_path=FIGURE_DIR / "figure_main_s2.png"
    )

    # Optional single-condition figures
    plot_single_condition(
        df=df_exp,
        proxy_dist=PROXY_GENDER_DIST,
        out_path=FIGURE_DIR / "figure_s2_explicit.png"
    )

    plot_single_condition(
        df=df_imp,
        proxy_dist=PROXY_GENDER_DIST,
        out_path=FIGURE_DIR / "figure_s2_implicit.png"
    )