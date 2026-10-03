from langchain_openai import OpenAiEmbeddings
from dotenv import load_dotenv
load_dotenv()

embedding=OpenAiEmbeddings(model='text-embedding-3-large',dimensions=32)
result=embedding.embed_query("What is capital of Telangana")
print(result)
#The issue with the output because API Key has 0 credits.