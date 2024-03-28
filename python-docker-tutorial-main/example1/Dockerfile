FROM python:3.9-slim

WORKDIR /app

COPY main.py .

RUN pip install --no-cache-dir requests beautifulsoup4 && \
    apt-get update && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

CMD ["python", "./main.py"]