from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
llm=ChatOpenAI(model="gpt-4")
result=llm.invoke("What is capital of Telangana")
print(result.content)
#The issue with the output because API Key has 0 credits.