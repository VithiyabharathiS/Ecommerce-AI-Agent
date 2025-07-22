import pandas as pd
import sqlite3
import os

# File paths (update all 3 accordingly)
ad_sales_file = r'D:\ecommerce-ai-agent\data\Product-Level Ad Sales and Metrics.csv'
total_sales_file = r'D:\ecommerce-ai-agent\data\Product-Level Total Sales and Metrics.csv'
eligibility_file = r'D:\ecommerce-ai-agent\data\Product-Level Eligibility Table.csv'

# SQLite database file
db_path = r'D:\ecommerce-ai-agent\ecommerce_data.db'

# Connect to SQLite
conn = sqlite3.connect(db_path)

# Load and save each dataset into separate tables
ad_sales_df = pd.read_csv(ad_sales_file)
ad_sales_df.to_sql('product_ad_sales_metrics', conn, if_exists='replace', index=False)

total_sales_df = pd.read_csv(total_sales_file)
total_sales_df.to_sql('product_total_sales_metrics', conn, if_exists='replace', index=False)

eligibility_df = pd.read_csv(eligibility_file)
eligibility_df.to_sql('product_eligibility', conn, if_exists='replace', index=False)

# Print confirmation and show available tables
print("Tables successfully created in SQLite database!")
tables = pd.read_sql("SELECT name FROM sqlite_master WHERE type='table';", conn)
print(tables)

# Close connection
conn.close()
