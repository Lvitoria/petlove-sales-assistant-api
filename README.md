# API de Assistente de Vendas Petlove 🐾

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

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

## 🚀 Primeiros Passos

Siga estas instruções para configurar e executar o projeto localmente.

### Pré-requisitos

-   Python 3.9+
-   Um ambiente virtual ativo (por exemplo, `venv`)

### 1. Clonar o Repositório

```bash
git clone <url-do-seu-repositorio>
cd petlove-sales-assistant-api
```
opcional 
```bash
python -m venv venv
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

### 3. Instalar Dependências

Com seu ambiente virtual ativado, instale os pacotes necessários:

No bash com Windows (opcional caso tenha criado o venv):

```bash
source venv/Scripts/activate
```
instalando
```bash
pip install -r requirements.txt
```

### 4. Executar a Aplicação

Você pode executar a aplicação usando Uvicorn. A flag `--reload` permite o recarregamento automático para desenvolvimento.

```bash
uvicorn src.main:app --reload
```

A API estará disponível em `http://127.0.0.1:8000`.

## 📚 Documentação da API

Uma vez que a aplicação esteja em execução, você pode acessar a documentação interativa Swagger UI para explorar e testar os endpoints.

**Atenção:** Em ambientes de servidor gratuito, a primeira requisição à API pode demorar um pouco mais para responder (cold start).

-   **URL da Swagger UI:** [https://petlove-sales-assistant-api.onrender.com/api/v1/docs](https://petlove-sales-assistant-api.onrender.com/api/v1/docs)

*(Nota: Para desenvolvimento local, a documentação estará em `http://127.0.0.1:8000/api/v1/docs`)*

### Exemplo de Requisição

Aqui está um exemplo de como consultar o endpoint principal:

```bash
curl --location 'https://petlove-sales-assistant-api.onrender.com/api/question-and-answer' \
--header 'Content-Type: application/json' \
--data '{
    "question": "qual a melhor ração para um cão filhote de porte pequeno?"
}'
```

