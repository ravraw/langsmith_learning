from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

load_dotenv()
os.environ["LANGSMITH_PROJECT"] = "01_simple_llm"

# Simple one-line prompt
prompt = PromptTemplate.from_template("{question}")

model = ChatOpenAI(model='gpt-4o-mini')
parser = StrOutputParser()

# Chain: prompt → model → parser
chain = prompt | model | parser

# Run it
result = chain.invoke({"question": "What is the capital of USA?"})
print(result)