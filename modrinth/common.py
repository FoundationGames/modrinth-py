import requests
from requests.models import Response

api_prefix = "https://api.modrinth.com/"

def to_json(response : Response):
    if response.status_code != 200:
        raise LookupError(f"Recieved status code {response.status_code} upon request to {response.url}")
    data = response.json()
    if "error" in data:
        raise LookupError(data["description"])
    return data