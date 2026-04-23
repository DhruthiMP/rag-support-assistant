# Low-Level Design (LLD)
## RAG-Based Customer Support Assistant

---

## 1. Module-Level Design

### 1. Document Processing Module
- Reads input file (`support.txt` / PDF)
- Loads content into memory

### 2. Chunking Module
- Splits text into chunks
- Chunk size: 500 characters
- Overlap: 100 characters

### 3. Embedding Module
- Converts text chunks into vectors
- Uses HuggingFace embeddings

### 4. Vector Storage Module
- Stores embeddings in ChromaDB
- Enables similarity search

### 5. Retrieval Module
- Accepts user query
- Retrieves top relevant chunks

### 6. Query Processing Module
- Takes user input
- Sends query to retriever

### 7. Graph Execution Module
- Controls workflow using LangGraph
- Nodes:
  - process_node
  - route_node
  - hitl_node

### 8. HITL Module
- Handles escalation
- Returns fallback response

---

## 2. Data Structures

### Document Format
```python
{
    "page_content": "text data",
    "metadata": {}
}
````

### Chunk Format

```python
{
    "chunk_text": "text chunk"
}
```

### State Object (Graph)

```python
{
    "query": str,
    "retriever": object,
    "answer": str,
    "decision": str
}
```

---

## 3. Workflow Design (LangGraph)

### Nodes

1. **process_node**

   * Retrieves documents
   * Builds context
   * Generates answer

2. **route_node**

   * Checks answer quality
   * Decides:

     * respond
     * escalate

3. **hitl_node**

   * Returns fallback response

---

### Edges

```
process → route
route → respond (end)
route → hitl
hitl → end
```

---

## 4. Conditional Routing Logic

### Respond when:

* Answer is not empty
* Answer length is sufficient
* Context is found

### Escalate when:

* No documents retrieved
* Answer is too short
* Low confidence

---

## 5. HITL Design

### When triggered:

* No context found
* Weak/short answer

### Action:

* Return fallback message:
  "⚠️ Connecting you to human support..."

### Future:

* Integrate real support system

---

## 6. API / Interface Design

### Input

```json
{
    "query": "user question"
}
```

### Output

```json
{
    "answer": "response text"
}
```

---

## 7. Error Handling

### Cases handled:

* No relevant documents → fallback
* Empty query → ignored
* LLM failure → fallback

---

## 8. File Structure

```
rag-support-assistant/
│
├── app.py
├── graph.py
├── rag_pipeline.py
├── data/
│   └── support.txt
├── HLD.md
├── LLD.md
```

---

## 9. Key Implementation Details

* Uses ChromaDB for vector storage
* Uses LangGraph for workflow control
* Uses rule-based answering for stability
* Uses Streamlit for UI

---

## 10. Summary

This LLD defines the internal working of the RAG system, including modules, data flow, decision logic, and workflow execution using LangGraph.