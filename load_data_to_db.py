import pandas as pd
import sqlite3
import os

# Step 1: Define CSV paths
base_path = r'F:\ecommerce-ai-agent-main\data'
ad_sales_file = os.path.join(base_path, 'Product-Level Ad Sales and Metrics.csv')
total_sales_file = os.path.join(base_path, 'Product-Level Total Sales and Metrics.csv')
eligibility_file = os.path.join(base_path, 'Product-Level Eligibility Table.csv')

# Step 2: Define database path in the 'database' folder
db_path = r'F:\ecommerce-ai-agent-main\database\ecommerce_data.db'

# Step 3: Connect and load data
conn = sqlite3.connect(db_path)

# Create tables
pd.read_csv(ad_sales_file).to_sql('product_ad_sales_metrics', conn, if_exists='replace', index=False)
pd.read_csv(total_sales_file).to_sql('product_total_sales_metrics', conn, if_exists='replace', index=False)
pd.read_csv(eligibility_file).to_sql('product_eligibility', conn, if_exists='replace', index=False)

print("✅ Tables successfully created in ecommerce_data.db!")

# Optional: show tables
tables = pd.read_sql("SELECT name FROM sqlite_master WHERE type='table';", conn)
print(tables)

conn.close()
