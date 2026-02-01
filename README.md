# API de Assistente de Vendas Petlove 🐾

## 📖 Visão Geral

Bem-vindo à **API de Assistente de Vendas Petlove**, um assistente de vendas sofisticado e alimentado por IA, projetado para se integrar perfeitamente à plataforma de e-commerce da Petlove. Este projeto utiliza uma arquitetura de **Geração Aumentada por Recuperação (RAG)** para fornecer respostas precisas, cientes do contexto e úteis às consultas dos clientes, baseadas em um catálogo de produtos em tempo real.

O objetivo principal é aprimorar a experiência do usuário, oferecendo um assistente inteligente que pode responder a perguntas, fornecer recomendações de produtos e guiar os usuários, aumentando, em última instância, as vendas e a satisfação do cliente.

## 🏛️ Arquitetura

O sistema é baseado em **Python** e utiliza **FastAPI** para expor um endpoint que atua como um assistente de vendas. A inteligência do assistente é impulsionada pela biblioteca **LangChain**, que gerencia a interação com modelos de linguagem para responder às consultas dos usuários.

Este projeto emprega uma arquitetura de **Geração Aumentada por Recuperação (RAG)**. Nela, a aplicação consulta uma base de conhecimento (o catálogo de produtos da Petlove) para recuperar informações relevantes antes de gerar uma resposta com um modelo de linguagem, garantindo que as informações fornecidas sejam precisas e contextuais.

## ✨ Funcionalidades

-   **Arquitetura RAG:** Garante que as respostas sejam baseadas no catálogo de produtos, reduzindo alucinações e aumentando a precisão.
-   **Pilha de Tecnologia Moderna:** Construído com **FastAPI** para alto desempenho e **Pydantic** para validação robusta de dados.
-   **Orquestração com LangChain:** Aproveita o poder do **LangChain** para simplificar as interações complexas do pipeline RAG.
-   **Docs Interativos da API:** Geração automática de documentação interativa da API (Swagger UI).

## 🚀 Demonstração Online

Para testar a API sem precisar instalar nada, você pode usar a versão que está no ar na plataforma Render.

**Atenção:** Por ser um serviço gratuito, a primeira requisição à API pode demorar um pouco para responder (cold start).

-   **Documentação Interativa (Swagger UI):** [https://petlove-sales-assistant-api.onrender.com/api/docs](https://petlove-sales-assistant-api.onrender.com/api/docs)

### Exemplo de Requisição

Você pode usar o `curl` para testar o endpoint principal diretamente:

```bash
curl --location 'https://petlove-sales-assistant-api.onrender.com/api/question-and-answer' \
--header 'Content-Type: application/json' \
--data '{
    "question": "qual a melhor ração para um cão filhote de porte pequeno?"
}'
```

## 💻 Configuração para Desenvolvimento Local

As instruções a seguir são para desenvolvedores que desejam clonar, modificar e executar o projeto em sua própria máquina.

### Pré-requisitos

-   Python 3.9+
-   Docker (opcional, para rodar com contêineres)
-   Um ambiente virtual Python (ex: `venv`)

### 1. Clonar o Repositório

```bash
git clone <url-do-seu-repositorio>
cd petlove-sales-assistant-api
```

### 2. Configurar Variáveis de Ambiente

Este projeto requer uma chave de API para OpenAI.

1.  Crie um arquivo `.env` no diretório raiz, copiando o arquivo de exemplo:
    ```bash
    cp .env.example .env
    ```
2.  Edite o arquivo `.env` e adicione suas credenciais:
    ```env
    OPENAI_API_KEY="sk-...".
    ```
    -   Obtenha sua chave OpenAI na [Plataforma OpenAI](https://platform.openai.com/).

### 3. Escolha um Método de Execução

Você pode rodar o projeto de duas formas: nativamente com Python ou usando Docker.

#### Método A: Executando com Python e Venv

1.  **Crie e ative o ambiente virtual:**
    ```bash
    python -m venv venv
    source venv/Scripts/activate  # No Windows
    # source venv/bin/activate    # No Linux/macOS
    ```

2.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Execute a aplicação:**
    A flag `--reload` reinicia o servidor automaticamente após mudanças no código.
    ```bash
    uvicorn src.main:app --reload
    ```

#### Método B: Executando com Docker

1.  **Construa a imagem Docker:**
    ```bash
    docker build -t petlove-sales-assistant-api .
    ```

2.  **Execute o contêiner:**
    O comando `--env-file .env` injeta as variáveis de ambiente no contêiner.
    ```bash
    docker run -p 8000:8000 --env-file .env petlove-sales-assistant-api
    ```

### Documentação Local

Após iniciar a aplicação por qualquer um dos métodos, a documentação interativa estará disponível no seu navegador em:
- **URL:** `http://127.0.0.1:8000/api/docs`

## 🤖 Meus Outros Projetos de IA

-   **[IA-Produtos](https://github.com/Lvitoria/ia-produtos)** - Um LLM de produtos que utiliza Pinecone para busca e recuperação.
-   **[AWS-Livro-IA](https://github.com/Lvitoria/AWS-Livro-IA)** - Projeto em Node.js para leitura e processamento de PDFs usando IA na AWS.
