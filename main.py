from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="Petlove Sales Assistant API",
    description="API for the Petlove Sales Assistant",
    version="1.0.0",
    openapi_url="/api/v1/openapi.json",
    docs_url="/api/v1/docs",
    redoc_url="/api/v1/redoc",
    openapi_tags=[
        {
            "name": "Health Check",
            "description": "Endpoints para verificar o status da API."
        },
        {
            "name": "Chat",
            "description": "Endpoints para enviar mensagens para o modelo OpenAI."
        }
    ]
)

@app.get("/health", 
    summary="Verificação de saúde da API",
    description="Endpoint para verificar se a API está funcionando corretamente.",
    tags=["Health Check"])
def health_check():
    """Verifica o status da API."""
    return {"status": "ok"}