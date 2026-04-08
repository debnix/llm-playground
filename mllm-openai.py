from openai import OpenAI
from dotenv import load_dotenv

#Cargar variables de entorno
load_dotenv()

#Crear instancia del cliente
client = OpenAI()

#Crear respuesta
response = client.responses.create(
    model="gpt-5",
    input=[
        {
            "role": "user",
            "content": [
                {
                    "type": "input_text",
                    "text": "Como se llama ese arquero y de que equipo es?",
                },
                {
                    "type": "input_image",
                    "image_url": "https://www.acordantioquia.com/wp-content/uploads/2020/08/Ren%C3%A9-Huigita-Colprensa.jpg"
                }
            ]
        }
    ]
)

print(response.output_text)