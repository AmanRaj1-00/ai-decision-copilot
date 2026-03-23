import streamlit as st
import ollama

st.title("💬 AI Business Chat")

question = st.text_input("Ask something")

if question:
    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": question}]
    )
    st.write(response["message"]["content"])
