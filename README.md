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
chmod +x deploy.sh
./deploy.sh
```

use `docker-compose -f docker-compose.prod.yml down` to stop containers
