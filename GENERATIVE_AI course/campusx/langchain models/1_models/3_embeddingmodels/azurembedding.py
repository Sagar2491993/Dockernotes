# # from langchain_openai import OpenAIEmbeddings
# # from dotenv import load_dotenv

# # load_dotenv()

# # embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

# # result = embedding.embed_query("Delhi is the capital of India")

# # print(str(result))


# # # Initialize Azure OpenAI Embeddings
# # embedding = OpenAIEmbeddings(
# #     model=deployment_name,  # Use deployment name instead of model name
# #     dimensions=32,
# #     openai_api_key=azure_api_key,
# #     openai_api_base=azure_endpoint,
# #     openai_api_type="azure",
# #     openai_api_version="2023-12-01-preview"  # Use the latest version available
# # )

# # # Perform embedding
# # result = embedding.embed_query("Delhi is the capital of India")

# # # Print the result
# # print(str(result))




# from langchain_openai import AzureChatOpenAI
# from langchain_openai import OpenAIEmbeddings
# from dotenv import load_dotenv
# import os
# load_dotenv()


# # --> AZURE DEPLOYMENT CONFIG VARIABLES
# AZURE_OPENAI_ENDPOINT = os.getenv('AZURE_OPENAI_ENDPOINT')
# AZURE_DEPLOYMENT = os.getenv('AZURE_DEPLOYMENT')
# AZURE_API_VERSION = os.getenv('AZURE_API_VERSION')

# model = AzureChatOpenAI(
#     azure_endpoint=AZURE_OPENAI_ENDPOINT,
#     azure_deployment=AZURE_DEPLOYMENT,
#     api_version=AZURE_API_VERSION,
#     temperature=0,
# )

# embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)



# result = model.invoke("Write a 5 line poem on cricket")

# print(result.content)


import os
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-large",
    openai_api_key=os.getenv("AZURE_OPENAI_ENDPOINT"),
    #openai_api_base=os.getenv("OPENAI_API_BASE"),
    openai_api_version=os.getenv("AZURE_API_VERSION"),
    dimensions=32
)

result = embeddings.embed_query("Write a 5 line poem on cricket")
print(result.content)