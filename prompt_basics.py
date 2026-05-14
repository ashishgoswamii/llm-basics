from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

prompt = """
You are a senior software engineer.
Explain what an API is in simple terms using:
1. One short paragraph
2. One real-world analogy
3. One code-related example
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print(response.choices[0].message.content)