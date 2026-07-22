from langchain_huggingface import HuggingFaceEmbeddings


def crear_modelo_embeddings():

    modelo = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    return modelo