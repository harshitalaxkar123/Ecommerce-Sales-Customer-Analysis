
import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL
from getpass import getpass

BASE_DIR = Path(__file__).resolve().parents[1]
OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

password = getpass("Enter MySQL root password: ")

url = URL.create(
    "mysql+pymysql",
    username="root",
    password=password,
    host="127.0.0.1",
    port=3306,
    database="ecommerce_analysis"
)

engine = create_engine(url, pool_pre_ping=True)

views = {
    "monthly_sales_view": "monthly_sales_sql.csv",
    "country_sales_view": "country_sales_sql.csv",
    "product_sales_view": "product_sales_sql.csv",
    "customer_sales_view": "customer_sales_sql.csv"
}

try:
    with engine.connect() as connection:
        for view, filename in views.items():
            df = pd.read_sql(
                text(f"SELECT * FROM {view}"),
                connection
            )

            output_file = OUTPUT_DIR / filename
            df.to_csv(output_file, index=False)

            print(f"{view}: {len(df):,} rows exported")

    print("\nSQL and Python integration successful!")

finally:
    engine.dispose()
