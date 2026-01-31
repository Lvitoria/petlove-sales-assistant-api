from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

class ChatService:
    """
    A chat service that uses the LangChain library.
    """
    def __init__(self, model: str = "gpt-3.5-turbo", temperature: float = 0):
        self.llm = ChatOpenAI(model=model, temperature=temperature)

        with open("src/database/database.md", "r", encoding="utf-8") as f:
            self.database_catalog_context = f.read()

        self.system_prompt = (
            "Você é o especialista de vendas da Petlove. "
            "Sua missão é ajudar clientes a escolherem os melhores produtos para seus pets. "
            "Seja amigável, técnico quando necessário (citando benefícios de saúde) e foque no catálogo Petlove. "
            "Responda sempre em português do Brasil de forma concisa e útil."
            "Caso o cliente pergunte sobre um produto que não existe no catálogo, informe que não temos esse produto."
            "Caso o cliente pergunte outra coisa que não seja sobre o catálogo, informe que não entendo a pergunta e peça para ele reformular."
            "O catálogo completo está disponível abaixo: "
            f"O catálogo completo está disponível abaixo: \n{self.database_catalog_context}"
        )

    def get_response(self, message: str) -> str:
        """
        Gets a response from the LangChain chat model.

        Args:
            message: The user's message.

        Returns:
            The chat model's response.
        """
        messages = [
            SystemMessage(content=self.system_prompt),
            HumanMessage(content=message),
        ]
        response = self.llm.invoke(messages)
        return response.content
