

````md
# Research Agent with RAG

## Overview
This project extends a research agent with a local RAG system.

The agent can:
- search the web
- read web pages
- search a local knowledge base
- generate and save Markdown reports

The system supports:
- document ingestion from the `data/` directory
- document chunking
- embeddings generation
- FAISS vector storage
- BM25 lexical retrieval
- hybrid retrieval
- cross-encoder reranking

## Project Structure
```text
homework-lesson-5/
├── main.py
├── agent.py
├── tools.py
├── retriever.py
├── ingest.py
├── config.py
├── requirements.txt
├── data/
├── vector_store/
├── output/
└── .env
````

## Features

* Web search with `web_search`
* Web page reading with `read_url`
* Local knowledge base search with `knowledge_search`
* Markdown report saving with `write_report`

## Ingestion Pipeline

Run the ingestion pipeline before using the knowledge base:

```bash
python ingest.py
```

This will:

* load documents from `data/`
* split them into chunks
* generate embeddings
* build the FAISS index
* save chunk data for BM25 retrieval

## Running the Agent

Start the agent with:

```bash
python main.py
```

## Example Queries

* `What is RAG and what are the main retrieval approaches?`
* `Create a short Markdown report about RAG and retrieval approaches and save it to rag_report.md`

## Requirements

Install dependencies with:

```bash
pip install -r requirements.txt
```

## Notes

* The vector index is stored in `vector_store/`
* Generated reports are stored in `output/`
* API keys must be stored in `.env`


