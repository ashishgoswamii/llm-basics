from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv()

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": "You extract information and return only valid JSON."
        },
        {
            "role": "user",
            "content": "Extract name, role, and location from this sentence: Ashish is a Software Engineer based in Pune."
        }
    ],
    response_format={
        "type": "json_object"
    }
)

data = response.choices[0].message.content

print(data)

parsed_data = json.loads(data)

print("Name:", parsed_data.get("name"))
print("Role:", parsed_data.get("role"))
print("Location:", parsed_data.get("location"))