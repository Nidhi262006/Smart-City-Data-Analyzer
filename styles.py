"""
CSS Styling for Smart City Data Analyzer dashboard
"""

from config import COLORS


def get_custom_css():
    """Generate custom CSS for the dashboard theme"""
    return f"""
    <style>
        /* Main theme colors */
        :root {{
            --bg-primary: {COLORS['bg_primary']};
            --bg-secondary: {COLORS['bg_secondary']};
            --bg-tertiary: {COLORS['bg_tertiary']};
            --accent-primary: {COLORS['accent_primary']};
            --accent-secondary: {COLORS['accent_secondary']};
            --success: {COLORS['success']};
            --warning: {COLORS['warning']};
            --danger: {COLORS['danger']};
            --text-primary: {COLORS['text_primary']};
            --text-secondary: {COLORS['text_secondary']};
            --border-color: {COLORS['border_color']};
        }}
        
        /* Main container */
        .main {{
            background-color: {COLORS['bg_primary']};
            color: {COLORS['text_primary']};
        }}
        
        /* Sidebar styling */
        [data-testid="stSidebar"] {{
            background-color: {COLORS['bg_secondary']};
        }}
        
        /* Hide default Streamlit elements */
        #MainMenu {{
            visibility: hidden;
        }}
        
        footer {{
            visibility: hidden;
        }}
        
        .viewerBadge_container__r5tak {{
            visibility: hidden;
        }}
        
        /* Header styling */
        .dashboard-header {{
            background-color: {COLORS['bg_secondary']};
            border: 1px solid {COLORS['border_color']};
            border-radius: 12px;
            padding: 24px;
            margin-bottom: 24px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
        }}
        
        /* Section heading */
        .section-heading {{
            color: {COLORS['text_primary']};
            font-size: 20px;
            font-weight: 700;
            margin-top: 24px;
            margin-bottom: 12px;
            padding-bottom: 8px;
            border-bottom: 2px solid {COLORS['border_color']};
        }}
        
        /* Metric components */
        [data-testid="metric-container"] {{
            background-color: {COLORS['bg_tertiary']};
            border: 1px solid {COLORS['border_color']};
            border-radius: 12px;
            padding: 16px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }}
        
        [data-testid="metric-container"] > div:first-child {{
            color: {COLORS['text_secondary']};
            font-size: 12px;
            font-weight: 600;
            letter-spacing: 1px;
            text-transform: uppercase;
        }}
        
        [data-testid="metric-container"] > div:nth-child(2) {{
            color: {COLORS['accent_primary']};
            font-size: 28px;
            font-weight: 700;
        }}
        
        /* Dataframe styling */
        [data-testid="stDataframe"] {{
            background-color: {COLORS['bg_secondary']} !important;
        }}
        
        .stDataFrame {{
            background-color: {COLORS['bg_secondary']};
        }}
        
        /* Container styling */
        [data-testid="stContainer"] {{
            background-color: transparent;
        }}
        
        /* Heading styling */
        h3 {{
            color: {COLORS['text_primary']};
            font-size: 16px;
            font-weight: 600;
            margin-bottom: 8px;
        }}
        
        /* Upload section styling */
        .upload-section {{
            background-color: {COLORS['bg_secondary']};
            border: 1px solid {COLORS['border_color']};
            border-radius: 12px;
            padding: 24px;
            margin-bottom: 20px;
        }}
    </style>
    """
