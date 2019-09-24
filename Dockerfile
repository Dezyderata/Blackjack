FROM python:3.6.8-slim

WORKDIR /app

COPY . /app

CMD ["python3", "game.py"]
