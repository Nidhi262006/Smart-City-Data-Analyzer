"""
Configuration and theme constants for Smart City Data Analyzer
"""

# Theme Colors
COLORS = {
    "bg_primary": "#0B1120",
    "bg_secondary": "#111827",
    "bg_tertiary": "#151D2E",
    "accent_primary": "#38BDF8",  # Cyan
    "accent_secondary": "#8B5CF6",  # Purple
    "success": "#22C55E",  # Green
    "warning": "#F59E0B",  # Orange
    "danger": "#EF4444",  # Red
    "text_primary": "#FFFFFF",
    "text_secondary": "#A0AEC0",
    "border_color": "#2D3748",
}

# Page Configuration
PAGE_CONFIG = {
    "page_title": "Smart City Data Analyzer",
    "page_icon": "🏙️",
    "layout": "wide",
    "initial_sidebar_state": "collapsed",
}

# Metric Labels
METRIC_LABELS = {
    "total_areas": "Total Areas",
    "avg_traffic": "Avg Traffic",
    "avg_pollution": "Avg Pollution",
    "avg_energy": "Avg Energy",
}

# Chart Dimensions
CHART_DIMS = {
    "small": (8, 5),
    "large": (12, 5),
}

# Section Headings
SECTIONS = {
    "overview": "📊 Dataset Overview",
    "preview": "📋 Dataset Preview",
    "analytics": "📈 Urban Analytics",
    "insights": "💡 Key Insights",
    "correlation": "🔗 Correlation Analysis",
    "statistics": "📐 Dataset Statistics",
    "visualization": "📑 Dataset Visualization",
}

# Insight Labels
INSIGHTS = {
    "traffic": {
        "title": "⚠️ Traffic Hotspot",
        "color": "#F59E0B",
        "metric": "Traffic",
    },
    "pollution": {
        "title": "🌍 Air Quality",
        "color": "#EF4444",
        "metric": "Pollution",
    },
    "energy": {
        "title": "⚡ Energy",
        "color": "#38BDF8",
        "metric": "Energy",
    },
}
