from langchain_chroma import Chroma
from config import CHROMA_DB_DIR
from rag.embeddings import crear_modelo_embeddings

def cargar_vectorstore():
    modelo_embeddings = crear_modelo_embeddings()
    vectorstore = Chroma(
        persist_directory=CHROMA_DB_DIR,
        embedding_function=modelo_embeddings
    )
    return vectorstore

def crear_vectorstore(chunks, modelo_embeddings):

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=modelo_embeddings,
        persist_directory=CHROMA_DB_DIR
    )

    return vectorstore