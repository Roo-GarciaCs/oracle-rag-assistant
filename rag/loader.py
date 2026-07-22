
from pathlib import Path
from langchain_community.document_loaders import PyMuPDFLoader

def cargar_documentos(ruta_pdf):

    ruta = Path(ruta_pdf)

    if not ruta.exists():
        raise FileNotFoundError(
            f"No se encontró el archivo PDF: {ruta}"
        )

    loader = PyMuPDFLoader(str(ruta))

    documentos = loader.load()

    return documentos
