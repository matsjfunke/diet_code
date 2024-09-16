# Diet Code

a web app that ranks developers productivity based on amount of deletions and spreads the gospel of deleting code

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
