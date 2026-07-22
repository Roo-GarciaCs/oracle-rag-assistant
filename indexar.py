from config import PDF_PATH

from rag.loader import cargar_documentos
from rag.splitter import dividir_documentos
from rag.embeddings import crear_modelo_embeddings
from rag.vectorstore import crear_vectorstore


print("Cargando documento...")

documentos = cargar_documentos(PDF_PATH)

print(f"Documentos cargados: {len(documentos)}")


print("Dividiendo documento...")

chunks = dividir_documentos(documentos)

print(f"Chunks creados: {len(chunks)}")


print("Creando modelo de embeddings...")

modelo_embeddings = crear_modelo_embeddings()


print("Creando base vectorial...")

vectorstore = crear_vectorstore(
    chunks,
    modelo_embeddings
)

print("¡Indexación completada correctamente!")