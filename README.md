# Secret Share App

A temporary secret sharing application inspired by tools like Yopass.

Unlike the original Yopass architecture, this project does not implement zero-knowledge encryption. Secrets are processed and stored server-side using Flask and SQLite, meaning the backend can access the secret contents in plain text.

The main goal of the project is to explore infrastructure, containerization, orchestration and deployment concepts rather than advanced cryptographic security mechanisms.

This project was developed as part of a Distributed Computing assignment using:

- Python 3.12
- Flask
- SQLite
- Docker
- Docker Compose
- Kubernetes
- Minikube

The application allows users to:

- Create temporary secrets
- Share secrets using unique URLs
- Configure expiration times
- Open secrets only once
- Automatically expire secrets

# Features

- Temporary secret sharing
- One-time secret access
- Expiration system
- SQLite persistence
- Docker containerization
- Docker Compose orchestration
- Kubernetes deployment with Minikube
- Persistent storage using Docker volumes

# Project Structure

```text
secret-share-app/
│
├── app/
│   ├── static/
│   ├── templates/
│   ├── app.py
│   ├── database.py
│   ├── routes.py
│   ├── services.py
│   ├── schema.sql
│   └── models/
│
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .dockerignore
├── .gitignore
└── README.md
```

# Running the Project Locally (Flask)

git clone <repository-url>
cd secret-share-app
python3 -m venv venv
source venv/bin/activate (linux)
pip install -r requirements.txt
python app/app.py
http://127.0.0.1:5000

# Running with Docker

docker build -t secret-share-app:latest . (build the Docker image)
docker run \
--name secret-share-container \
-p 5000:5000 \
secret-share-app:latest
http://127.0.0.1:5000

# Running with Docker Compose

docker compose up
docker compose down (to stop the application)

Docker Compose automatically:

Creates the container
Creates the network
Mounts persistent volumes
Exposes the application port

# Running with Kubernetes (Minikube)

minikube start --driver=docker
docker build -t secret-share-app:latest .
minikube image load secret-share-app:latest
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl get pods
kubectl get services
minikube service secret-share-service

# Persistence

The application uses:

SQLite for storing secrets
Docker volumes for persistent storage
Kubernetes volumes for container storage

# Security Notes

This project was developed for educational purposes.

Current security features include:

Unique UUID secret URLs
Optional one-time secret access
Secret expiration system

Future improvements may include:

Client-side encryption
HTTPS/TLS
End-to-end encryption
Rate limiting
Authentication system

# Learning Goals

This project was created to practice:

Backend development with Flask
Docker containerization
Docker Compose orchestration
Kubernetes deployments
Distributed computing concepts
Persistent storage management
Infrastructure troubleshooting
