from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI

def get_llm(name):
    if name == "ollama":
        return ChatOllama(model="llama3.1")
    elif name == "openai":
        return ChatOpenAI(model="gpt-4o")
    raise ValueError(f"Unknown LLM name: {name}")
