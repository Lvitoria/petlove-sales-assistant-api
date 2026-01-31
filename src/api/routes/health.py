from fastapi import APIRouter

router = APIRouter()

@router.get(
    "/health",
    summary="Verificação de saúde da API",
    description="Endpoint para verificar se a API está funcionando corretamente.",
    tags=["Health Check"]
)
def health_check():
    """Verifica o status da API."""
    return {"status": "ok"}
