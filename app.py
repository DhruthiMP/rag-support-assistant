import streamlit as st
from rag_pipeline import create_vectorstore
from graph import build_graph

st.title("💬 RAG Customer Support Assistant")

query = st.text_input("Ask your question:")

if query:
    with st.spinner("Processing..."):

        vectorstore = create_vectorstore()
        retriever = vectorstore.as_retriever()

        graph = build_graph()

        result = graph.invoke({
            "query": query,
            "retriever": retriever
        })

        st.success(result.get("answer", "No response"))