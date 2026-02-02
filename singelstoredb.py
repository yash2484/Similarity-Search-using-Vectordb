from sentence_transformers import SentenceTransformer, util

import numpy as np
model = SentenceTransformer('all-MiniLM-L6-v2')

# Example documents
documents = [

    "The quick brown fox jumps over the lazy dog.",

    "I had a great time at the park with my friends.",

    "The economy is showing signs of recovery after the pandemic.",

    "The surface of Mars is red due to iron oxide.",

    "Machine learning models have become very sophisticated."

]

# Example query
query = "Natural language processing models"

# Encode the documents
document_embeddings = model.encode(documents)

# Encode the query
query_embedding = model.encode(query)

##abhishek.gitam@gmail.com
