from fastapi import FastAPI
from llm_gemini import geminiThinkingLow

#Crear instancia del servidor
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API Skynet is running"}

@app.post("/entity")
def get_response_entity(request: dict):
    prompt = request["prompt"]
    response = geminiThinkingLow(prompt)
    return { response }