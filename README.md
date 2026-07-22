# Oracle Cloud RAG Assistant

Asistente inteligente basado en **Retrieval-Augmented Generation (RAG)** que permite consultar el Manual de Oracle Cloud Infrastructure (OCI) utilizando Inteligencia Artificial.

El proyecto fue desarrollado como parte del **Alura Challenge IA**, implementando una arquitectura modular con LangChain, ChromaDB y un modelo LLM para responder preguntas únicamente con información contenida en el documento.

---

# Características

- Consulta un manual PDF de Oracle Cloud Infrastructure.
- Búsqueda semántica mediante embeddings.
- Base vectorial utilizando ChromaDB.
- Traducción automática de preguntas del español al inglés.
- Respuestas generadas por un LLM (Groq).
- Interfaz web desarrollada con Streamlit.
- Arquitectura modular para facilitar mantenimiento y escalabilidad.

---

# Tecnologías utilizadas

- Python
- Streamlit
- LangChain
- ChromaDB
- HuggingFace Embeddings
- Groq API
- PyMuPDF

---

# Estructura del proyecto

```
oracle-rag-assistant/
│
├── rag/
│   ├── loader.py
│   ├── splitter.py
│   ├── embeddings.py
│   ├── vectorstore.py
│   ├── retriever.py
│   └── llm.py
│
├── chroma_db/
├── data/
│   └── oracle_manual.pdf
│
├── app.py
├── config.py
├── indexar.py
├── streamlit_app.py
├── requirements.txt
└── README.md
```

---

# Funcionamiento

1. Se carga el documento PDF.
2. El contenido se divide en fragmentos.
3. Se generan embeddings.
4. Los embeddings se almacenan en ChromaDB.
5. El usuario realiza una pregunta.
6. La pregunta se traduce al inglés.
7. Se recuperan los fragmentos más relevantes.
8. El LLM genera una respuesta basada únicamente en el documento.

---
# Arquitectura

```
PDF
   │
   ▼
Loader
   │
   ▼
Splitter
   │
   ▼
Embeddings
   │
   ▼
ChromaDB
   │
   ▼
Retriever
   │
   ▼
Groq LLM
   │
   ▼
Respuesta
```

# Instalación

Instalar dependencias:
# Variables de entorno

Crear un archivo `.env` en la raíz del proyecto.

Ejemplo:

```env
GROQ_API_KEY=tu_api_key
GOOGLE_API_KEY=tu_api_key
```

```bash
pip install -r requirements.txt
```

Crear el archivo `.env` con las credenciales necesarias.

---

# Ejecutar la indexación

```bash
python indexar.py
```

---

# Ejecutar la aplicación

```bash
streamlit run streamlit_app.py
```

---

# Ejemplos de preguntas

- ¿Qué es un compartimento?
- ¿Qué es Oracle Cloud Infrastructure?
- ¿Qué es una VCN?
- ¿Cómo funcionan las políticas de acceso?

---

# Autor

**Roberto García**

Proyecto desarrollado para el **Alura Challenge IA**.

# Notas

Este proyecto responde únicamente con información recuperada del Manual de Oracle Cloud Infrastructure mediante una arquitectura RAG.

Si la información no existe en el documento, el asistente indica que no encontró información relacionada.