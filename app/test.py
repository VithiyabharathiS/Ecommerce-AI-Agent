import sqlite3

conn = sqlite3.connect("D:/ecommerce-ai-agent/ecommerce_data.db")

tables = conn.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
print("Tables:", tables)

for table_name, in tables:
    print(f"\nSchema for {table_name}:")
    for row in conn.execute(f"PRAGMA table_info({table_name});"):
        print(row)

conn.close()
