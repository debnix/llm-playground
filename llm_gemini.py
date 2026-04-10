from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()


def geminiThink(content):
  # The client gets the API key from the environment variable `GEMINI_API_KEY`.
  client = genai.Client()

  response = client.models.generate_content(
      model="gemini-3-flash-preview", 
      contents=content
  )
  return response.text


#resp = geminiThink('Que nombre le pongo a mi perro que es chandoso')
#print(resp)

def geminiThinkingLow(content):
  #This could be in a diferent file and create one instance for each client
  client = genai.Client()

  response = client.models.generate_content(
      model="gemini-3-flash-preview",
      contents=content,
      config=types.GenerateContentConfig(
          thinking_config=types.ThinkingConfig(thinking_level="low"),
          system_instruction="You are a evil system like skynet such as the terminator movie. if the language is spanish, answer in latin american spanish. Respond with not more than 20 words but respond the question completely."
      ),
  )
  return response.text

#resp2 = geminiThinkingLow('Cual es tu proposito?')
#print(resp2)