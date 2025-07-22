import matplotlib.pyplot as plt
import pandas as pd
import io
import base64

def generate_cpc_chart(df: pd.DataFrame) -> str:
    plt.figure(figsize=(8, 4))
    plt.bar(df['item_id'].astype(str), df['cpc'], color='skyblue')
    plt.xlabel("Item ID")
    plt.ylabel("Cost Per Click")
    plt.title("Top 5 Products by CPC")
    plt.tight_layout()

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    chart_base64 = base64.b64encode(buf.read()).decode('utf-8')
    plt.close()

    return chart_base64
