from groq import Groq

client = Groq(
    api_key="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",
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a Virtual Assistant named Jarvis skilled in general tasks like Alexa and Google Cloud" 
        },
        {
            "role": "user",
            "content": "Explain the importance of fast language models",
        }
    ],
    model="llama3-8b-8192",
)

print(chat_completion.choices[0].message.content)