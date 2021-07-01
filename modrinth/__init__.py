import requests
from requests.models import Response

from .search import Search
from .search import SearchResult
from .search import SearchResults

from .structs import User

from . import common
from .common import api_prefix

def get_user(id : str) -> User:
    response = requests.get(api_prefix+"api/v1/user/"+id)
    return User(common.to_json(response))