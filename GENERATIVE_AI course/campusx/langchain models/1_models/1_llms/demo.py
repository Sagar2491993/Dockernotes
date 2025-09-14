from langchain_openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
import os

api_key = os.getenv("AZURE_API_KEY")


llm = OpenAI(model='gpt-3.5-turbo-instruct')

result = llm.invoke("What is the capital of India")

print(result)