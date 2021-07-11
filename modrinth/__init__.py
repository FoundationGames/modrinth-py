import aiohttp

from . import api

from .structs import User
from .structs import Mod
from .structs import Version
from .structs import Team
from .structs import SearchResult
from .structs import SearchResults

from .search import Search

class ModrinthSession:
    def __init__(self):
        self._session = aiohttp.ClientSession()

    async def __aenter__(self):
        return self

    async def __aexit__(self, type, value, traceback):
        await self.close()

    async def close(self):
        await self._session.close()

    async def get_user(self, id : str) -> User:
        return await api._user(self._session, id)

    async def get_mod(self, id : str) -> Mod:
        return await api._mod(self._session, id)

    async def get_version(self, id : str) -> Version:
        return await api._version(self._session, id)

    async def get_team(self, id : str) -> Team:
        return await api._team(self._session, id)

    async def search(self, search : Search) -> SearchResults:
        return await search._search(self._session)