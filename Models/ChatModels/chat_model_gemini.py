from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
llm = ChatGoogleGenerativeAI(model="gemini-3.8-flash",temperature=1.8
)
result = llm.invoke("Generate a poem on rohit sharma of 4 lines ?")
print(result.content[0]["text"])

#With temperature=0

#With effortless grace, he pulls the ball away,  
#The fearless Hitman who rules the field of play.  
#Record double-centuries etched into his name,  
#A champion captain who conquered cricket’s game.



#With temperature=1.8

#With effortless grace and an elegant stride,  
#He pulls every ball with unmatched ease and pride.  
#A leader and legend, the ‘Hitman’ supreme,  
#Rohit carries the heart of a billion-strong dream.