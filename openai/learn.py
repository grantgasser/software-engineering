import openai
import config

openai.api_key = config.API_KEY

response = openai.Embedding.create(
  input="this is great!",
  model="text-embedding-ada-002"
)

print(response)