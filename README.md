# Diet Code

a web app that ranks developers productivity based on amount of deletions and spreads the gospel of deleting code
avnoan
## Run locally

```sh
docker-compose up --build
```

**Backend:**

- access localhost:8000/docs for fastapi dashboard -> for testing specific endpoints
- access localhost:8000/openapi.json to generate the OpenAPI documentation

**Frontend:**

- access localhost:3000 and interact with the UI

## Deployment on Server


```sh
# rsync files to server
cd diet-code
rsync -av --exclude-from='.rsyncignore' -e "ssh -i ~/.ssh/<private-key>" . <user>@<ip-address>:diet-code

# ssh into server

ssh -i ~/.ssh/diet-code root@<ip-address>

# use the deployment script to automate docker & docker-compose installation, and starting docker containers
chmod +x deploy.sh
./deploy.sh
```

go to https://diet-code.dev/taste and try to taste the diet code ranking for any public repo with contributors (try: https://github.com/matsjfunke/psychopy-install-setup)

to stop containers use:
```sh
docker-compose -f docker-compose.prod.yml down
```

### Deploy on VPS with another webapp running

to deploy diet-code along with another webapp on one server use `docker-compose.prod.shared.yml`

```sh
# Build the images
docker-compose -f docker-compose.prod.shared.yml build

# Connect Traefik to the diet-code network
# Network name is prefixed with directory name (diet-code_) by Docker Compose
docker network connect diet-code_diet-code-web traefik

# Start the services
docker-compose -f docker-compose.prod.shared.yml up -d
```
