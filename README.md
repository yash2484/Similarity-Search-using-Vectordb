# Similarity Search with Vector Embeddings

## Overview
This project is an **introductory implementation of similarity search** using vector embeddings. It demonstrates how textual data can be converted into numerical vectors, stored in a vector database, and queried to retrieve semantically similar results.

---

## Key Concepts
- Vector embeddings  
- Semantic similarity  
- Vector databases  
- Nearest neighbor search  

---

## Project Structure
```text
3-SimilaritySearch/
├── app.py                 # Main application logic
├── vector_store.py        # Vector store creation and search logic
├── singlestoredb.py       # Database connection and storage
├── query_database.json    # Sample data for querying
├── requirements           # Project dependencies
├── .gitignore
└── README.md
```


## How It Works
Text data is converted into vector embeddings

Embeddings are stored in a vector database

User queries are embedded and compared using similarity metrics

The most relevant results are returned

## Setup and Run
Install dependencies
bash
Copy code
pip install -r requirements
Run the application
bash
Copy code
python app.py
Purpose
This project serves as a foundation for understanding similarity search, a core building block for modern AI systems such as search engines, recommendation systems, and Retrieval-Augmented Generation (RAG) pipelines.

### Future Enhancements
Scale to larger datasets

Add an API or UI layer

Extend to RAG-based applications
