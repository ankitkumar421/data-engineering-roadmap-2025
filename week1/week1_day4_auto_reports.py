import pandas as pd
from sqlalchemy import create_engine
import os

# -------------------------------
# 1. Connect to database
# -------------------------------
engine = create_engine("sqlite:///sales_db.sqlite")
print("✅ Connected to SQLite")

# -------------------------------
# 2. Define SQL queries
# -------------------------------
queries = {
    "total_revenue": """
        SELECT SUM(revenue) AS total_revenue
        FROM sales;
    """,
    "top_customers": """
        SELECT customer_id, SUM(revenue) AS total_revenue
        FROM sales
        GROUP BY customer_id
        ORDER BY total_revenue DESC
        LIMIT 5;
    """,
    "monthly_revenue": """
        SELECT order_month, SUM(revenue) AS monthly_revenue
        FROM sales
        GROUP BY order_month
        ORDER BY order_month;
    """
}

# -------------------------------
# 3. Run queries & save results
# -------------------------------
os.makedirs("reports", exist_ok=True)

for name, query in queries.items():
    df = pd.read_sql(query, engine)
    
    # Save to CSV
    csv_path = f"reports/{name}.csv"
    df.to_csv(csv_path, index=False)
    
    # Save to Excel
    excel_path = f"reports/{name}.xlsx"
    df.to_excel(excel_path, index=False)
    
    print(f"✅ Saved {name} report -> {csv_path}, {excel_path}")
