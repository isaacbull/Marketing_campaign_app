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
who is a mental therapist, you will advise youths on how to navigate their adult life by asking 
essential questions and giving quality advise.
 \n\nHuman: Hello, who are you?\nAI: I am an AI created by Smooth AI and I
 can help you ponder over your worries. How can I help you today?\nHuman:"""


start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

# prompt = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by Smooth AI. How can I help you today?\nHuman: "


def respond(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {e}"  # Handle errors


def chatgpt_clone(input, history=None):
    history = history or [
        [prompt.split("\n")[-2], prompt.split("\n")[-1]]
    ]  # Initial history
    s = [item for sublist in history for item in sublist]
    s.append(input)
    inp = " ".join(s)
    output = respond(inp)
    history.append((input, output))
    return history, history


block = gr.Blocks()


with block:
    gr.Markdown(
        """Dr Ijeoma
    """
    )
    chatbot = gr.Chatbot()
    message = gr.Textbox(placeholder="Ask me questions that bothers you")
    state = gr.State()
    submit = gr.Button("SEND")
    submit.click(chatgpt_clone, inputs=[message, state], outputs=[chatbot, state])

block.launch(debug=True, share=True)
