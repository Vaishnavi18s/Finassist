# Architecture :-

+--------------------+
|   Streamlit Frontend  |
+--------------------+
           ↓
+--------------------+
|   Orchestrator Agent   |
+--------------------+
     ↓        ↓       ↓
+--------+ +--------+ +--------+
| API    | | Analysis | | Voice  |
| Agent  | | Agent    | | Agent  |
+--------+ +--------+ +--------+
     ↓        ↓       ↓
+--------+ +------------+ +------------+
| Scraper| | Retriever   | | LLM/Language|
| Agent  | | Agent       | | Agent       |
+--------+ +------------+ +------------+

# Setup and deployment

Local Setup
Folder Structure:
finassist/
├── docker-compose.yml
├── .env
├── api_agent/
│   ├── Dockerfile
│   ├── main.py
│   └── requirements.txt
├── analysis_agent/
├── language_agent/
├── retriever_agent/
├── scraping_agent/
├── streamlit_app/
├── orchestrator/
└── voice_agent/

Sample docker-compose.yml (simplified for two agents):

services:
  api_agent:
    build: ./api_agent
    ports:
      - "8000:8000"
  analysis_agent:
    build: ./analysis_agent
    ports:
      - "8001:8000"
      
Run all containers:

docker-compose up --build
Verify running containers

(Didnt deploy due to RAM shortage)

# Performance Benchmarks
depennds on following agents:-
API Agent
Analysis Agent	
Retriever Agent	


