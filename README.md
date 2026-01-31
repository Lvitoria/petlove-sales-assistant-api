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

A aplicação estará disponível em `http://127.0.0.1:5000/`.
