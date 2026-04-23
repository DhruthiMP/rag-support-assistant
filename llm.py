from transformers import pipeline

def load_llm():
    return pipeline(
        "text-generation",
        model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
        max_new_tokens=120,
        temperature=0.3
    )