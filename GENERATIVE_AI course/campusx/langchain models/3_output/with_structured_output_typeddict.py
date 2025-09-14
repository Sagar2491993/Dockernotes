#from typing import TypedDict, Annotated, Optional, Literal

from typing import TypedDict, Annotated, Optional
from langchain_openai import AzureChatOpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Azure OpenAI Configuration
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_DEPLOYMENT = os.getenv("AZURE_DEPLOYMENT")
AZURE_API_VERSION = os.getenv("AZURE_API_VERSION")

# Debugging: Ensure environment variables are loaded
if not AZURE_OPENAI_API_KEY:
    raise ValueError("Missing AZURE_OPENAI_API_KEY. Check your .env file.")

# Initialize Azure OpenAI Model
model = AzureChatOpenAI(
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    azure_deployment=AZURE_DEPLOYMENT,
    api_version=AZURE_API_VERSION,
    api_key=AZURE_OPENAI_API_KEY,
    temperature=0,
)

# Schema for structured output
class Review(TypedDict):
    key_themes: Annotated[list[str], "List of key themes in the review"]
    summary: Annotated[str, "Brief summary of the review"]
    #sentiment: Annotated[Literal["pos", "neg"], "Sentiment of the review"]

    sentiment: Annotated[str, "Sentiment of the review positive and negative"]
    

    pros: Annotated[Optional[list[str]], "List of pros"]
    cons: Annotated[Optional[list[str]], "List of cons"]
    name: Annotated[Optional[str], "Reviewer's name"]

# Configure structured output model

structured_model = model.with_structured_output(Review)

# Sample review processing
result = structured_model.invoke(
    """I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it's an absolute powerhouse! 
    The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. 
    The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver. 
    The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. 
    The 200MP camera is stunning, capturing crisp, vibrant images even in low light. 
    However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI comes with bloatware. 
    Review by Nitish Singh."""
)

#print(result.get('name', 'No reviewer name found'))
print(result)