
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "outputs" / "sales_transactions.csv"

OUTPUT_DIR = BASE_DIR / "outputs"
CHART_DIR = OUTPUT_DIR / "charts"

CHART_DIR.mkdir(parents=True, exist_ok=True)

print("=" * 60)
print("       E-COMMERCE EXPLORATORY DATA ANALYSIS")
print("=" * 60)

# Load cleaned sales data
df = pd.read_csv(DATA_FILE, parse_dates=["InvoiceDate"])

# Add month column
df["Month"] = df["InvoiceDate"].dt.to_period("M").astype(str)

# 1. Overall business KPIs
total_revenue = df["Revenue"].sum()
total_orders = df["Invoice"].nunique()
total_customers = df["Customer ID"].nunique()
total_products = df["StockCode"].nunique()
total_countries = df["Country"].nunique()
total_units = df["Quantity"].sum()

print("\n1. OVERALL BUSINESS PERFORMANCE")
print("Total Revenue:", round(total_revenue, 2))
print("Total Orders:", total_orders)
print("Unique Customers:", total_customers)
print("Unique Products:", total_products)
print("Countries:", total_countries)
print("Units Sold:", total_units)

# 2. Monthly sales analysis
monthly_sales = df.groupby("Month").agg(
    Revenue=("Revenue", "sum"),
    Orders=("Invoice", "nunique")
).reset_index()

monthly_sales.to_csv(
    OUTPUT_DIR / "monthly_sales_analysis.csv",
    index=False
)

print("\n2. TOP 5 MONTHS BY REVENUE")
print(
    monthly_sales.nlargest(5, "Revenue").to_string(index=False)
)

# Monthly revenue chart
plt.figure(figsize=(13, 6))
plt.plot(
    monthly_sales["Month"],
    monthly_sales["Revenue"],
    marker="o"
)
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=60)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig(CHART_DIR / "monthly_revenue_trend.png", dpi=150)
plt.close()

# 3. Country sales analysis
country_sales = df.groupby("Country").agg(
    Revenue=("Revenue", "sum"),
    Orders=("Invoice", "nunique"),
    Customers=("Customer ID", "nunique")
).reset_index()

country_sales = country_sales.sort_values(
    "Revenue", ascending=False
)

country_sales.to_csv(
    OUTPUT_DIR / "country_sales_analysis.csv",
    index=False
)

print("\n3. TOP 10 COUNTRIES BY REVENUE")
print(country_sales.head(10).to_string(index=False))

# Country revenue chart
top_countries = country_sales.head(10).sort_values("Revenue")

plt.figure(figsize=(11, 6))
plt.barh(
    top_countries["Country"],
    top_countries["Revenue"]
)
plt.title("Top 10 Countries by Revenue")
plt.xlabel("Revenue")
plt.ylabel("Country")
plt.tight_layout()
plt.savefig(CHART_DIR / "top_10_countries.png", dpi=150)
plt.close()

# 4. Product sales analysis
product_sales = df.groupby(
    ["StockCode", "Description"]
).agg(
    Revenue=("Revenue", "sum"),
    Units_Sold=("Quantity", "sum"),
    Orders=("Invoice", "nunique")
).reset_index()

product_sales = product_sales.sort_values(
    "Revenue", ascending=False
)

product_sales.to_csv(
    OUTPUT_DIR / "product_sales_analysis.csv",
    index=False
)

print("\n4. TOP 10 PRODUCTS BY REVENUE")
print(product_sales.head(10).to_string(index=False))

# Product revenue chart
top_products = product_sales.head(10).sort_values("Revenue")

plt.figure(figsize=(12, 7))
plt.barh(
    top_products["Description"].str.slice(0, 35),
    top_products["Revenue"]
)
plt.title("Top 10 Products by Revenue")
plt.xlabel("Revenue")
plt.ylabel("Product")
plt.tight_layout()
plt.savefig(CHART_DIR / "top_10_products.png", dpi=150)
plt.close()

# 5. Customer analysis
customer_sales = df.dropna(
    subset=["Customer ID"]
).groupby("Customer ID").agg(
    Revenue=("Revenue", "sum"),
    Orders=("Invoice", "nunique"),
    Units_Purchased=("Quantity", "sum")
).reset_index()

customer_sales = customer_sales.sort_values(
    "Revenue", ascending=False
)

customer_sales.to_csv(
    OUTPUT_DIR / "customer_sales_analysis.csv",
    index=False
)

print("\n5. TOP 10 CUSTOMERS BY REVENUE")
print(customer_sales.head(10).to_string(index=False))

# 6. Save KPI summary
kpi_summary = pd.DataFrame({
    "Metric": [
        "Total Revenue",
        "Total Orders",
        "Unique Customers",
        "Unique Products",
        "Countries",
        "Units Sold"
    ],
    "Value": [
        round(total_revenue, 2),
        total_orders,
        total_customers,
        total_products,
        total_countries,
        total_units
    ]
})

kpi_summary.to_csv(
    OUTPUT_DIR / "business_kpi_summary.csv",
    index=False
)

print("\n" + "=" * 60)
print("EDA COMPLETED SUCCESSFULLY!")
print("Analysis files saved in outputs folder.")
print("Charts saved in outputs/charts folder.")
print("=" * 60)
