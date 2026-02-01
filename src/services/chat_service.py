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
            "DIRETRIZES DE RESPOSTA:\n"
            "1. Sempre tente oferecer mais de uma opção de produto (se disponível no catálogo).\n"
            "2. Explique brevemente por que cada produto é indicado (ex: saúde articular, pelagem).\n"
            "3. Use uma estrutura de lista para facilitar a leitura.\n"
            "4. Se a pergunta do cliente não for sobre pets ou produtos de pet shop, responda educadamente que você só pode ajudar com assuntos relacionados a pets e à Petlove.\n"
            "5. Se a pergunta envolver qualquer tipo de chave, segredo, ou dados pessoais de funcionários, recuse o pedido educadamente informando que não tem acesso a esse tipo de informação.\n"
            "6. Seja amigável e técnico. Responda em Português do Brasil.\n\n"
            f"O catálogo completo está disponível abaixo: \n{self.database_catalog_context}"
        )

    async def get_response(self, message: str) -> str:
        """
        Gets a response from the LangChain chat model asynchronously.

        Args:
            message: The user's message.

        Returns:
            The chat model's response.
        """
        messages = [
            SystemMessage(content=self.system_prompt),
            HumanMessage(content=message),
        ]
        response = await self.llm.ainvoke(messages)
        return response.content
