import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq   # ✅ correct import

load_dotenv()

def get_llm():
    return ChatGroq(
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model_name=os.getenv("GROQ_MODEL")
    )