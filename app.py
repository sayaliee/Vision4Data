# Streamlit app code for visualizing Installs variations with Plotly
import streamlit as st
import pandas as pd
import plotly.express as px


# Load data
df = pd.read_csv("Cleanedhack2.csv")  # Replace with the actual path if running locally

# Title and description
st.title("PlayStore Analysis Dashboard")
st.markdown("Explore the variation of Installs with other columns in the dataset.")

# Sidebar for column selection
categorical_cols = ['App', 'Category', 'Genres', 'Content Rating']
numerical_cols = ['Rating', 'Reviews', 'Size', 'Price']

all_columns = categorical_cols + numerical_cols
selected_column = st.sidebar.selectbox("Select a column to compare with Installs:", all_columns)

# Plotting
if selected_column:
    if selected_column in categorical_cols:
        # Bar chart for categorical columns
        fig = px.bar(df, x=selected_column, y="Installs", title=f"Installs variation by {selected_column}")
    else:
        # Scatter plot for numerical columns
        fig = px.scatter(df, x=selected_column, y="Installs", trendline="ols",
                         title=f"Installs vs {selected_column}")

    st.plotly_chart(fig)


