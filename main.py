from fastapi import FastAPI
from llm_openai import openAIBasic

#Crear instancia del servidor
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/assistant/{prompt}")
def get_assistant(prompt: str):
    response = openAIBasic(prompt)
    return {"assistant": response}