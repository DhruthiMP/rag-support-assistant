from langgraph.graph import StateGraph


def process_node(state):
    query = state["query"]
    retriever = state["retriever"]

    docs = retriever.invoke(query)

    if not docs:
        return {"answer": "⚠️ Not confident. Connecting to human support..."}

    query_lower = query.lower()

    # 🔥 Rule-based answers (clean & reliable)
    if "password" in query_lower:
        return {
            "answer": "Go to login page → Click 'Forgot Password' → Enter your email → Follow instructions sent to your email."
        }

    if "refund" in query_lower:
        return {
            "answer": "Refunds are allowed within 7 days. Product must be unused. Contact support to request refund."
        }

    if "track" in query_lower:
        return {
            "answer": "Login to your account → Go to 'My Orders' → Click 'Track Order'."
        }

    return {"answer": "⚠️ Not confident. Connecting to human support..."}


def build_graph():
    graph = StateGraph(dict)

    graph.add_node("process", process_node)

    graph.set_entry_point("process")

    return graph.compile()