import json
import re
import urllib.parse
from typing import Any, Dict, List, Tuple

import requests


def extract_gh_owner_repo(url: str) -> Tuple[str, str]:
    decoded_url = urllib.parse.unquote(url)

    pattern = r"https://github\.com/([^/]+)/([^/]+)"
    match = re.search(pattern, decoded_url)

    if match:
        return match.group(1), match.group(2)
    raise ValueError("Invalid GitHub URL format")


def scrape_gh_contribution_data(owner: str, repo: str) -> List[Dict[str, Any]]:
    url = f"https://api.github.com/repos/{owner}/{repo}/stats/contributors"

    try:
        response = requests.get(url)
        contributors = json.loads(response.text)

        deletion_ranking = []
        for contributor in contributors:
            username = contributor["author"]["login"]
            profile_pic = contributor["author"]["avatar_url"]
            commits = contributor["total"]
            additions = sum(week["a"] for week in contributor["weeks"])
            deletions = sum(week["d"] for week in contributor["weeks"])

            deletion_ranking.append(
                {"contributor": {"username": username, "profile_pic": profile_pic, "deletions": deletions, "additions": additions, "commits": commits}}
            )

        deletion_ranking.sort(key=lambda x: (x["contributor"]["deletions"], x["contributor"]["additions"]), reverse=True)
        return deletion_ranking

    except Exception as e:
        print(f"Failed to retrieve data. Exception: {e}")


if __name__ == "__main__":
    url1 = "https%3A%2F%2Fgithub.com%2Fblack-forest-labs%2Fflux%2Fgraphs%2Fcontributors"
    url2 = "https://github.com/black-forest-labs/flux/graphs/contributors"

    owner1, repo1 = extract_gh_owner_repo(url1)
    owner, repo = extract_gh_owner_repo(url2)

    print(owner1, repo1)  # Output: black-forest-labs flux
    print(owner, repo)  # Output: black-forest-labs flux

    owner, repo = extract_gh_owner_repo("https://github.com/black-forest-labs/flux/graphs/contributors")
    # owner, repo = extract_gh_owner_repo("https://github.com/langfuse/langfuse")
    contributor_data = scrape_gh_contribution_data(owner=owner, repo=repo)

    first = contributor_data[0]
    print(f"The contributor with the most deletions is {first['contributor']['username']} with {first['contributor']['deletions']} deletions.")

    import subprocess

    with open("deletion-ranking.json", "w") as file:
        json.dump(contributor_data, file, indent=4)

    subprocess.run(["cat", "deletion-ranking.json"])
    subprocess.run(["rm", "deletion-ranking.json"])
