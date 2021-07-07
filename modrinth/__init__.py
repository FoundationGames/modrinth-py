from . import api

from .structs import User
from .structs import Mod
from .structs import Version
from .structs import Team
from .structs import SearchResult
from .structs import SearchResults

from .search import Search

async def get_user(id : str) -> User:
    return await api._user(id)

async def get_mod(id : str) -> Mod:
    return await api._mod(id)

async def get_version(id : str) -> Version:
    return await api._version(id)

async def get_team(id : str) -> Team:
    return await api._team(id)

def open():
    api._open()

def close():
    api._close()