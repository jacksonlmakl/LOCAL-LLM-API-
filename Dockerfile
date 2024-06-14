FROM python:3.9-slim

# Define build argument
ARG HUGGINGFACE_ACCESS_TOKEN

# Set environment variable from the build argument
ENV HUGGINGFACE_ACCESS_TOKEN=${HUGGINGFACE_ACCESS_TOKEN}

WORKDIR /app

COPY app/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

CMD ["python", "app.py"]

