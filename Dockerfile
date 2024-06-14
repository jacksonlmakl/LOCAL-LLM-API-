FROM python:3.9-slim

ENV HUGGINGFACE_ACCESS_TOKEN=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

WORKDIR /app

COPY app/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

CMD ["python", "app.py"]

