
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
OUTPUT_DIR = BASE_DIR / "outputs"
CHART_DIR = OUTPUT_DIR / "final_charts"
CHART_DIR.mkdir(parents=True, exist_ok=True)

# Load SQL analysis outputs
monthly = pd.read_csv(OUTPUT_DIR / "monthly_sales_sql.csv")
country = pd.read_csv(OUTPUT_DIR / "country_sales_sql.csv")
products = pd.read_csv(OUTPUT_DIR / "product_sales_sql.csv")
customers = pd.read_csv(OUTPUT_DIR / "customer_sales_sql.csv")

# 1. Monthly Revenue Trend
monthly = monthly.sort_values("Sales_Month")
plt.figure(figsize=(12, 5))
plt.plot(monthly["Sales_Month"], monthly["Total_Revenue"], marker="o")
plt.title("Monthly Sales Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(CHART_DIR / "monthly_revenue.png", dpi=150)
plt.close()

# 2. Top 10 Countries
top_countries = country.nlargest(10, "Total_Revenue").sort_values("Total_Revenue")
plt.figure(figsize=(10, 6))
plt.barh(top_countries["Country"], top_countries["Total_Revenue"])
plt.title("Top 10 Countries by Revenue")
plt.xlabel("Revenue")
plt.tight_layout()
plt.savefig(CHART_DIR / "top_countries.png", dpi=150)
plt.close()

# 3. Top 10 Products
top_products = products.nlargest(10, "Total_Revenue").sort_values("Total_Revenue")
plt.figure(figsize=(10, 6))
plt.barh(top_products["Description"].astype(str), top_products["Total_Revenue"])
plt.title("Top 10 Products by Revenue")
plt.xlabel("Revenue")
plt.tight_layout()
plt.savefig(CHART_DIR / "top_products.png", dpi=150)
plt.close()

# 4. Top 10 Customers
top_customers = customers.nlargest(10, "Total_Spending").sort_values("Total_Spending")
plt.figure(figsize=(10, 6))
plt.barh(top_customers["CustomerID"].astype(str), top_customers["Total_Spending"])
plt.title("Top 10 Customers by Spending")
plt.xlabel("Revenue")
plt.tight_layout()
plt.savefig(CHART_DIR / "top_customers.png", dpi=150)
plt.close()

print("All 4 dashboard charts created successfully!")
print(f"Saved in: {CHART_DIR}")

print("All 4 dashboard charts created successfully!")
print(f"Saved in: {CHART_DIR}")
print("Charts:", list(CHART_DIR.glob("*.png")))