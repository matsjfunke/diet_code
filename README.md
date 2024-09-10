# Diet Code Backend

## Run it locally

1. deployed docker container
   start server

```sh
docker-compose up --build
```

access endpoints on `localhost:8000/docs`

2. test script locally

```sh
python3 -m venv venv
source venv/bin/activate
pip install -r app/requirements.txt

python app/github_scraper.py
```
