#!/bin/bash

set -e

command_exists() {
  command -v "$1" >/dev/null 2>&1
}

echo "Updating system packages..."
sudo apt-get update -y

if ! command_exists docker; then
  echo "Docker not found. Installing Docker..."
  sudo apt-get install -y docker.io
fi

if ! command_exists docker-compose; then
  echo "Docker Compose not found. Installing Docker Compose..."
  sudo apt-get install -y docker-compose
fi

echo "Stopping and removing existing project containers..."
docker-compose -f docker-compose.prod.yml down --remove-orphans

echo "Stopping all Docker containers..."
docker stop $(docker ps -aq) 2>/dev/null || true

echo "Pruning unused Docker resources..."
docker system prune -f

if ! docker network ls | grep -q "web"; then
  echo "Creating Docker network 'web'..."
  docker network create web
fi

echo "Pulling the latest images..."
docker-compose -f docker-compose.prod.yml pull

echo "Building and starting the services..."
docker-compose -f docker-compose.prod.yml up --build -d

echo "Deployment complete."
