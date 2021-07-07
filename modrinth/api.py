import aiohttp
from .structs import *
from . import common

_session = aiohttp.ClientSession()
open = True

async def _to_json(response):
    if response.status != 200:
        raise LookupError(f"Recieved status code {response.status} upon request to {response.url}")
    data = await response.json()
    if "error" in data:
        raise LookupError(data["description"])
    return data

async def _user(id : str) -> User:
    global _session
    async with _session.get(common._api_prefix+"v1/user/"+id) as response:
        return User(await _to_json(response))

async def _mod(id : str) -> Mod:
    global _session
    async with _session.get(common._api_prefix+"v1/mod/"+id) as response:
        return Mod(await _to_json(response))

async def _version(id : str) -> Version:
    global _session
    async with _session.get(common._api_prefix+"v1/version/"+id) as response:
        return Version(await _to_json(response))

async def _team(id : str) -> Team:
    global _session
    async with _session.get(common._api_prefix+"v1/team/"+id+"/members") as response:
        return Team(id, await _to_json(response))

async def _search(params : dict) -> SearchResults:
    global _session
    async with _session.get(common._api_prefix+"v1/mod", json=params) as response:
        return SearchResults(await _to_json(response))

async def _open():
    global _session, open
    if _session == None:
        _session = await aiohttp.ClientSession()
        open = True

async def _close():
    global _session, open
    if _session != None:
        await _session.close()
        open = False
