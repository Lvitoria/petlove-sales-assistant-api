from pydantic import BaseModel, Field

class ChatMessage(BaseModel):
    question: str = Field(..., description="A pergunta do cliente para o assistente de vendas.", min_length=1, max_length=200)


