from fastapi import FastAPI, HTTPException, Request
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

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

@app.post('/chat',
    summary="Chat com o modelo OpenAI",
    description="Endpoint para enviar uma mensagem para o modelo OpenAI e receber uma resposta.",
    tags=["Chat"]
)
async def chat(request: Request) -> dict:
    """Envia uma mensagem para o modelo OpenAI e recebe uma resposta."""
    try:
        data = await request.json()
        message = data.get("message")

        if not message:
            raise HTTPException(status_code=400, detail="Message is required")
        
        llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
        messages = [
            HumanMessage(content=f"{message}")
        ]

        response = llm.invoke(messages)
        
        print(f"Response: {response.content}")

        return {
            "status": "success",
            "response": response.content
        }
    except Exception as e: 
        raise HTTPException(
                status_code=500, 
                detail=f"Internal server error: {e}"
            )
