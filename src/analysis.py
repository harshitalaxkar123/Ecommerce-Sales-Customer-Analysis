
import pandas as pd
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "online_retail_combined.csv"
OUTPUT_DIR = BASE_DIR / "outputs"

OUTPUT_DIR.mkdir(exist_ok=True)

print("=" * 60)
print("          E-COMMERCE DATA CLEANING")
print("=" * 60)

# Load original combined dataset
df = pd.read_csv(
    DATA_FILE,
    dtype={"Invoice": str, "StockCode": str}
)

print("\nOriginal records:", len(df))

# STEP 1: Remove exact duplicate records
before = len(df)
df = df.drop_duplicates().copy()
print("\nDuplicates removed:", before - len(df))

# STEP 2: Standardize text columns
df["Description"] = df["Description"].fillna("Unknown Product")
df["Country"] = df["Country"].str.strip()
df["StockCode"] = df["StockCode"].str.strip()

# STEP 3: Convert data types
df["InvoiceDate"] = pd.to_datetime(
    df["InvoiceDate"],
    errors="coerce"
)

df["Customer ID"] = pd.to_numeric(
    df["Customer ID"],
    errors="coerce"
)

# STEP 4: Create business flags
df["IsCancelled"] = df["Invoice"].str.startswith(
    "C", na=False
)

df["IsReturn"] = (
    (df["Quantity"] < 0) & (~df["IsCancelled"])
)

df["HasNegativePrice"] = df["Price"] < 0

df["IsValidSale"] = (
    (~df["IsCancelled"]) &
    (df["Quantity"] > 0) &
    (df["Price"] > 0)
)

# STEP 5: Calculate transaction value
df["Revenue"] = df["Quantity"] * df["Price"]

# STEP 6: Create separate business datasets
sales_df = df[df["IsValidSale"]].copy()

returns_df = df[df["IsReturn"]].copy()

cancelled_df = df[df["IsCancelled"]].copy()

customer_df = sales_df[
    sales_df["Customer ID"].notna()
].copy()

# STEP 7: Save cleaned datasets
df.to_csv(
    OUTPUT_DIR / "cleaned_online_retail.csv",
    index=False
)

sales_df.to_csv(
    OUTPUT_DIR / "sales_transactions.csv",
    index=False
)

returns_df.to_csv(
    OUTPUT_DIR / "returns_transactions.csv",
    index=False
)

cancelled_df.to_csv(
    OUTPUT_DIR / "cancelled_transactions.csv",
    index=False
)

customer_df.to_csv(
    OUTPUT_DIR / "customer_transactions.csv",
    index=False
)

# STEP 8: Print cleaning summary
print("\n" + "=" * 60)
print("             CLEANING SUMMARY")
print("=" * 60)

print("Records after duplicate removal:", len(df))
print("Valid sales records:", len(sales_df))
print("Return records:", len(returns_df))
print("Cancelled invoice records:", len(cancelled_df))
print("Records with negative price:", df["HasNegativePrice"].sum())
print("Sales records with Customer ID:", len(customer_df))

print("\nTotal valid sales revenue:",
      round(sales_df["Revenue"].sum(), 2))

print("\nMissing Customer IDs retained in master dataset:",
      df["Customer ID"].isna().sum())

print("\nAll cleaned datasets saved in outputs folder.")

print("\nDATA CLEANING COMPLETED!")


