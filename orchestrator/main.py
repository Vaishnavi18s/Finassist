from fastapi import FastAPI, Request
import requests

app = FastAPI()

@app.post("/orchestrate")
async def orchestrate(request: Request):
    body = await request.json()
    query = body["query"]
    
    api_data = requests.get("http://api_agent:8001/api/fetch_data?ticker=TSM").json()
    headlines = requests.get("http://scraping_agent:8002/scrape/filings").json()
    retriever_data = requests.post("http://retriever_agent:8003/retrieve/docs", json={"query": query}).json()
    analysis = requests.get("http://analysis_agent:8004/analyze/aum").json()
    facts = f"API: {api_data}, Headlines: {headlines}, Retriever: {retriever_data}, Analysis: {analysis}"
    summary = requests.post("http://language_agent:8005/generate/summary", json={"facts": facts}).json()
    return {"response": summary["summary"]}