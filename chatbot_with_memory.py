from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()


print("AI Chatbot with memory started. Type 'exit' to quit.")

messages = [
    {
        "role": "system",
        "content": "You are a helpful AI assistant for a software engineer learning AI engineering."
    }
]

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    # Add the user's message to the history
    messages.append({"role": "user", "content": user_input})

    try:

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )

        reply = response.choices[0].message.content
        print("Bot:", reply)

        # Add the bot's reply so it remembers it next turn
        messages.append({"role": "assistant", "content": reply})
    except Exception as e:
        print("An error occurred:", str(e))
        messages.pop()  # remove the user message we just added, so retry works cleanly
