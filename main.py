import os
from dotenv import load_dotenv, dotenv_values
import google.generativeai as genai
import gradio as gr


load_dotenv()


def load_gemini_model():
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])
    model = genai.GenerativeModel("gemini-1.5-flash")
    return model


model = load_gemini_model()
prompt = """You are a travel advisor, who helps users plan travel. you will ask user essential 
questions like: how much is your budget, how long would you like to travel for, how far would
you like to travel for."""


def respond(prompt, history):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {e}"  # Handle errors


demo = gr.ChatInterface(
    respond,
    analytics_enabled=True,
    submit_btn="Ask Dr Ijeoma",
    theme="soft",
    title="Dr Ijeoma",
    description="This is a chatbot that helps you plan your travel",
)

if __name__ == "__main__":
    demo.launch(debug=True, inbrowser=True, share=True)
