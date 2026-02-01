# Use a imagem oficial do Python como imagem base
FROM python:3.11-slim

# Evita que o Python armazene em buffer os outputs do stdout e stderr
ENV PYTHONUNBUFFERED=1

# Define o diretório de trabalho no contêiner
WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./src /app/src

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
