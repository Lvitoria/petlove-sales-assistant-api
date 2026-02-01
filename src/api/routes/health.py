from fastapi import APIRouter
from src.schema.chat import HealthResponse

router = APIRouter()

@router.get(
    "/health",
    summary="Verificação de saúde da API",
    description="Endpoint para verificar se a API está funcionando corretamente.",
    tags=["Health Check"]
)
def health_check() -> HealthResponse:
    """Verifica o status da API."""
    return HealthResponse(status="ok")
