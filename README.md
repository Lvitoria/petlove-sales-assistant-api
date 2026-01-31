## Instruções de Instalação

Siga os passos abaixo para configurar e executar o projeto:

1. Crie um ambiente virtual:
    ```bash
    python -m venv venv
    ```
2. Ative o ambiente virtual:
    - No bash com Windows:
        ```bash
        source venv/Scripts/activate
        ```
    - No Windows:
        ```bash
        ./venv/Scripts/activate
        ```
    - No Linux/Mac:
        ```bash
        source venv/bin/activate
        ```
3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
4. Configure as variáveis de ambiente necessárias (exemplo no arquivo `.env.example`):
    ```bash
    cp .env.example .env
    ```
5. Caso queira sair 
    ```bash
    deactivate
    ```

A aplicação estará disponível em `http://127.0.0.1:8000/`.

## Rodando a Aplicação

Existem duas formas equivalentes para rodar a aplicação em modo de desenvolvimento (com reload automático):

1.  **Executando o script principal:**

    Este método é uma forma conveniente de iniciar o servidor Uvicorn, conforme configurado em `main.py`.

    ```bash
    python main.py
    ```

2.  **Usando o comando Uvicorn diretamente:**

    Esta é a forma padrão de executar aplicações FastAPI com Uvicorn.

    ```bash
    uvicorn main:app --reload
    ```

Em ambos os casos, a aplicação estará disponível em `http://127.0.0.1:8000/`.
