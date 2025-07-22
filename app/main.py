from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from app.llm_handler import query_llm_to_sql
from app.db_handler import run_sql_query
from app.chart_handler import generate_cpc_chart
import pandas as pd
import os

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


@app.get("/")
def read_index():
    return FileResponse("app/static/index.html")


class QueryRequest(BaseModel):
    question: str


@app.post("/ask")
async def ask_question(request: QueryRequest):
    question = request.question

    # Step 1: Convert question to SQL
    sql_query = query_llm_to_sql(question)

    # Step 2: Run SQL query
    result_df = run_sql_query(sql_query)

    # Step 3: Prepare output JSON
    result_json = result_df.to_dict(orient="records")

    # Step 4: Optional - show top 5 CPC chart for specific queries
    chart_base64 = None
    if "cost per click" in question.lower() or "cpc" in question.lower():
        try:
            # Create CPC column if data available
            if 'ad_spend' in result_df.columns and 'clicks' in result_df.columns:
                result_df['cpc'] = result_df['ad_spend'] / result_df['clicks']
                top5_df = result_df[result_df['clicks'] > 0].sort_values(by='cpc', ascending=False).head(5)
                chart_base64 = generate_cpc_chart(top5_df)
        except Exception as e:
            print("Chart generation failed:", e)

    return {
        "question": question,
        "sql": sql_query,
        "result": result_json,
        "chart": chart_base64  # base64 encoded image
    }
