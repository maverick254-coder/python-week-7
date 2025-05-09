
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("Nike Dataset.csv")

# Clean dataset
df_cleaned = df.dropna()

# Basic statistics
print("\nBasic Statistics:")
print(df_cleaned.describe())

# Group by Product and compute average Total Sales
avg_sales_per_product = df_cleaned.groupby('Product')['Total Sales'].mean()
print("\nAverage Sales per Product:")
print(avg_sales_per_product)

# Convert Invoice Date to datetime
df_cleaned['Invoice Date'] = pd.to_datetime(df_cleaned['Invoice Date'], dayfirst=True)
df_sorted = df_cleaned.sort_values('Invoice Date')
daily_sales = df_sorted.groupby('Invoice Date')['Total Sales'].sum()

# 1. Line chart - Sales over time
plt.figure(figsize=(10, 5))
plt.plot(daily_sales.index, daily_sales.values, color='blue')
plt.title('Total Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Bar chart - Average Sales per Product
plt.figure(figsize=(10, 6))
avg_sales_per_product.sort_values().plot(kind='barh', color='green')
plt.title('Average Total Sales per Product')
plt.xlabel('Average Sales')
plt.ylabel('Product')
plt.tight_layout()
plt.show()

# 3. Histogram - Units Sold Distribution
plt.figure(figsize=(8, 5))
plt.hist(df_cleaned['Units Sold'], bins=20, color='orange', edgecolor='black')
plt.title('Distribution of Units Sold')
plt.xlabel('Units Sold')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# 4. Scatter plot - Units Sold vs Total Sales
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df_cleaned, x='Units Sold', y='Total Sales', hue='Product')
plt.title('Units Sold vs. Total Sales')
plt.xlabel('Units Sold')
plt.ylabel('Total Sales')
plt.legend(title='Product', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
