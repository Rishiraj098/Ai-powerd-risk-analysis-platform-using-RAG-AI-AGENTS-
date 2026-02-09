Enterprise Risk Intelligence Platform using RAG & AI Agents
## Overview
Enterprise Risk Intelligence Platform is a full-stack AI decision-support system designed to analyze enterprise documents such as policies, audit reports, and compliance files.
The system uses Retrieval-Augmented Generation (RAG) and logically structured AI agents to provide explainable, document-grounded risk insights. This project focuses on architecture-driven intelligence rather than chatbot-style responses.
## Problem Statement
Enterprises generate large volumes of unstructured documents containing hidden risks. Manual analysis is time-consuming, error-prone, and difficult to scale.
## Solution
This platform ingests enterprise documents, converts them into a searchable knowledge base, retrieves relevant information using semantic search, and generates explainable risk insights grounded in real documents.
## Key Features
- Full-stack web application
- RAG-based document grounding
- Vector database for semantic retrieval
- AI agents for retrieval, analysis, and explanation
- Explainable risk outputs with references
- Clean enterprise-style UI

---

## Tech Stack
- Frontend: HTML, CSS, JavaScript
- Backend: Python, FastAPI
- AI: LLM APIs, Embeddings
- Vector Database: FAISS
- Deployment: Vercel (Frontend), Render (Backend)

---

## Architecture
User Query → Vector Search → Relevant Documents → LLM + Context → Explainable Risk Insight

---

## Project Status
🚧 Currently under active development  
📌 Backend and frontend integration in progress

---

## License
MIT License
