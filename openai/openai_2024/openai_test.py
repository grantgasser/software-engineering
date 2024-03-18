from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=[
        {"role": "user", "content": "How to install jupyter in a python venv"}
    ]
)

print(completion.choices[0].message)