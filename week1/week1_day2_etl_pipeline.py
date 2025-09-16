import os
import pandas as pd
from sqlalchemy import create_engine

# ------------------------------
# 1. Extract
# ------------------------------
print("🔹 Extracting data...")

# Load raw CSV
df = pd.read_csv("data/sales.csv", parse_dates=["order_date"])
print(f"Loaded {df.shape[0]} rows")

# ------------------------------
# 2. Transform
# ------------------------------
print("🔹 Transforming data...")

# Remove duplicates
df = df.drop_duplicates()

# Fix types
df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce').fillna(0).astype(int)
df['unit_price'] = pd.to_numeric(df['unit_price'], errors='coerce').fillna(0.0)
df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')

# Add revenue & order_month
df['revenue'] = df['quantity'] * df['unit_price']
df['order_month'] = df['order_date'].dt.to_period('M').astype(str)

print("✅ Transformation done")

# ------------------------------
# 3. Load
# ------------------------------
print("🔹 Loading data into SQLite...")

# Create SQLite database (file will be created in project folder)
os.makedirs("week1", exist_ok=True)
engine = create_engine("sqlite:///week1/sales_db.sqlite", echo=False)
print("Rows before load:", df.shape[0])
# Save the dataframe into a table
df.to_sql("sales", engine, if_exists="replace", index=False)

print("✅ Data loaded into week1/sales_db.sqlite (table: sales)")
