"""
Chart generation functions for Smart City Data Analyzer
"""

import matplotlib.pyplot as plt
from config import COLORS, CHART_DIMS


def create_traffic_chart(data):
    """Create traffic by area bar chart"""
    fig, ax = plt.subplots(figsize=CHART_DIMS["small"])
    ax.bar(
        data["Area"],
        data["Traffic"],
        color=COLORS["accent_primary"],
        edgecolor=COLORS["border_color"],
        linewidth=1.5,
    )
    _style_chart(ax, fig, "Area", "Traffic Level")
    return fig


def create_pollution_chart(data):
    """Create pollution by area bar chart"""
    fig, ax = plt.subplots(figsize=CHART_DIMS["small"])
    ax.bar(
        data["Area"],
        data["Pollution"],
        color=COLORS["accent_secondary"],
        edgecolor=COLORS["border_color"],
        linewidth=1.5,
    )
    _style_chart(ax, fig, "Area", "Pollution Level")
    return fig


def create_energy_chart(data):
    """Create energy consumption line chart"""
    fig, ax = plt.subplots(figsize=CHART_DIMS["large"])
    ax.plot(
        data["Area"],
        data["Energy"],
        color=COLORS["accent_primary"],
        marker="o",
        linewidth=2.5,
        markersize=8,
    )
    ax.fill_between(range(len(data)), data["Energy"], alpha=0.2, color=COLORS["accent_primary"])
    _style_chart(ax, fig, "Area", "Energy Consumption")
    ax.grid(True, alpha=0.1, color=COLORS["border_color"])
    return fig


def create_correlation_heatmap(correlation):
    """Create correlation heatmap"""
    fig, ax = plt.subplots(figsize=(8, 6))
    im = ax.imshow(
        correlation.values,
        cmap="coolwarm",
        aspect="auto",
        vmin=-1,
        vmax=1,
    )

    ax.set_xticks(range(len(correlation.columns)))
    ax.set_yticks(range(len(correlation.columns)))
    ax.set_xticklabels(correlation.columns, color=COLORS["text_secondary"], fontweight="600")
    ax.set_yticklabels(correlation.columns, color=COLORS["text_secondary"], fontweight="600")
    ax.set_facecolor(COLORS["bg_secondary"])
    fig.patch.set_facecolor(COLORS["bg_secondary"])

    # Add correlation values to heatmap
    for i in range(len(correlation.columns)):
        for j in range(len(correlation.columns)):
            ax.text(
                j,
                i,
                f"{correlation.values[i, j]:.2f}",
                ha="center",
                va="center",
                color="white",
                fontweight="600",
                fontsize=11,
            )

    plt.colorbar(im, ax=ax, label="Correlation")
    plt.tight_layout()
    return fig


def _style_chart(ax, fig, xlabel, ylabel):
    """Apply common styling to charts"""
    ax.set_facecolor(COLORS["bg_secondary"])
    fig.patch.set_facecolor(COLORS["bg_secondary"])

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color(COLORS["border_color"])
    ax.spines["bottom"].set_color(COLORS["border_color"])

    ax.tick_params(colors=COLORS["text_secondary"])
    ax.set_xlabel(xlabel, color=COLORS["text_secondary"], fontweight="600")
    ax.set_ylabel(ylabel, color=COLORS["text_secondary"], fontweight="600")

    plt.tight_layout()
