
import pandas as pd
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "outputs" / "sales_transactions.csv"
OUTPUT_DIR = BASE_DIR / "outputs"

print("=" * 60)
print("             CUSTOMER RFM ANALYSIS")
print("=" * 60)

# Load sales data
df = pd.read_csv(
    DATA_FILE,
    dtype={"Invoice": str, "StockCode": str},
    parse_dates=["InvoiceDate"],
    low_memory=False
)

# Calculate reference date
snapshot_date = df["InvoiceDate"].max() + pd.Timedelta(days=1)

# Calculate RFM metrics
rfm = df.groupby("Customer ID").agg(
    Recency=("InvoiceDate", lambda x: (snapshot_date - x.max()).days),
    Frequency=("Invoice", "nunique"),
    Monetary=("Revenue", "sum")
).reset_index()

# Create RFM scores
rfm["R_Score"] = pd.qcut(
    rfm["Recency"].rank(method="first"),
    4,
    labels=[4, 3, 2, 1]
).astype(int)

rfm["F_Score"] = pd.qcut(
    rfm["Frequency"].rank(method="first"),
    4,
    labels=[1, 2, 3, 4]
).astype(int)

rfm["M_Score"] = pd.qcut(
    rfm["Monetary"].rank(method="first"),
    4,
    labels=[1, 2, 3, 4]
).astype(int)

# Combined RFM score
rfm["RFM_Score"] = (
    rfm["R_Score"].astype(str) +
    rfm["F_Score"].astype(str) +
    rfm["M_Score"].astype(str)
)

# Customer segmentation
def segment_customer(row):
    if row["RFM_Score"] == "444":
        return "Best Customers"
    elif row["R_Score"] >= 3 and row["F_Score"] >= 3:
        return "Loyal Customers"
    elif row["R_Score"] >= 3:
        return "Recent Customers"
    elif row["R_Score"] <= 2 and row["F_Score"] >= 3:
        return "At Risk Customers"
    else:
        return "Others"

rfm["Segment"] = rfm.apply(segment_customer, axis=1)

# Save RFM results
rfm.to_csv(
    OUTPUT_DIR / "customer_rfm_analysis.csv",
    index=False
)

# Segment summary
segment_summary = rfm.groupby("Segment").agg(
    Customers=("Customer ID", "count"),
    Revenue=("Monetary", "sum")
).reset_index()

segment_summary.to_csv(
    OUTPUT_DIR / "customer_segments_summary.csv",
    index=False
)

print("\nRFM SUMMARY")
print(rfm.head(10).to_string(index=False))

print("\nCUSTOMER SEGMENTS")
print(segment_summary.to_string(index=False))

print("\nRFM analysis saved successfully!")
