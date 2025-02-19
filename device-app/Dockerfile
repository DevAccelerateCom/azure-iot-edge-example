FROM python:3.11-slim

WORKDIR /app
COPY main.py .
COPY requirements.txt .

# Installa le dipendenze
RUN pip install -r requirements.txt

CMD ["python", "main.py"]