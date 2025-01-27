import requests
import os
from dotenv import load_dotenv

load_dotenv()

def search_companies(payload):
    """
    Searches for companies using the Apollo API.

    Args:
        api_key (str): Your API key for the Apollo API.
        num_employees_ranges (list): List of employee range strings (e.g., ["1,200"]).
        locations (list): List of location strings (e.g., ["kuala lumpur", "malaysia"]).
        keyword_tags (list): List of keyword tags (e.g., ["IT services", "Pega Systems"]).
        name (str, optional): Organization name to search for. Defaults to None.
        not_locations (list, optional): List of locations to exclude. Defaults to None.
        page (int, optional): Page number for pagination. Defaults to 1.
        per_page (int, optional): Number of results per page. Defaults to 3.

    Returns:
        list: A list of organizations matching the search criteria.
    """
    url = "https://api.apollo.io/api/v1/mixed_companies/search"

    headers = {
        "accept": "application/json",
        "Cache-Control": "no-cache",
        "Content-Type": "application/json",
        "x-api-key": os.getenv("APOLLO_KEY")
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
        data = response.json()['organizations']
        return data
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
