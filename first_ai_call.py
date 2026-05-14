from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": "Explain AI in simple terms."
        }
    ]
)
# Print response.usage to see how many tokens (word-pieces) were used.
print(response.usage)
print(response.choices[0].message.content)