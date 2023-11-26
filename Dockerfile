FROM python:3.10-alpine

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

ENV PIP_NO_CACHE_DIR=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PIP_DEFAULT_TIMEOUT=100

ENV POETRY_VERSION=1.4.2
ENV POETRY_VIRTUALENVS_IN_PROJECT=true

WORKDIR /

COPY pyproject.toml poetry.lock ./
COPY main.py ./
COPY src ./src

RUN pip install "poetry==$POETRY_VERSION"
RUN poetry install --only main --no-interaction --no-ansi

CMD ["poetry", "run", "uvicorn", "--reload", "main:app", "--host", "0.0.0.0",  "--port", "5000"]







