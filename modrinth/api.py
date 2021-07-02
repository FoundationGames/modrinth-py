import requests
from .structs import *
from . import common

def _to_json(response : requests.models.Response):
    if response.status_code != 200:
        raise LookupError(f"Recieved status code {response.status_code} upon request to {response.url}")
    data = response.json()
    if "error" in data:
        raise LookupError(data["description"])
    return data

def _user(id : str) -> User:
    response = requests.get(common._api_prefix+"v1/user/"+id)
    return User(_to_json(response))

def _mod(id : str) -> Mod:
    response = requests.get(common._api_prefix+"v1/mod/"+id)
    return Mod(_to_json(response))

def _version(id : str) -> Version:
    response = requests.get(common._api_prefix+"v1/version/"+id)
    return Version(_to_json(response))

def _team(id : str) -> Team:
    response = requests.get(common._api_prefix+"v1/team/"+id+"/members")
    return Team(id, _to_json(response))

def _search(params : dict) -> SearchResults:
    response = requests.get(common._api_prefix+"v1/mod", params=params)
    return SearchResults(_to_json(response))