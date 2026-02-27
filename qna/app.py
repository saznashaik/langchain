# Q&A Chatbot using LangChain + OpenAI + Streamlit

import streamlit as st
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()

# Function to get response
def get_openai_response(question):
    
    llm = ChatOpenAI(
        model="gpt-4o-mini",   # recommended model
        temperature=0.5
    )
    
    response = llm.invoke(question)
    
    return response.content


# Initialize Streamlit app
st.set_page_config(page_title="Q&A Demo")

st.header("LangChain Application")

# Input box
user_input = st.text_input("Input:", key="input")

# Button
submit = st.button("Ask the question")

# Generate response only when button clicked
if submit and user_input:
    
    response = get_openai_response(user_input)
    
    st.subheader("The Response is:")
    st.write(response)
