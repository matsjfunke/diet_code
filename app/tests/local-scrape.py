import json
import re
import time
from typing import Dict, List

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By


class ScraperException(Exception):
    """Custom exception for scraper errors."""

    pass


def extract_gh_repo_id(gh_url: str) -> str:
    pattern = r"https://github\.com/([^/]+)/([^/]+)"
    match = re.search(pattern, gh_url)

    if match:
        return f"{match.group(1)}/{match.group(2)}"
    raise ValueError("Invalid GitHub URL format")


def scrape_gh_deletion_ranking(repo_id: str) -> List[Dict[str, str]]:
    """
    param: str -> repo_owner/repo_name
    retuns json -> ranking of deletions
    """
    options = ChromeOptions()
    options.add_argument("--headless=new")

    try:
        driver = webdriver.Chrome(options=options)
    except WebDriverException as e:
        raise ScraperException(f"Failed to initialize the web driver: {str(e)}")

    url = f"https://github.com/{repo_id}/graphs/contributors"
    driver.get(url)

    # Wait for the page to load
    time.sleep(5)

    deletion_ranking = []
    try:
        contributors = driver.find_elements(By.CSS_SELECTOR, "li.contrib-person")
        if not contributors:
            raise ScraperException(f"No contributors found for repository: {repo_id}")

        for contributor in contributors:
            try:
                rank_element = contributor.find_element(By.CSS_SELECTOR, "span.f5.text-normal.color-fg-muted.float-right")
                rank = rank_element.text.replace("#", "").strip() if rank_element else "N/A"

                name_element = contributor.find_element(By.CSS_SELECTOR, "a.text-normal")
                name = name_element.text if name_element else "N/A"

                deletions_element = contributor.find_element(By.CSS_SELECTOR, "span.color-fg-danger.text-normal")
                deletions = deletions_element.text.replace("--", "").strip() if deletions_element else "N/A"

                additions_element = contributor.find_element(By.CSS_SELECTOR, "span.color-fg-success.text-normal")
                additions = additions_element.text.replace("++", "").strip() if deletions_element else "N/A"

                deletion_ranking.append({"rank": rank, "name": name, "deletions": deletions, "additions": additions})
            except NoSuchElementException as e:
                raise ScraperException(f"Failed to scrape contributor data: {str(e)}")
    finally:
        driver.quit()

    return deletion_ranking


if __name__ == "__main__":
    import argparse
    import subprocess

    parser = argparse.ArgumentParser(description="Process a GitHub URL.")
    parser.add_argument("--url", type=str, required=True, help="The GitHub repository URL")

    args = parser.parse_args()

    gh_url = args.url
    repo_id = extract_gh_repo_id(gh_url)

    deletion_ranking = scrape_gh_deletion_ranking(repo_id=repo_id)

    # Write data to JSON file
    with open("deletion-ranking.json", "w") as file:
        json.dump(deletion_ranking, file, indent=4)

    subprocess.run(["cat", "deletion-ranking.json"])
