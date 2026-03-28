from openai import OpenAI
from dotenv import load_dotenv

#Cargar variables de entorno
load_dotenv()

def openAIBasic(prompt):
    client = OpenAI()
    response = client.responses.create(
            model="gpt-5.4",
            input=prompt
        )
    return response.output_text

# response = openAIBasic('Dime cual es tu nombre')

# print(response)

