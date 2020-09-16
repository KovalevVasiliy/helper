# Base image
# Build and push to dockerhub, for other images to inherit from

FROM python:3.8 as base

ENV POETRY_VERSION=1.0.2

ENV PIP_DISABLE_PIP_VERSION_CHECK=on
ENV PIP_NO_CACHE_DIR=off
ENV PYTHONDONTWRITEBYTECODE=on
ENV PYTHONFAULTHANDLER=on
ENV PYTHONUNBUFFERED=on
ENV PYTHONPATH=/opt/app

WORKDIR /code

COPY /src .

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN pip install "poetry==$POETRY_VERSION" \
    && poetry config virtualenvs.create false

COPY pyproject.toml .
RUN poetry install
CMD [ "python3.8", "./server.py" ]
