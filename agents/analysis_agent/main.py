from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/analyze/aum")
def analyze():
    yesterday = 18.0
    today = 22.0
    change_pct = ((today - yesterday) / yesterday) * 100
    return {"aum_yesterday": yesterday, "aum_today": today, "change_pct": change_pct}