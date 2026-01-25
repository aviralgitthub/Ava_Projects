from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="<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>",
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message.content)