FROM python:3.12-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY ./src .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]