import sqlite3
import pandas as pd

# Path to your SQLite DB
DB_PATH = r'F:\ecommerce-ai-agent-main\database\ecommerce_data.db'

def run_sql_query(query: str) -> pd.DataFrame:
    try:
        conn = sqlite3.connect(DB_PATH)
        df = pd.read_sql_query(query, conn)
        conn.close()
        return df
    except Exception as e:
        return pd.DataFrame({"error": [str(e)]})
