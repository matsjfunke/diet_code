from fastapi import FastAPI, HTTPException

from .github_scraper import extract_gh_owner_repo, scrape_gh_contribution_data

app = FastAPI()


@app.get("/deletion-ranking")
async def return_ranking(url: str):
    try:
        owner, repo = extract_gh_owner_repo(url)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    try:
        deletion_ranking = scrape_gh_contribution_data(owner=owner, repo=repo)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")

    return deletion_ranking


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
