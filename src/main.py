from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from http import HTTPStatus
from dotenv import load_dotenv
import uvicorn

from src.api.routes import health, chat

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

if __name__ == "__main__":
    uvicorn.run("src.main:app", host="127.0.0.1", port=8000, reload=True)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    """
    Handler customizado para erros de validação do Pydantic, retornando mensagens em português.
    """
    errors = []
    for error in exc.errors():
        field = ".".join(map(str, error["loc"][1:]))
        msg = error["msg"]
        
        if "field required" in msg:
            translated_msg = f"Campo '{field}' é obrigatório."
        elif "value is not a valid string" in msg:
            translated_msg = f"Campo '{field}' deve ser uma string válida."
        else:
            translated_msg = f"Erro no campo '{field}': {msg}"
            
        errors.append({"campo": field, "mensagem": translated_msg})
        
    return JSONResponse(
        status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
        content={"detail": "Erro de validação", "erros": errors},
    )

app.include_router(health.router, prefix="/api/v1")
app.include_router(chat.router, prefix="/api/v1")
