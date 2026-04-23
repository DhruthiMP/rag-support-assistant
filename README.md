# 💬 RAG Customer Support Assistant

## 📌 Project Overview
This project is a Retrieval-Augmented Generation (RAG) based Customer Support Assistant built using LangGraph and ChromaDB.

It answers user queries based on a knowledge base and escalates to human support when needed.

---

## 🚀 Features
- 📄 Loads knowledge base (PDF/Text)
- 🔍 Retrieves relevant information using embeddings
- 🤖 Generates contextual answers
- 🔀 Uses LangGraph workflow
- ⚠️ Human-in-the-Loop (HITL) escalation

---

## 🏗️ Tech Stack
- Python
- Streamlit (UI)
- LangChain
- LangGraph
- ChromaDB

---

## 📂 Project Structure

rag-support-assistant/
│── app.py
│── graph.py
│── rag_pipeline.py
│── llm.py
│── data/
│ └── support.txt
│── HLD.md
│── LLD.md
│── TECHNICAL_DOC.md
│── requirements.txt


---

## ⚙️ Setup Instructions

### 1. Clone repo

git clone <your-repo-link>
cd rag-support-assistant


### 2. Create virtual environment

python -m venv venv
source venv/bin/activate


### 3. Install dependencies

pip install -r requirements.txt


### 4. Run the app

streamlit run app.py


---

## 💡 Example Questions
- How can I reset my password?
- What is the refund policy?
- How to track my order?

---

## 🔄 Workflow
User Query → Retriever → Context → LLM → Decision  
→ Respond OR Escalate (HITL)

---

## ⚠️ HITL (Human-in-the-Loop)
If:
- No context found  
- Answer too short  

➡️ System escalates to human support.

---

## 📊 Future Improvements
- Multi-document support
- Chat history memory
- API deployment
- Better UI design

---

## 👩‍💻 Author
Dhruthi M P