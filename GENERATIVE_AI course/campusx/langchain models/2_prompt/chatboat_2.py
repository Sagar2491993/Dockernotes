
from langchain_openai import AzureChatOpenAI
from dotenv import load_dotenv
import os
load_dotenv()



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

# history store help to response
chat_histry = []
while True:
    user_input = input('You: ')
    chat_histry.append(user_input)
     
    result = model.invoke(chat_histry)
    chat_histry.append(result.content)
    print("AI: ", chat_histry)

print(chat_histry)
