
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

# convectional but not store histry
while True:
    user_input = input('You: ')
    if user_input == "exit":
        break
    result = model.invoke(user_input)
    print("AI: ", result.content)


    
  



