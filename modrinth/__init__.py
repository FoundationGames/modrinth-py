import requests
from requests.models import Response

from .search import Search
from .search import SearchResult
from .search import SearchResults

from .structs import User
from .structs import Mod
from .structs import Version
from .structs import Team

from . import common
from .common import api_prefix

def get_user(id : str) -> User:
    response = requests.get(api_prefix+"api/v1/user/"+id)
    return User(common.to_json(response))

def get_mod(id : str) -> Mod:
    response = requests.get(api_prefix+"api/v1/mod/"+id)
    return Mod(common.to_json(response))

def get_version(id : str) -> Version:
    response = requests.get(api_prefix+"api/v1/version/"+id)
    return Version(common.to_json(response))

def get_team(id : str) -> Team:
    response = requests.get(api_prefix+"api/v1/team/"+id+"/members")
    return Team(common.to_json(response))