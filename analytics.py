"""
Data analysis and calculations for Smart City Data Analyzer
"""

import pandas as pd


def load_data(uploaded_file):
    """Load CSV data from uploaded file"""
    return pd.read_csv(uploaded_file)


def calculate_metrics(data):
    """Calculate key metrics from dataset"""
    return {
        "total_areas": len(data),
        "avg_traffic": data["Traffic"].mean(),
        "avg_pollution": data["Pollution"].mean(),
        "avg_energy": data["Energy"].mean(),
    }


def get_key_insights(data):
    """Calculate key insights from dataset"""
    return {
        "max_traffic": data.loc[data["Traffic"].idxmax()],
        "max_pollution": data.loc[data["Pollution"].idxmax()],
        "max_energy": data.loc[data["Energy"].idxmax()],
    }


def get_correlation_matrix(data):
    """Calculate correlation matrix for numeric columns"""
    return data.corr(numeric_only=True)


def get_statistics(data):
    """Calculate descriptive statistics"""
    return data.describe()
