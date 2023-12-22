from dotenv import find_dotenv, load_dotenv
from langchain.llms import OpenAI

load_dotenv(find_dotenv())

openai_llm = OpenAI()
print(openai_llm("How to cook Miso Soup?"))
