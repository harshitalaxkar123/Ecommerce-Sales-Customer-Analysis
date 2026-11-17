
import pandas as pd
from pathlib import Path
from getpass import getpass
from sqlalchemy import create_engine, types, text
from sqlalchemy.engine import URL

# Project paths
BASE_DIR = Path(__file__).resolve().parents[1]
DATA_FILE = BASE_DIR / "outputs" / "sales_transactions.csv"

# Database configuration
password = getpass("Enter MySQL root password: ")

connection_url = URL.create(
    drivername="mysql+pymysql",
    username="root",
    password=password,
    host="127.0.0.1",
    port=3306,
    database="ecommerce_analysis"
)

engine = create_engine(connection_url, pool_pre_ping=True)

# SQL column data types
sql_types = {
    "Invoice": types.VARCHAR(20),
    "StockCode": types.VARCHAR(20),
    "Description": types.TEXT(),
    "Quantity": types.INTEGER(),
    "InvoiceDate": types.DateTime(),
    "Price": types.DECIMAL(12, 4),
    "CustomerID": types.BIGINT(),
    "Country": types.VARCHAR(100),
    "IsCancelled": types.Boolean(),
    "IsReturn": types.Boolean(),
    "HasNegativePrice": types.Boolean(),
    "IsValidSale": types.Boolean(),
    "Revenue": types.DECIMAL(14, 4)
}

def main():

    if not DATA_FILE.exists():
        raise FileNotFoundError(f"CSV file not found: {DATA_FILE}")

    total_rows = 0
    chunk_number = 0

    print("Starting CSV import into MySQL...")

    chunks = pd.read_csv(
        DATA_FILE,
        chunksize=10000,
        dtype={"Invoice": str, "StockCode": str},
        parse_dates=["InvoiceDate"],
        low_memory=False
    )

    for df in chunks:

        chunk_number += 1

        # Rename column for SQL compatibility
        df.rename(
            columns={"Customer ID": "CustomerID"},
            inplace=True
        )

        # Convert customer IDs to nullable integers
        df["CustomerID"] = (
            pd.to_numeric(df["CustomerID"], errors="coerce")
            .round()
            .astype("Int64")
        )

        # Convert numeric columns
        df["Quantity"] = pd.to_numeric(df["Quantity"])
        df["Price"] = pd.to_numeric(df["Price"])
        df["Revenue"] = pd.to_numeric(df["Revenue"])

        # Convert boolean columns
        bool_columns = [
            "IsCancelled",
            "IsReturn",
            "HasNegativePrice",
            "IsValidSale"
        ]

        for col in bool_columns:
            df[col] = df[col].astype("boolean")

        # Insert records into MySQL
        df.to_sql(
            name="sales_transactions",
            con=engine,
            if_exists="replace" if chunk_number == 1 else "append",
            index=False,
            dtype=sql_types,
            chunksize=1000
        )

        total_rows += len(df)

        print(f"Chunk {chunk_number} imported | Total rows: {total_rows:,}")

    # Verify imported records
    with engine.connect() as connection:
        count = connection.execute(
            text("SELECT COUNT(*) FROM sales_transactions")
        ).scalar_one()

    print("\nImport completed successfully!")
    print(f"Total imported records: {count:,}")

    engine.dispose()


if __name__ == "__main__":
    main()
