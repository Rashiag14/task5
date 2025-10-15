import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('sales.csv')

# Compute total sales per transaction
df['Total'] = df['Quantity'] * df['Price']

#ANALYSIS
# 1. Total sales by customer
sales_by_customer = df.groupby('Customer')['Total'].sum().sort_values(ascending=False)

# 2. Total sales by category
sales_by_category = df.groupby('Category')['Total'].sum().sort_values(ascending=False)

# 3. Monthly sales trend
df['Date'] = pd.to_datetime(df['Date'])
sales_by_month = df.groupby(df['Date'].dt.to_period('M'))['Total'].sum()

# 4. Top 5 customers
top_customers = sales_by_customer.head(5)
print(top_customers)


plt.style.use('seaborn-v0_8')
plt.figure(figsize=(14, 8))

# -----------------------------
# Plot 1: Sales by Customer
# -----------------------------
plt.subplot(2, 2, 1)
sales_by_customer.plot(kind='bar', color='teal', edgecolor='black')
plt.title('Total Sales by Customer')
plt.ylabel('Sales Amount')
plt.xticks(rotation=45)

# -----------------------------
# Plot 2: Sales by Category
# -----------------------------
plt.subplot(2, 2, 2)
sales_by_category.plot(kind='barh', color='orange', edgecolor='black')
plt.title('Sales by Category')
plt.xlabel('Sales Amount')

# -----------------------------
# Plot 3: Monthly Sales Trend
# -----------------------------
plt.subplot(2, 1, 2)
sales_by_month.plot(marker='o', color='purple')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.grid(True, linestyle='--', alpha=0.6)

# -----------------------------
# Show dashboard
# -----------------------------
plt.tight_layout()
plt.show()

