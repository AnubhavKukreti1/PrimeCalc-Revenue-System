import os
from pathlib import Path

import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

# --------------------------------------------------
# 1. PROJECT CONFIGURATION
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data" / "raw"

load_dotenv(PROJECT_ROOT / ".env")

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "revenuex")
DB_USER = os.getenv("DB_USER", "anubhavkukreti")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")

# Local PostgreSQL socket connection.
# This avoids requiring TCP password authentication.
if DB_PASSWORD:
    DB_URL = (
        f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}"
        f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
else:
    DB_URL = (
        f"postgresql+psycopg2://{DB_USER}@/{DB_NAME}"
    )

engine = create_engine(DB_URL)

# --------------------------------------------------
# 2. DATASET CONFIGURATION
# --------------------------------------------------

CSV_FILES = {
    "customers": "olist_customers_dataset.csv",
    "geolocation": "olist_geolocation_dataset.csv",
    "order_items": "olist_order_items_dataset.csv",
    "order_payments": "olist_order_payments_dataset.csv",
    "order_reviews": "olist_order_reviews_dataset.csv",
    "orders": "olist_orders_dataset.csv",
    "products": "olist_products_dataset.csv",
    "sellers": "olist_sellers_dataset.csv",
    "category_translation": "product_category_name_translation.csv",
}

# --------------------------------------------------
# 3. VERIFY DATABASE CONNECTION
# --------------------------------------------------

with engine.connect() as connection:
    result = connection.execute(
        text("SELECT current_database()")
    ).scalar()

    print(f"Connected to database: {result}")

# --------------------------------------------------
# 4. IMPORT CSV FILES
# --------------------------------------------------

ingestion_results = []

for table_name, filename in CSV_FILES.items():

    file_path = DATA_DIR / filename

    print("\n" + "=" * 55)
    print(f"Processing: {filename}")

    try:

        if not file_path.exists():
            raise FileNotFoundError(
                f"File not found: {file_path}"
            )

        df = pd.read_csv(file_path)

        source_rows = len(df)

        # Import original CSV columns and values.
        df.to_sql(
            name=table_name,
            con=engine,
            schema="raw",
            if_exists="fail",
            index=False,
            chunksize=5000,
            method="multi"
        )

        ingestion_results.append({
            "table_name": table_name,
            "filename": filename,
            "source_rows": source_rows,
            "status": "SUCCESS",
            "error": None
        })

        print(f"Rows imported: {source_rows}")
        print("Status: SUCCESS")

    except Exception as error:

        ingestion_results.append({
            "table_name": table_name,
            "filename": filename,
            "source_rows": None,
            "status": "FAILED",
            "error": str(error)
        })

        print(f"Status: FAILED")
        print(f"Error: {error}")

# --------------------------------------------------
# 5. SAVE INGESTION REPORT
# --------------------------------------------------

report_df = pd.DataFrame(ingestion_results)

REPORT_DIR = PROJECT_ROOT / "reports"
REPORT_DIR.mkdir(exist_ok=True)

report_path = REPORT_DIR / "ingestion_report.csv"

report_df.to_csv(report_path, index=False)

print("\n" + "=" * 55)
print("INGESTION SUMMARY")
print("=" * 55)

print(report_df.to_string(index=False))

print(f"\nReport saved at: {report_path}")

engine.dispose()
