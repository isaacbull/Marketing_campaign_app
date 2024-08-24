import os
from dotenv import load_dotenv, dotenv_values


load_dotenv()

print(os.getenv("GEMINI_API_KEY"))
print("hello world")


def add(x, y):
    return x + y
