#!/bin/bash

# Update and install Docker and Docker Compose if needed
sudo apt-get update
sudo apt-get install -y docker docker-compose

# Create Docker network if it doesn't exist
if ! docker network ls | grep -q "web"; then
  docker network create web
fi

# Pull the latest images and build the containers
docker-compose -f docker-compose.prod.yml pull
docker-compose -f docker-compose.prod.yml build

# Start the services
docker-compose -f docker-compose.prod.yml up --build --remove-orphans -d

echo "Deployment complete."
