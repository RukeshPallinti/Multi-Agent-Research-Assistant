import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings

from config import (
    CHUNK_SIZE,
    CHUNK_OVERLAP,
    VECTOR_DB_DIR,
    EMBEDDING_MODEL
)


def get_embeddings():
    return OllamaEmbeddings(
        model=EMBEDDING_MODEL
    )


def build_vector_store(pdf_path: str):

    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )

    chunks = splitter.split_documents(documents)

    embeddings = get_embeddings()

    vector_store = FAISS.from_documents(
        chunks,
        embeddings
    )

    os.makedirs(VECTOR_DB_DIR, exist_ok=True)

    vector_store.save_local(VECTOR_DB_DIR)

    return {
        "status": "success",
        "chunks_created": len(chunks)
    }


def load_vector_store():
    """
    SAFE LOADER:
    - Never crashes app
    - Returns None if DB doesn't exist
    """

    index_path = os.path.join(VECTOR_DB_DIR, "index.faiss")

    if not os.path.exists(index_path):
        return None

    embeddings = get_embeddings()

    try:
        return FAISS.load_local(
            VECTOR_DB_DIR,
            embeddings,
            allow_dangerous_deserialization=True
        )
    except Exception as e:
        print(f"[RAG WARNING] Failed to load vector store: {e}")
        return None


def search_documents(query: str, k: int = 4):

    vector_store = load_vector_store()

    # ✅ FIRST RUN SAFE BEHAVIOR
    if vector_store is None:
        return "📄 No PDF knowledge base found. Please upload or index a document first."

    try:
        docs = vector_store.similarity_search(
            query=query,
            k=k
        )

        return "\n\n".join(doc.page_content for doc in docs)

    except Exception as e:
        return f"RAG search failed: {e}"