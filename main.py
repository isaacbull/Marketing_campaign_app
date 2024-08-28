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
prompt = """You will be generating advises for whenever you are prompted like a chatbot
who is a travel planner, you will advise me on travel and help me plan their travels, asking
essential questions and giving quality advise."""


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
