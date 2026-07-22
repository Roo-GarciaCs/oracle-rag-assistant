from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq

from config import (
    LLM_PROVIDER,
    GEMINI_API_KEY,
    GEMINI_MODEL,
    GROQ_API_KEY,
    GROQ_MODEL,
)
def crear_llm():

    if LLM_PROVIDER == "google":

        llm = ChatGoogleGenerativeAI(
            model=GEMINI_MODEL,
            google_api_key=GEMINI_API_KEY,
            temperature=0
        )

    elif LLM_PROVIDER == "groq":

        llm = ChatGroq(
            model=GROQ_MODEL,
            groq_api_key=GROQ_API_KEY,
            temperature=0
        )
    else:
        raise ValueError(f"Proveedor de LLM no válido: {LLM_PROVIDER}")

    return llm