from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup

app = FastAPI()

@app.get("/scrape/filings")
def scrape_filings():
    url = "https://finance.yahoo.com/"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    headlines = [h.text for h in soup.select("h3")][:5]
    return {"headlines": headlines}