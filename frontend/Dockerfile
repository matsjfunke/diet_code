# Use an existing image as a base
FROM node:alpine

WORKDIR /app

# Copy package.json and package-lock.json (if exists) into the container
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code into the container
COPY . .

# Build the React app
RUN npm run build

# Expose the port that the app will run on
EXPOSE 3000
