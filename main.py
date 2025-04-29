import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

response = client.completions.create(
    model="code-davinci-002",
        prompt="def factorial(n):",
            max_tokens=100
            )

            print(response.choices[0].text.strip())