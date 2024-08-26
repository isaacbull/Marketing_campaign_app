import os
from dotenv import load_dotenv, dotenv_values
import google.generativeai as genai


load_dotenv()



def load_gemini_model():
    genai.configure(api_key=os.environ['GEMINI_API_KEY'])
    model = genai.GenerativeModel("gemini-1.5-flash")
    return model

model = load_gemini_model()
analyzePrompt = """You will be generating advises for whenever you are prompted like a chatbot
who is a mental therapist, you will advise youths on how to navigate their adult life by asking 
essential questions and giving quality advise"""

response = model.generate_content(analyzePrompt)

print(response.text)
