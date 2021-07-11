from .structs import *
from . import common

async def _to_json(response):
    if response.status != 200:
        raise LookupError(f"Recieved status code {response.status} upon request to {response.url}")
    data = await response.json()
    if "error" in data:
        raise LookupError(data["description"])
    return data

async def _user(session, id : str) -> User:
    async with session.get(common._api_prefix+"v1/user/"+id) as response:
        return User(await _to_json(response))

async def _mod(session, id : str) -> Mod:
    async with session.get(common._api_prefix+"v1/mod/"+id) as response:
        return Mod(session, await _to_json(response))

async def _version(session, id : str) -> Version:
    async with session.get(common._api_prefix+"v1/version/"+id) as response:
        return Version(await _to_json(response))

async def _team(session, id : str) -> Team:
    async with session.get(common._api_prefix+"v1/team/"+id+"/members") as response:
        return Team(session, id, await _to_json(response))

async def _search(session, params : dict) -> SearchResults:
    async with session.get(common._api_prefix+"v1/mod", params=params) as response:
        return SearchResults(session, await _to_json(response))
