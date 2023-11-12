# docker run -p 8000:8000 -it homework_03
FROM python:3.11.6-slim-bookworm

WORKDIR /app

RUN pip install --upgrade pip setuptools "poetry==1.7.0"
RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./
RUN poetry install

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

EXPOSE 8000