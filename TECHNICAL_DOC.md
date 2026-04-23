# Technical Documentation
## RAG-Based Customer Support Assistant

---

## 1. Introduction

### What is RAG?
Retrieval-Augmented Generation (RAG) is a technique that combines information retrieval with text generation.  
Instead of relying only on a language model, it retrieves relevant data from a knowledge base and generates answers based on that.

### Why RAG?
- Reduces hallucination
- Improves accuracy
- Uses real data
- Scalable for real-world systems

### Use Case
Customer support automation:
- Password reset
- Refund queries
- Order tracking
- General FAQs

---

## 2. System Architecture Explanation

The system consists of:

- **UI Layer (Streamlit)** → User interaction  
- **Document Processing** → Load & chunk data  
- **Embedding Layer** → Convert text to vectors  
- **Vector DB (ChromaDB)** → Store embeddings  
- **Retriever** → Fetch relevant data  
- **LangGraph Workflow** → Controls logic  
- **Response Generator** → Generates answer  
- **HITL System** → Escalation to human  

---

## 3. Design Decisions

### Chunk Size
- 500 characters with overlap
- Balance between context and performance

### Embedding Strategy
- HuggingFace embeddings (free & efficient)

### Retrieval Approach
- Similarity search using ChromaDB

### Prompt Design
- Strict instructions:
  - Answer from context only
  - Keep answers short (2–3 lines)

---

## 4. Workflow Explanation (LangGraph)

### Nodes

1. **process_node**
   - Retrieves documents
   - Builds context
   - Generates answer

2. **route_node**
   - Evaluates answer
   - Decides next step

3. **hitl_node**
   - Handles fallback response

---

### State Flow


Query → process_node → route_node → (respond / hitl)


---

## 5. Conditional Logic

### Respond when:
- Relevant context exists
- Answer is meaningful

### Escalate when:
- No documents found
- Answer too short
- Low confidence

---

## 6. HITL Implementation

### Role
Ensures system reliability when AI is uncertain

### Trigger Conditions
- Missing context
- Weak answers

### Response
Returns:
"⚠️ Connecting you to human support..."

### Benefits
- Improves trust
- Avoids wrong answers

---

## 7. Challenges & Trade-offs

### 1. Retrieval Accuracy vs Speed
- More chunks → better accuracy
- But slower retrieval

### 2. Chunk Size vs Context Quality
- Small chunks → faster
- Large chunks → better context

### 3. Cost vs Performance
- Using LLM API → costly
- Using rule-based → cheaper but limited

---

## 8. Testing Strategy

### Sample Queries

- "How to reset password?"
- "What is refund policy?"
- "How to track my order?"

### Expected Behavior
- Correct answers from knowledge base
- Escalation when needed

---

## 9. Future Enhancements

- Multi-document support
- Real LLM integration (OpenAI)
- Feedback learning system
- Chat memory
- API deployment (FastAPI)
- UI improvements

---

## 10. Conclusion

This project demonstrates a complete RAG system with:
- Retrieval + Generation
- Workflow control using LangGraph
- Intelligent routing
- Human fallback mechanism

It reflects real-world system design principles and scalable AI architecture.