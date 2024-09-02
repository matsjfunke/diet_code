import json
import time
from typing import Dict, List

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options


def scrape_repo_deletion_ranking(repo_id: str) -> List[Dict[str, str]]:
    """
    param: str -> repo_owner/repo_name
    retuns json -> ranking of deletions
    """
    # Set up options for Firefox
    options = Options()
    options.headless = True

    # Initialize the WebDriver
    driver = webdriver.Firefox(options=options)
    url = f"https://github.com/{repo_id}/graphs/contributors?from=2023-08-27&to=2024-09-02&type=d"
    driver.get(url)

    # Wait for the page to load
    time.sleep(5)

    deletion_ranking = []
    try:
        contributors = driver.find_elements(By.CSS_SELECTOR, "li.contrib-person")

        for contributor in contributors:
            # Extract rank
            rank_element = contributor.find_element(By.CSS_SELECTOR, "span.f5.text-normal.color-fg-muted.float-right")
            rank = rank_element.text.replace("#", "").strip() if rank_element else "N/A"

            # Extract name
            name_element = contributor.find_element(By.CSS_SELECTOR, "a.text-normal")
            name = name_element.text if name_element else "N/A"

            # Extract deletions
            deletions_element = contributor.find_element(By.CSS_SELECTOR, "span.color-fg-danger.text-normal")
            deletions = deletions_element.text.replace("--", "").strip() if deletions_element else "N/A"

            # Append data to list
            deletion_ranking.append({"rank": rank, "name": name, "deletions": deletions})

    finally:
        driver.quit()

    return deletion_ranking


if __name__ == "__main__":
    deletion_ranking = scrape_repo_deletion_ranking(repo_id="rememberry-io/rememberry")

    # Write data to JSON file
    with open("deletion-ranking.json", "w") as file:
        json.dump(deletion_ranking, file, indent=4)

    import subprocess
    subprocess.run(["cat", "deletion-ranking.json"])
