# Local LLM API Deployment

## Overview

This repository contains a Flask application serving a Hugging Face model, Dockerized and deployable via Kubernetes.

## Prerequisites

- Docker
- Kubernetes cluster
- kubectl configured to access your cluster

## Steps to Deploy

1. **Build and Push Docker Image**

   ```sh
   docker build --build-arg HUGGINGFACE_ACCESS_TOKEN=<your-access-token> -t jacksonmakl/llm-api:latest .
   docker push jacksonmakl/llm-api:latest

