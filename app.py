import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Smart City Data Analyzer")

# Upload dataset
uploaded_file = st.file_uploader("Upload City Dataset", type=["csv"])

if uploaded_file is not None:
    
    data = pd.read_csv(uploaded_file)
    
    st.write("Dataset Preview")
    st.write(data.head())

    st.write("Basic Statistics")
    st.write(data.describe())

    # Traffic chart
    st.subheader("Traffic Analysis")
    plt.figure()
    plt.bar(data["Area"], data["Traffic"])
    plt.title("Traffic by Area")
    st.pyplot(plt)

    # Pollution chart
    st.subheader("Pollution Levels")
    plt.figure()
    plt.bar(data["Area"], data["Pollution"])
    plt.title("Pollution by Area")
    st.pyplot(plt)

    # Energy chart
    st.subheader("Energy Consumption")
    plt.figure()
    plt.plot(data["Area"], data["Energy"])
    plt.title("Energy Usage")
    st.pyplot(plt)

    st.subheader("Key Insights")

    max_traffic = data.loc[data["Traffic"].idxmax()]
    max_pollution = data.loc[data["Pollution"].idxmax()]
    max_energy = data.loc[data["Energy"].idxmax()]

    st.write("Area with highest traffic:", max_traffic["Area"])
    st.write("Area with highest pollution:", max_pollution["Area"])
    st.write("Area with highest energy consumption:", max_energy["Area"])

    st.subheader("Correlation Analysis")

    correlation = data.corr(numeric_only=True)
    st.write(correlation)

    st.subheader("Dataset Visualization")
    st.dataframe(data)