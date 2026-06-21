# Multi-Agent Research Assistant

A research assistant built using LangGraph, LangChain, Ollama, FAISS, and Streamlit. The application helps automate the process of gathering information, verifying findings, and generating structured research reports. It also supports Retrieval-Augmented Generation (RAG) by allowing users to upload PDF documents and use them as a knowledge source during research.

---

## Features

* Multi-agent workflow using LangGraph
* Local LLM inference with Ollama
* PDF document upload and processing
* Retrieval-Augmented Generation (RAG)
* Semantic search using FAISS
* Wikipedia integration
* DuckDuckGo web search integration
* Automated research report generation
* PDF export support
* Streamlit-based user interface
* Fully local execution

---

## Tech Stack

### Frameworks

* Streamlit
* LangChain
* LangGraph

### LLM & Embeddings

* Ollama
* Phi-3
* Nomic Embed Text

### Retrieval & Storage

* FAISS
* Retrieval-Augmented Generation (RAG)

### Data Sources

* DuckDuckGo Search
* Wikipedia
* PDF Documents

### Report Generation

* ReportLab

---

## Project Architecture

```text
User Query
    │
    ▼
Research Agent
    │
    ├── Web Search
    ├── Wikipedia Search
    └── PDF Retrieval (RAG)
    │
    ▼
Verification Agent
    │
    ▼
Writer Agent
    │
    ▼
PDF Report Generator
    │
    ▼
Final Research Report
```

---

## How It Works

### Research Agent

The Research Agent gathers information from multiple sources including web search, Wikipedia, and uploaded PDF documents. The collected information is combined into a structured research summary.

### Verification Agent

The Verification Agent reviews the collected information, removes duplicate content, improves readability, and filters weak or repetitive statements.

### Writer Agent

The Writer Agent converts the verified information into a professional report containing:

* Executive Summary
* Key Findings
* Detailed Analysis
* Conclusion
* References

---

## RAG Pipeline

```text
PDF Upload
    │
    ▼
Document Loading
    │
    ▼
Text Chunking
    │
    ▼
Embeddings
(nomic-embed-text)
    │
    ▼
FAISS Vector Store
    │
    ▼
Semantic Retrieval
    │
    ▼
Context Injection into LLM
```

---

## Project Structure

```text
Multi-Agent-Research-Assistant/

├── agents/
│   ├── researcher.py
│   ├── verifier.py
│   └── writer.py
│
├── graph/
│   └── workflow.py
│
├── tools/
│   ├── search_tool.py
│   ├── wiki_tool.py
│   ├── rag_tool.py
│   └── pdf_generator.py
│
├── vector_db/
├── reports/
│
├── app.py
├── config.py
├── requirements.txt
└── README.md
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/Multi-Agent-Research-Assistant.git

cd Multi-Agent-Research-Assistant
```

### Create a Virtual Environment

```bash
python -m venv .venv
```

### Activate the Environment

Windows:

```bash
.venv\Scripts\activate
```

Linux/Mac:

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Required Packages

```text
streamlit
langchain
langgraph
langchain-community
langchain-ollama
faiss-cpu
pypdf
duckduckgo-search
ddgs
wikipedia
reportlab
python-dotenv
```

---

## Install Ollama Models

```bash
ollama pull phi3
ollama pull nomic-embed-text
```

Optional models:

```bash
ollama pull llama3
ollama pull mistral
```

---

## Running the Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## Usage

### Research Without a PDF

1. Enter a research topic.
2. Click **Generate Report**.
3. The system collects information from web search and Wikipedia.
4. A structured report is generated.

### Research With a PDF

1. Upload a PDF document.
2. Enter a research topic.
3. Click **Generate Report**.
4. Relevant information is retrieved from the uploaded document using RAG.
5. A report is generated using both document and web-based information.

---

## Skills Demonstrated

* Multi-Agent Systems
* Retrieval-Augmented Generation (RAG)
* Vector Databases (FAISS)
* Semantic Search
* Local LLM Deployment
* LangGraph Workflows
* Prompt Engineering
* Document Intelligence
* Streamlit Application Development
* Report Automation

---

## Future Improvements

* Multi-PDF support
* Source citation tracking
* Conversation memory
* Report templates
* DOCX export
* Research history dashboard
* Cloud deployment

---

## Author

Rukesh

This project was built as a hands-on exploration of multi-agent workflows, Retrieval-Augmented Generation (RAG), and local LLM applications using open-source tools.
