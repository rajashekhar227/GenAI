from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from transformers import pipeline
import os
os.environ["HF_HOME"] = "D:/huggingface_cache"
pipe = pipeline(
    "text-generation",
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    temperature=0.5,
    max_new_tokens=100
)

llm = HuggingFacePipeline(pipeline=pipe)

model = ChatHuggingFace(llm=llm)

res = model.invoke("What is the capital of Telangana")

print(res.content)