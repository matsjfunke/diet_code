from fastapi import FastAPI, HTTPException

from .contributor_scraper import ScraperException, extract_gh_repo_id, scrape_gh_deletion_ranking

app = FastAPI()


@app.get("/deletion-ranking")
async def return_ranking(gh_url: str):
    try:
        repo_id = extract_gh_repo_id(gh_url)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    try:
        deletion_ranking = scrape_gh_deletion_ranking(repo_id=repo_id)
    except ScraperException as e:
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")

    return deletion_ranking


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
