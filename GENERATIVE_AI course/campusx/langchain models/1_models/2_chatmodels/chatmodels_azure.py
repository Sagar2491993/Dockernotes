# from langchain_openai import  AzureChatOpenAI
# from dotenv import load_dotenv

# load_dotenv()

# model = AzureChatOpenAI(model='gpt-4', temperature=1.5, max_completion_tokens=10)

# result = model.invoke("Write a 5 line poem on cricket")

# print(result.content)

from langchain_openai import AzureChatOpenAI
from dotenv import load_dotenv
import os
load_dotenv()
from langchain.chat_models import AzureChatOpenAI

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
result = model.invoke("Write a 5 line poem on cricket")

print(result.content)