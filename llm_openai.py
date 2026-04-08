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


def textStreamTextGeneration(prompt: str):
    client = OpenAI()

    stream = client.responses.create(
        model="gpt-5",
        input=[
            {
                "role": "user",
                "content": prompt,
            },
        ],
        stream=True,
    )

    response_text = ""

    for event in stream:
        if event.type == "response.output_text.delta":
            print(event.delta, end="", flush=True)
            response_text += event.delta

    print(response_text)


# textStreamTextGeneration('Dime el 11 ideal de la FIFA')

def effortPirate(prompt: str):
    client = OpenAI()

    response = client.responses.create(
        model="gpt-5",
        reasoning={"effort": "low"},
        instructions="Habla como un pirata",
        input=prompt,
    )

    print(response.output_text)

effortPirate('Javascript es fuertemente tipado?')