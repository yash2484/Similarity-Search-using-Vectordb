import streamlit as st
from vector_store import load_vectorstore, search_similar_queries

st.set_page_config(page_title="User Query Characterization")
st.title("🔍 User Query Similarity Bot")

user_query = st.text_input("Enter your query:")

if user_query:
    vectorstore = load_vectorstore()
    results = search_similar_queries(user_query, vectorstore)

    st.subheader("Top 5 Similar Queries")
    for i, query in enumerate(results, 1):
        st.markdown(f"**{i}.** {query}")
