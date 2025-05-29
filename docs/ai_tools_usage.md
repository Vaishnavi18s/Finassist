# AI Tool Usage Log

## Overview
This document captures the detailed usage of AI tools in the Multi-Agent Finance Assistant project, including prompts used, code generation, model configuration, and reasoning for tool selection.

---

## 1. Model & Frameworks

- **LLM Used:** Deepseek/ OpenAI GPT-4 
- **Integration Framework:** LangChain
- **Search Engine:** FAISS
- **LLM API Params:**
  ```json
  {
    "temperature": 0.3,
    "top_p": 0.95,
    "max_tokens": 1024
  }

## Prompt Engineering Log

Orchestrator → LLM Agent
Prompt Used:

input:-

"You are a multi-agent orchestrator. When a user asks for stock advice, classify the intent, route to retriever or analysis agent, and return insights."

Expected Response:
{
  "intent": "get_stock_analysis",
  "target_agent": "analysis_agent"
}
Retriever Agent → FAISS Query
Prompt Pattern:

"Retrieve top 3 documents related to yfin earnings report"
Embedding Model:

text-embedding-ada-002 or bge-small-en

## Code Generation with LLM
Streamlit UI Generator
