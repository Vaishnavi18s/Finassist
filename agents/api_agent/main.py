# agents/api_agent/main.py
from fastapi import FastAPI
from pydantic import BaseModel
import yfinance as yf

app = FastAPI()

class StockRequest(BaseModel):
    symbol: str

@app.post("/api/fetch_data")
def fetch_data(request: StockRequest):
    stock = yf.Ticker(request.symbol)
    hist = stock.history(period="1d")
    current_price = hist['Close'].iloc[-1]
    return {
        "symbol": request.symbol,
        "current_price": round(current_price, 2)
    }

