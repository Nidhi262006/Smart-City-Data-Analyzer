import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Smart City Data Analyzer")

uploaded_file = st.file_uploader("Upload City Dataset", type=["csv"])

METRIC_CONFIG = {
    "Traffic": {
        "column": "Traffic",
        "chart_type": "bar",
        "title": "Traffic by Area",
        "ylabel": "Traffic Level",
        "color": "#2196F3",
    },
    "Pollution": {
        "column": "Pollution",
        "chart_type": "bar",
        "title": "Pollution by Area",
        "ylabel": "Pollution Level",
        "color": "#FF5722",
    },
    "Energy Consumption": {
        "column": "Energy",
        "chart_type": "line",
        "title": "Energy Usage by Area",
        "ylabel": "Energy (kWh)",
        "color": "#4CAF50",
    },
}

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

    st.write("Dataset Preview")
    st.write(data.head())

    st.write("Basic Statistics")
    st.write(data.describe())

    st.subheader("Metric Visualization")
    selected_metric = st.selectbox(
        "Select a city metric to visualize:",
        options=list(METRIC_CONFIG.keys()),
        index=0,
    )

    config = METRIC_CONFIG[selected_metric]
    col = config["column"]

    if col in data.columns:
        fig, ax = plt.subplots(figsize=(10, 5))

        if config["chart_type"] == "bar":
            ax.bar(data["Area"], data[col], color=config["color"])
        else:
            ax.plot(data["Area"], data[col], marker="o", color=config["color"])

        ax.set_title(config["title"], fontsize=14, fontweight="bold")
        ax.set_xlabel("Area", fontsize=12)
        ax.set_ylabel(config["ylabel"], fontsize=12)
        ax.tick_params(axis="x", rotation=45)
        plt.tight_layout()
        st.pyplot(fig)
    else:
        st.warning(f"Column '{col}' not found in the dataset.")

    st.subheader("Key Insights")
    for metric_name, cfg in METRIC_CONFIG.items():
        c = cfg["column"]
        if c in data.columns:
            max_row = data.loc[data[c].idxmax()]
            st.write(f"**{metric_name}**: {max_row['Area']} ({max_row[c]})")

    st.subheader("Correlation Analysis")
    correlation = data.corr(numeric_only=True)
    st.write(correlation)

    st.subheader("Dataset Visualization")
    st.dataframe(data)
