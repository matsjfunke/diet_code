import json
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

# Set up options for Firefox
options = Options()
options.headless = True

# Initialize the WebDriver
driver = webdriver.Firefox(options=options)
url = "https://github.com/rememberry-io/rememberry/graphs/contributors?from=2023-08-27&to=2024-09-02&type=d"
driver.get(url)

# Wait for the page to load
time.sleep(5)

# Extract contributor data
contributors_data = []
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
        contributors_data.append({"rank": rank, "name": name, "deletions": deletions})

finally:
    driver.quit()

# Write data to JSON file
with open("deletion-ranking.json", "w") as file:
    json.dump(contributors_data, file, indent=4)
