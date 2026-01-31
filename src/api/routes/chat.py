from fastapi import APIRouter, HTTPException
from src.schema.chat import ChatMessage
from src.services.chat_service import ChatService

router = APIRouter()

@router.post(
    '/question-and-answer',
    summary="Chat com o modelo OpenAI",
    description="Endpoint para enviar uma mensagem para o modelo OpenAI e receber uma resposta.",
    tags=["Question and Answer"]
)
async def chat(
    chat_message: ChatMessage
) -> dict:
    """
    Envia uma mensagem para o modelo OpenAI e recebe uma resposta.
    """
    try:
        chat_service = ChatService()
        response_content = chat_service.get_response(chat_message.question)
        return {
            "response": response_content
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Internal server error: {e}"
        )
