from fastapi import FastAPI
from llm_gemini import geminiThinkingLow
from fastapi.middleware.cors import CORSMiddleware


#Crear instancia del servidor
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "API Skynet is running"}

@app.post("/entity")
def get_response_entity(request: dict):
    prompt = request["prompt"]
    response = geminiThinkingLow(prompt)
    return { response }