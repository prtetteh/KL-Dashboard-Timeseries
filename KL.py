# Import required libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configure Matplotlib and Seaborn for color
sns.set(style="whitegrid")
plt.rcParams['axes.titlesize'] = 18
plt.rcParams['axes.titleweight'] = 'bold'
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['axes.edgecolor'] = 'black'

# Set up the title with color
st.markdown("<h1 style='color:mediumvioletred; font-size: 36px;'>🌟 Business Dashboard 🌟</h1>", unsafe_allow_html=True)
st.markdown("<p style='color:darkslateblue; font-size: 20px;'>This dashboard provides insights into sales, customer demographics, and product performance.</p>", unsafe_allow_html=True)

# Data Input
# Replace 'your_file.csv' with your actual CSV file path
file_path = '/content/drive/MyDrive/TimeSeriesClass-Fall2024/Streamlit/sales.csv'

# Load data
data = pd.read_csv(file_path)
st.markdown("<p style='color:steelblue; font-size: 18px;'><strong>Preview of the Uploaded Data:</strong></p>", unsafe_allow_html=True)
st.write(data.head())

# Sales Insights
st.markdown("<h2 style='color:darkorange;'>📈 Sales Insights</h2>", unsafe_allow_html=True)
plt.figure(figsize=(10, 6))
plt.plot(data['sales_date'], data['sales_amount'], color="orangered", linewidth=2.5, marker='o', markersize=5)
plt.title('Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Sales Amount')
st.pyplot(plt.gcf())  # Display the figure in Streamlit

# Customer Segmentation by Region
st.markdown("<h2 style='color:teal;'>🌍 Customer Segmentation by Region</h2>", unsafe_allow_html=True)
plt.figure(figsize=(8, 8))
region_sales = data.groupby('region')['sales_amount'].sum()
colors = sns.color_palette("viridis", len(region_sales))
plt.pie(region_sales, labels=region_sales.index, autopct='%1.1f%%', colors=colors, startangle=140, wedgeprops={'edgecolor': 'black'})
plt.title("Customer Segmentation by Region")
st.pyplot(plt.gcf())

# Product Analysis
st.markdown("<h2 style='color:mediumseagreen;'>📊 Product Analysis</h2>", unsafe_allow_html=True)
top_products_df = data.groupby('product')['sales_amount'].sum().nlargest(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=top_products_df.index, y=top_products_df.values, palette="Spectral")
plt.title("Top Products By Sales")
plt.xlabel("Product")
plt.ylabel("Sales Amount")
plt.xticks(rotation=45)
st.pyplot(plt.gcf())

# Footer
st.markdown("<hr style='border-top: 3px solid lightgray;'>", unsafe_allow_html=True)
st.markdown("<p style='color:dimgray; font-size: 16px;'>This business dashboard template is flexible. Expand upon it based on your specific business needs.</p>", unsafe_allow_html=True)
