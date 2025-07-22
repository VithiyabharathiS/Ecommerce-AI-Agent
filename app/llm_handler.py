import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get the API key securely
api_key = os.getenv("GEMINI_API_KEY")

# Configure the Gemini API
genai.configure(api_key=api_key)

# Set the model
model = genai.GenerativeModel(model_name="models/gemini-2.5-pro")

# Prompt with schema info
PROMPT_TEMPLATE = """
You are an expert data analyst working with a SQLite database.

Use ONLY the following tables and columns:

1. product_total_sales_metrics:
   - date
   - item_id
   - total_sales
   - total_units_ordered

2. product_ad_sales_metrics:
   - date
   - item_id
   - ad_sales
   - impressions
   - ad_spend
   - clicks
   - units_sold

3. product_eligibility:
   - eligibility_datetime_utc
   - item_id
   - eligibility
   - message

The column `item_id` is the common key to JOIN the tables.

Write SQLite-compatible SQL.
ONLY return the SQL query (no explanation or markdown).

Convert the following question into SQL:

Question: "{question}"
"""

def query_llm_to_sql(question: str) -> str:
    prompt = PROMPT_TEMPLATE.format(question=question)
    try:
        response = model.generate_content(prompt)
        sql_code = response.text.strip()
        if sql_code.startswith("```sql"):
            sql_code = sql_code.replace("```sql", "").replace("```", "").strip()
        return sql_code
    except Exception as e:
        print("Gemini API Error:", e)
        return "Error generating SQL"
