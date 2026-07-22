from dotenv import load_dotenv
import os

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
PDF_PATH = os.path.join(DATA_DIR, "oracle_manual.pdf")
CHROMA_DB_DIR = os.path.join(BASE_DIR, "chroma_db")

# Configuración del splitter
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 50

# Configuración del Retriever

TOP_K = 4
SCORE_THRESHOLD = 0.15
SEARCH_TYPE = "similarity_score_threshold"

# Proveedores

EMBEDDING_PROVIDER = "huggingface"
LLM_PROVIDER = "groq"

# Modelos

GEMINI_MODEL = "gemini-2.5-flash"
GROQ_MODEL = "llama-3.3-70b-versatile"