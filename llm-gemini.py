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
  client = genai.Client()

  response = client.models.generate_content(
      model="gemini-3-flash-preview",
      contents=content,
      config=types.GenerateContentConfig(
          thinking_config=types.ThinkingConfig(thinking_level="low")
      ),
  )
  return response.text

resp2 = geminiThinkingLow('Cual es el proposito de la vida?')
print(resp2)