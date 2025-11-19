# 1. Escolhemos o Sistema Operacional base (Linux leve com Python)
FROM python:3.13-slim

# 2. Definimos que não queremos arquivos temporários de python (.pyc)
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 3. Definimos a pasta de trabalho dentro do container
WORKDIR /app

# 4. Instalamos as dependências do sistema necessárias para o PostgreSQL
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libpq-dev \
    && apt-get clean

# 5. Instalamos o Poetry
RUN pip install poetry

# 6. Copiamos os arquivos de requisitos
COPY pyproject.toml poetry.lock ./

# 7. Instalamos as dependências do projeto (sem criar venv, pois o container JÁ É isolado)
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-root

# 8. Copiamos todo o resto do código para dentro do container
COPY . .

# 9. Comando padrão (será substituído pelo docker-compose, mas é bom ter)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]