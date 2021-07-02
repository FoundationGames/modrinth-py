from . import api

from .structs import User
from .structs import Mod
from .structs import Version
from .structs import Team
from .structs import SearchResult
from .structs import SearchResults

from .search import Search

def get_user(id : str) -> User:
    return api._user(id)

def get_mod(id : str) -> Mod:
    return api._mod(id)

def get_version(id : str) -> Version:
    return api._version(id)

def get_team(id : str) -> Team:
    return api._team(id)