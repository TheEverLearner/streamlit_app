import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Title of the dashboard
st.title('Interactive Streamlit Dashboard')

# Sample data creation
np.random.seed(42)
data = pd.DataFrame({
    'category': np.random.choice(['A', 'B', 'C', 'D'], size=100),
    'value': np.random.rand(100) * 100,
    'date': pd.date_range(start='2021-01-01', periods=100)
})

# Sidebar filters
st.sidebar.header('Filters')
selected_category = st.sidebar.multiselect('Select Category', options=data['category'].unique(), default=data['category'].unique())
selected_date_range = st.sidebar.date_input('Select Date Range', [data['date'].min(), data['date'].max()])

# Filter data based on user input
filtered_data = data[
    (data['category'].isin(selected_category)) &
    (data['date'] >= pd.to_datetime(selected_date_range[0])) &
    (data['date'] <= pd.to_datetime(selected_date_range[1]))
]

# Display filtered data
st.write('Filtered Data', filtered_data)

# Plotly interactive chart
fig = px.line(filtered_data, x='date', y='value', color='category', title='Values over Time by Category')
st.plotly_chart(fig)

# Adding more interactive elements
st.header('Additional Visualizations')

# Histogram
st.subheader('Histogram of Values')
hist_values = np.histogram(filtered_data['value'], bins=30, range=(0,100))[0]
st.bar_chart(hist_values)

# Table
st.subheader('Descriptive Statistics')
st.write(filtered_data.describe())
