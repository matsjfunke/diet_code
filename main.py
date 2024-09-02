"""
matsjfunke
"""

from fastapi import FastAPI

from contributor_scraper import extract_gh_repo_id, scrape_gh_deletion_ranking

app = FastAPI()


@app.get("/deletion-ranking")
async def return_ranking(gh_url: str):
    repo_id = extract_gh_repo_id(gh_url)
    return scrape_gh_deletion_ranking(repo_id)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
