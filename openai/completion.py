import openai
import config

openai.api_key = config.API_KEY

response = openai.Completion.create(model="text-davinci-003", prompt="Country roads, take me home", temperature=0, max_tokens=20)

print(response.choices[0].text)