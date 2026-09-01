"""
UI Component functions for Smart City Data Analyzer
"""

import streamlit as st
from config import COLORS, SECTIONS


def render_header():
    """Render dashboard header"""
    header_html = f"""
    <div class="dashboard-header">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; padding-bottom: 16px; border-bottom: 1px solid {COLORS['border_color']};">
            <div style="color: {COLORS['accent_primary']}; font-size: 12px; font-weight: 700; letter-spacing: 2px; text-transform: uppercase;">SMART CITY ANALYTICS</div>
            <div style="color: {COLORS['success']}; font-size: 12px; font-weight: 600; display: flex; align-items: center; gap: 8px;">
                <span style="width: 6px; height: 6px; background-color: {COLORS['success']}; border-radius: 50%; display: inline-block;"></span>DASHBOARD ACTIVE
            </div>
        </div>
        <div style="margin-bottom: 24px;">
            <h1 style="color: {COLORS['text_primary']}; font-size: 28px; font-weight: 700; margin: 0 0 10px 0;">Smart City Data Analyzer</h1>
            <p style="color: {COLORS['text_secondary']}; font-size: 14px; line-height: 1.6; margin: 0;">Urban intelligence at a glance. Monitor traffic, pollution and energy across city areas.</p>
        </div>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px;">
            <div style="background-color: {COLORS['bg_primary']}; border: 1px solid {COLORS['border_color']}; border-radius: 10px; padding: 18px; text-align: center;">
                <div style="font-size: 28px; margin-bottom: 10px;">🚦</div>
                <h3 style="color: {COLORS['text_primary']}; font-size: 15px; font-weight: 700; margin: 0 0 6px 0;">Traffic</h3>
                <p style="color: {COLORS['text_secondary']}; font-size: 13px; margin: 0; line-height: 1.4;">Monitor traffic across city areas</p>
            </div>
            <div style="background-color: {COLORS['bg_primary']}; border: 1px solid {COLORS['border_color']}; border-radius: 10px; padding: 18px; text-align: center;">
                <div style="font-size: 28px; margin-bottom: 10px;">🌫️</div>
                <h3 style="color: {COLORS['text_primary']}; font-size: 15px; font-weight: 700; margin: 0 0 6px 0;">Pollution</h3>
                <p style="color: {COLORS['text_secondary']}; font-size: 13px; margin: 0; line-height: 1.4;">Track pollution levels</p>
            </div>
            <div style="background-color: {COLORS['bg_primary']}; border: 1px solid {COLORS['border_color']}; border-radius: 10px; padding: 18px; text-align: center;">
                <div style="font-size: 28px; margin-bottom: 10px;">⚡</div>
                <h3 style="color: {COLORS['text_primary']}; font-size: 15px; font-weight: 700; margin: 0 0 6px 0;">Energy</h3>
                <p style="color: {COLORS['text_secondary']}; font-size: 13px; margin: 0; line-height: 1.4;">Analyze energy consumption</p>
            </div>
        </div>
    </div>
    """
    st.markdown(header_html, unsafe_allow_html=True)


def render_upload_section():
    """Render file upload section"""
    upload_html = f"""
    <div style="background-color: {COLORS['bg_secondary']}; border: 1px solid {COLORS['border_color']}; border-radius: 12px; padding: 24px; margin-bottom: 20px;">
        <div style="color: {COLORS['text_primary']}; font-size: 16px; font-weight: 700; margin-bottom: 8px;">📤 Upload City Dataset</div>
        <p style="color: {COLORS['text_secondary']}; font-size: 13px; margin-bottom: 16px; margin-top: 0;">Select a CSV file to begin your analysis</p>
    </div>
    """
    st.markdown(upload_html, unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Upload CSV", type=["csv"], label_visibility="collapsed")
    return uploaded_file


def render_section_heading(section_key):
    """Render section heading"""
    heading = SECTIONS.get(section_key, "")
    st.markdown(f'<div class="section-heading">{heading}</div>', unsafe_allow_html=True)


def render_insight_card(area, value, title, color):
    """Render a single insight card"""
    insight_html = f"""
    <div style="background-color: {COLORS['bg_tertiary']}; border-left: 4px solid {color}; border-radius: 8px; padding: 16px;">
        <div style="color: {color}; font-size: 12px; font-weight: 700; letter-spacing: 1px; text-transform: uppercase; margin-bottom: 8px;">{title}</div>
        <div style="color: {COLORS['text_primary']}; font-size: 16px; font-weight: 600; margin-bottom: 4px;">{area}</div>
        <p style="color: {COLORS['text_secondary']}; font-size: 13px; margin: 0;">Highest {title.lower().split()[-1]} ({value} units)</p>
    </div>
    """
    st.markdown(insight_html, unsafe_allow_html=True)


def render_metrics_row(metrics):
    """Render four metric cards in a row"""
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(
            "Total Areas",
            metrics["total_areas"],
        )
    with col2:
        st.metric("Avg Traffic", f"{metrics['avg_traffic']:.1f}")
    with col3:
        st.metric("Avg Pollution", f"{metrics['avg_pollution']:.1f}")
    with col4:
        st.metric("Avg Energy", f"{metrics['avg_energy']:.1f}")


def render_insights_row(insights):
    """Render three insight cards in a row"""
    col1, col2, col3 = st.columns(3)

    with col1:
        render_insight_card(
            insights["max_traffic"]["Area"],
            insights["max_traffic"]["Traffic"],
            "⚠️ Traffic Hotspot",
            COLORS["warning"],
        )

    with col2:
        render_insight_card(
            insights["max_pollution"]["Area"],
            insights["max_pollution"]["Pollution"],
            "🌍 Air Quality",
            COLORS["danger"],
        )

    with col3:
        render_insight_card(
            insights["max_energy"]["Area"],
            insights["max_energy"]["Energy"],
            "⚡ Energy",
            COLORS["accent_primary"],
        )
