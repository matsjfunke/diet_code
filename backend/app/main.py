import logging

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from github_scraper import extract_gh_owner_repo, scrape_gh_contribution_data

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

origins = [
    "http://localhost:3000",
]
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])


@app.get("/gh-deletion-ranking")
async def return_ranking(url: str):
    try:
        owner, repo = extract_gh_owner_repo(url)
    except ValueError as e:
        logger.error(f"Error extracting owner and repo: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

    try:
        deletion_ranking = scrape_gh_contribution_data(owner=owner, repo=repo)
    except Exception as e:
        logger.error(f"Unexpected error scraping data: {str(e)}")
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")

    logger.info(f"Returned ranking for: {url}")
    return deletion_ranking


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
