import streamlit as st

from app import responder

st.set_page_config(
    page_title="Oracle Cloud RAG Assistant",
    layout="centered"
)
st.title("Oracle Cloud RAG Assistant")

with st.sidebar:


    st.title("Oracle RAG")

    st.markdown("---")

    st.subheader("Proyecto")

    st.write(
        """
        Asistente basado en **RAG** que responde preguntas
        utilizando exclusivamente el Manual de Oracle Cloud Infrastructure.
        """
    )

    st.markdown("---")

    st.subheader("🛠 Tecnologías")

    st.markdown("""
- Python
- Streamlit
- LangChain
- ChromaDB
- HuggingFace
- Groq
""")

    st.markdown("---")

    st.subheader("Desarrollado por:")

    st.write("Roberto García")

    st.caption("Proyecto desarrollado para Alura Challenge IA")

    st.caption("Alura Challenge 2026")

st.markdown(
    """
Consulta el **Manual de Oracle Cloud Infrastructure (OCI)** mediante
**Inteligencia Artificial + RAG**.

Escribe una pregunta relacionada con Oracle Cloud Infrastructure y el asistente
responderá utilizando únicamente la información del documento.
"""
)

st.info(
    """
**Ejemplos de preguntas:**

• ¿Qué es un compartimento?

• ¿Qué es una VCN?

• ¿Qué es Oracle Cloud Infrastructure?

• ¿Cómo funcionan las políticas de acceso?
"""
)

pregunta = st.text_input(
    "Escribe tu pregunta:",
    placeholder="Ejemplo: ¿Qué es un compartimento?"
)

if st.button("🔎 Consultar"):

    if not pregunta.strip():

        st.warning("Escribe una pregunta.")

    else:

        with st.spinner("Consultando el documento..."):

            respuesta = responder(pregunta)

        st.subheader("Respuesta")

        st.write(respuesta)