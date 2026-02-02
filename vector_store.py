import json
import os
import sys
from dotenv import load_dotenv
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.schema import Document

load_dotenv()

DB_FAISS_PATH = "faiss_index"
QUERY_DB_PATH = "query_database.json"

# Load or create the FAISS vector store
def load_vectorstore():
    if os.path.exists(DB_FAISS_PATH):
        return FAISS.load_local(DB_FAISS_PATH, OpenAIEmbeddings())
    else:
        with open(QUERY_DB_PATH, 'r') as f:
            queries = json.load(f)
        documents = [Document(page_content=q) for q in queries]
        vectorstore = FAISS.from_documents(documents, OpenAIEmbeddings())
        vectorstore.save_local(DB_FAISS_PATH)
        return vectorstore

# Search top 5 similar queries
def search_similar_queries(query, vectorstore):
    results = vectorstore.similarity_search(query, k=5)
    return [doc.page_content for doc in results]
