🛍️ Customer Sales Analysis Dashboard
📘 Overview

This project analyzes customer purchasing patterns and visualizes key business metrics using Python, Pandas, and Matplotlib.
It provides insights such as:

Top customers by total sales

Sales by product category

Monthly sales trends

The dashboard helps identify your best customers and visualize performance over time.

📂 Project Structure
├── sales.csv                  # Dataset file (customer sales records)
├── task5.py          # Main Python script
├── README.md                  # Project documentation

⚙️ Features

🧾 Data Cleaning & Aggregation: Calculates total sales per transaction.

👥 Customer Insights: Identifies top 5 customers by sales.

🏷️ Category Analysis: Summarizes sales by product category.

📅 Trend Visualization: Plots monthly sales performance.

📊 Dashboard View: Displays all key metrics in one visual dashboard.

📦 Requirements

Make sure the following Python libraries are installed:

pip install pandas matplotlib

📈 Dataset Format (sales.csv)

Your dataset should include the following columns:

Column	Description
Customer	Customer name
Category	Product category
Quantity	Quantity purchased
Price	Price per unit
Date	Transaction date (YYYY-MM-DD)
Example:
Customer,Category,Quantity,Price,Date
Alice,Electronics,2,500,2024-01-15
Bob,Clothing,3,250,2024-02-10
Charlie,Groceries,4,100,2024-03-05
David,Electronics,1,800,2024-03-15
Eve,Clothing,2,300,2024-04-01

🧮 How It Works

Load the dataset

df = pd.read_csv('sales.csv')


Compute total sales

df['Total'] = df['Quantity'] * df['Price']


Analyze

Group by Customer → total sales per customer

Group by Category → total sales per category

Convert Date → monthly trends

Visualize with Matplotlib

Bar chart for sales by customer

Horizontal bar for sales by category

Line chart for monthly trends

📊 Dashboard Preview

The script generates a 3-panel dashboard:

Chart	Description
📦 Bar Chart	Total Sales by Customer
🏷️ Horizontal Bar	Sales by Category
📈 Line Plot	Monthly Sales Trend
▶️ How to Run

Clone or download this repository.

Place your sales.csv file in the same directory.

Run:

python sales_analysis.py


A Matplotlib dashboard will appear showing all visualizations.

💡 Future Enhancements

Integrate Plotly Dash for interactive web dashboards.

Add regional or product-level filtering.

Export summary reports in Excel or PDF format.
