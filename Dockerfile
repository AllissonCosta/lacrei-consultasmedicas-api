# Escolhe o Sistema Operacional base (Linux leve com Python)
FROM python:3.13-slim

# Defi que não queremos arquivos temporários de python (.pyc)
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Defi a pasta de trabalho dentro do container
WORKDIR /app

# Instalamos as dependências do sistema necessárias para o PostgreSQL
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libpq-dev \
    && apt-get clean

# Instala o Poetry
RUN pip install poetry

# Copia os arquivos de requisitos
COPY pyproject.toml poetry.lock ./

# Instala as dependências do projeto (sem criar venv)
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-root

# Copia todo o resto do código para dentro do container
COPY . .

# Comando padrão (será substituído pelo docker-compose)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]