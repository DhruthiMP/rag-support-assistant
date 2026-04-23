# High-Level Design (HLD)
## RAG-Based Customer Support Assistant

---

## 1. System Overview

### Problem Statement
Customers frequently ask repetitive questions such as password reset, refund policies, and order tracking. Manual customer support is time-consuming, expensive, and not scalable.

### Solution
This project implements a Retrieval-Augmented Generation (RAG)-based Customer Support Assistant that:
- Processes a knowledge base (PDF/Text)
- Retrieves relevant information using embeddings
- Generates contextual answers
- Uses a workflow-based decision system
- Escalates to human support when needed (HITL)

---

## 2. Architecture Diagram

            +----------------------+
            |      User (UI)       |
            |   (Streamlit App)    |
            +----------+-----------+
                       |
                       v
            +----------------------+
            |   Query Processing   |
            +----------+-----------+
                       |
                       v
            +----------------------+
            |   LangGraph Engine   |
            | (Workflow Control)   |
            +----------+-----------+
                       |
        +--------------+--------------+
        |                             |
        v                             v

+----------------------+ +----------------------+
| Retriever | | Routing Decision |
| (Similarity Search) | | (Respond / Escalate) |
+----------+-----------+ +----------+-----------+
| |
v v
+----------------------+ +----------------------+
| ChromaDB | | HITL (Human Agent) |
| (Vector Database) | +----------------------+
+----------+-----------+
|
v
+----------------------+
| Context Builder |
+----------+-----------+
|
v
+----------------------+
| Response Generator |
| (LLM / Rule Engine) |
+----------------------+


---

## 3. Component Description

### 1. Document Loader
Loads the knowledge base from PDF or text files.

### 2. Chunking Strategy
Splits large documents into smaller chunks (e.g., 500 characters with overlap) for better retrieval accuracy.

### 3. Embedding Model
Converts text chunks into vector representations using embedding models.

### 4. Vector Store (ChromaDB)
Stores embeddings and enables efficient similarity search.

### 5. Retriever
Fetches relevant chunks based on user query using similarity search.

### 6. LLM Layer
Responsible for generating answers based on retrieved context.  
In this implementation, a rule-based approach is used instead of a live LLM API for stability and cost efficiency.

### 7. Graph Workflow Engine (LangGraph)
Controls the flow of execution using nodes and edges.

### 8. Routing Layer
Determines whether to:
- Respond to the user
- Escalate to human support

### 9. HITL Module (Human-in-the-Loop)
If the system cannot confidently answer, the query is escalated to a human support agent.

---

## 4. Data Flow

1. Load document (PDF/Text)
2. Split document into chunks
3. Convert chunks into embeddings
4. Store embeddings in ChromaDB
5. User submits a query
6. Query is processed and sent to retriever
7. Retriever performs similarity search
8. Relevant chunks are retrieved
9. Context is built from retrieved chunks
10. Response is generated (LLM / Rule Engine)
11. Routing decision:
    - If confident → Respond to user
    - If not → Escalate to human (HITL)

---

## 5. Technology Choices

- **Python** → Core programming language  
- **Streamlit** → User interface for interaction  
- **LangGraph** → Workflow orchestration and control logic  
- **ChromaDB** → Lightweight and efficient vector database  
- **HuggingFace Embeddings** → Free and efficient embedding model  

---

## 6. Scalability Considerations

- Supports large documents using chunking strategy  
- Can scale by using distributed vector databases  
- Can handle multiple concurrent user queries  
- Can be deployed as an API for production use  
- Caching mechanisms can be added to reduce latency  

---

## 7. Key Features

- Context-aware answering using RAG  
- Graph-based workflow using LangGraph  
- Intelligent routing system  
- Human-in-the-Loop fallback  
- Lightweight and cost-efficient implementation  

---

## 8. Conclusion

This system demonstrates a scalable and intelligent customer support assistant using RAG architecture.  
It combines retrieval, workflow orchestration, and decision-making to provide accurate and reliable responses while ensuring fallback to human support when necessary.