import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

# Set up options for Firefox
options = Options()
options.headless = False  # Set to True if you want to run in headless mode

# Initialize the WebDriver
driver = webdriver.Firefox(options=options)
url = "https://github.com/rememberry-io/rememberry/graphs/contributors?from=2023-08-27&to=2024-09-02&type=d"
driver.get(url)

# Wait for the page to load
time.sleep(5)

# Extract contributor data
try:
    contributors = driver.find_elements(By.CSS_SELECTOR, "li.contrib-person")

    for contributor in contributors:
        # Extract rank
        rank_element = contributor.find_element(By.CSS_SELECTOR, "span.f5.text-normal.color-fg-muted.float-right")
        rank = rank_element.text if rank_element else "N/A"

        # Extract name
        name_element = contributor.find_element(By.CSS_SELECTOR, "a.text-normal")
        name = name_element.text if name_element else "N/A"

        # Extract deletions
        deletions_element = contributor.find_element(By.CSS_SELECTOR, "span.color-fg-danger.text-normal")
        deletions = deletions_element.text if deletions_element else "N/A"

        # Print the extracted details
        print(f"Rank: {rank}")
        print(f"Name: {name}")
        print(f"Deletions: {deletions}")
        print("-" * 40)

finally:
    # Close the WebDriver
    driver.quit()
