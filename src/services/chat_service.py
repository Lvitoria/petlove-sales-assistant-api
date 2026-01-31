from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

class ChatService:
    """
    A chat service that uses the LangChain library.
    """
    def __init__(self, model: str = "gpt-3.5-turbo", temperature: float = 0):
        self.llm = ChatOpenAI(model=model, temperature=temperature)

    def get_response(self, message: str) -> str:
        """
        Gets a response from the LangChain chat model.

        Args:
            message: The user's message.

        Returns:
            The chat model's response.
        """
        messages = [
            SystemMessage(content="Você é um assistente de vendas da Petlove. Responda sempre em português do Brasil."),
            HumanMessage(content=message),
        ]
        response = self.llm.invoke(messages)
        return response.content
