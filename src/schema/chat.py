from pydantic import BaseModel, Field

class ChatMessage(BaseModel):
    question: str = Field(..., description="A pergunta do cliente para o assistente de vendas.", min_length=1, max_length=200)

class ChatResponse(BaseModel):
    response: str = Field(..., description="A resposta do assistente de vendas.")

class HealthResponse(BaseModel):
    status: str = Field(..., description="O status da API.")


