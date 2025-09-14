
from langchain_openai import AzureChatOpenAI
from dotenv import load_dotenv
import os
load_dotenv()
import streamlit as st



# --> AZURE DEPLOYMENT CONFIG VARIABLES
AZURE_OPENAI_ENDPOINT = os.getenv('AZURE_OPENAI_ENDPOINT')
AZURE_DEPLOYMENT = os.getenv('AZURE_DEPLOYMENT')
AZURE_API_VERSION = os.getenv('AZURE_API_VERSION')

model = AzureChatOpenAI(
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    azure_deployment=AZURE_DEPLOYMENT,
    api_version=AZURE_API_VERSION,
    temperature=0,
)

st.header('Reasearch Tool')
user_input = st.text_input("enter the prompt")

if st.button("summarize"):
    result = model.invoke(user_input)
    st.write(result.content)


   