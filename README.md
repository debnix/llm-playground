# llm-playground

A playground project to experiment with LLM integrations using a FastAPI backend and a frontend app.

## Requirements

- Python (for the API)
- Node.js + npm or yarn (for the frontend)

## Setup

> **Note:** You need to create a `.env` file with your Gemini or OpenAI API key.
And you need install fastapi dependency

Example:

```env
# Use one of these depending on your implementation
GEMINI_API_KEY=your_api_key_here
OPENAI_API_KEY=your_api_key_here
```

## Run project

- Server: fastapi dev
- Frontend: npm run dev or yarn dev