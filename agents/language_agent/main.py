from fastapi import FastAPI, Request
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

@app.post("/generate/summary")
async def generate_summary(request: Request):
    body = await request.json()
    facts = body.get("facts", "")
    prompt = f"Summarize this data into a daily finance report: {facts}"
    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return {"summary": completion.choices[0].message["content"]}