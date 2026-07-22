from rag.vectorstore import cargar_vectorstore
from rag.retriever import crear_retriever
from rag.llm import crear_llm

vectorstore = cargar_vectorstore()
print(vectorstore._collection.count())
retriever = crear_retriever(vectorstore)
llm = crear_llm()

def traducir_consulta(pregunta):

    prompt_traduccion = f"""
You are a translator.

Translate the following question into English.

Rules:
- Return ONLY the translation.
- Do not answer the question.
- Do not explain.
- Preserve Oracle Cloud Infrastructure technical terms.

Question:
{pregunta}
"""

    respuesta = llm.invoke(prompt_traduccion)

    return respuesta.content.strip()

def responder(pregunta):
    consulta = traducir_consulta(pregunta)
    documentos = retriever.invoke(consulta)

    if not documentos:
        return "No encontré información relacionada con esa pregunta en el documento."
    contexto = "\n\n".join(
        documento.page_content
        for documento in documentos
    )
    prompt = f"""
    Eres un asistente especializado en Oracle Cloud Infrastructure (OCI).

    Responde únicamente utilizando la información proporcionada en el contexto.

    Si la respuesta no está en el contexto, indica claramente que no encontraste esa información en el documento.

    Responde siempre en español.

    Contexto:
    {contexto}

    Pregunta:
    {pregunta}

    Respuesta:
    """
    respuesta = llm.invoke(prompt)
    return respuesta.content
if __name__ == "__main__":

    while True:

        pregunta = input("\nHaz una pregunta sobre Oracle (o escribe 'salir'): ")

        if pregunta.lower() == "salir":
            break

        respuesta = responder(pregunta)

        print("\nRespuesta:")
        print(respuesta)
