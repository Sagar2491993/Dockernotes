
from langchain_openai import AzureChatOpenAI
from dotenv import load_dotenv
import os
load_dotenv()
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt



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
st.header("reasearch tool") 
paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )


template = PromptTemplate(
    template = """ 
Please summarize the research paper provided in "{paper_input}" with the following specifications:

**Explanation Style:** {style_input}  
**Summary Length:** {length_input}  

### Key Requirements:
1. **Mathematical Details:**  
   - Include relevant mathematical equations if present in the paper.  
   - Explain mathematical concepts using simple, intuitive code snippets where applicable (e.g., Python).  

2. **Use of Analogies:**  
   - Simplify complex ideas using relatable analogies.  
   - If certain information is not available in the paper, respond with:  
     _"Insufficient information available."_  

Ensure the summary is **clear, accurate, and aligned** with the requested style and length.  
""",

    input_variables=["paper_input", "style_input", "length_input"],  # mandetary all input write otherwise show the error 
    validate_template= True  # all input in string
)

    
# fill placeholder
prompt = template.invoke({
    "paper_input":paper_input,
    "style_input":style_input,
    "length_input":length_input
})


if st.button("summarize"):
    result = model.invoke(prompt)
    st.write(result.content)
