"""
Smart City Data Analyzer - Main Application

A modern Streamlit dashboard for analyzing urban city data including
traffic patterns, pollution levels, and energy consumption.
"""

import streamlit as st
from config import PAGE_CONFIG
from styles import get_custom_css
from components import (
    render_header,
    render_upload_section,
    render_section_heading,
    render_metrics_row,
    render_insights_row,
)
from analytics import (
    load_data,
    calculate_metrics,
    get_key_insights,
    get_correlation_matrix,
    get_statistics,
)
from charts import (
    create_traffic_chart,
    create_pollution_chart,
    create_energy_chart,
    create_correlation_heatmap,
)

# ===== PAGE CONFIGURATION =====
st.set_page_config(**PAGE_CONFIG)

# ===== APPLY CUSTOM STYLING =====
st.markdown(get_custom_css(), unsafe_allow_html=True)

# ===== RENDER HEADER =====
render_header()

# ===== UPLOAD SECTION =====
uploaded_file = render_upload_section()

# ===== MAIN CONTENT (only if CSV is uploaded) =====
if uploaded_file is not None:

    # Load and process data
    data = load_data(uploaded_file)
    metrics = calculate_metrics(data)
    insights = get_key_insights(data)
    correlation = get_correlation_matrix(data)
    statistics = get_statistics(data)

    # ===== DATASET OVERVIEW SECTION =====
    render_section_heading("overview")
    render_metrics_row(metrics)

    # ===== DATASET PREVIEW SECTION =====
    render_section_heading("preview")
    with st.container():
        st.dataframe(data, use_container_width=True, hide_index=True)
        st.download_button(
            label="Download CSV",
            data=data.to_csv(index=False),
            file_name="analyzed_dataset.csv",
            mime="text/csv",
        )

    # ===== URBAN ANALYTICS SECTION =====
    render_section_heading("analytics")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Traffic by Area")
        st.pyplot(create_traffic_chart(data), use_container_width=True)

    with col2:
        st.markdown("### Pollution by Area")
        st.pyplot(create_pollution_chart(data), use_container_width=True)

    # Energy chart (full width)
    st.markdown("### Energy Consumption by Area")
    st.pyplot(create_energy_chart(data), use_container_width=True)

    # ===== KEY INSIGHTS SECTION =====
    render_section_heading("insights")
    render_insights_row(insights)

    # ===== CORRELATION ANALYSIS SECTION =====
    render_section_heading("correlation")
    st.pyplot(create_correlation_heatmap(correlation), use_container_width=True)
    st.markdown("#### Correlation Matrix")
    st.dataframe(correlation, use_container_width=True)

    # ===== DATASET STATISTICS SECTION =====
    render_section_heading("statistics")
    st.dataframe(statistics, use_container_width=True)

    # ===== FULL DATASET SECTION =====
    render_section_heading("visualization")
    st.markdown("#### Full Dataset")
    st.dataframe(data, use_container_width=True, hide_index=True)