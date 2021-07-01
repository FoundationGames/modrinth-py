import json

import requests
from requests.models import Response

from . import common
from .common import api_prefix

class SearchResult():
    def __init__(self, data : dict):
        self.__data = data
        self.__id = data["mod_id"].replace("local-", "")
    
    @property
    def id(self): return self.__id
    @property
    def type(self): return self.__data["project_type"]
    @property
    def author(self): return self.__data["author"]
    @property
    def title(self): return self.__data["title"]
    @property
    def description(self): return self.__data["description"]
    @property
    def categories(self): return self.__data["categories"]
    @property
    def game_versions(self): return self.__data["versions"]
    @property
    def lastest_game_version(self): return self.__data["lastest_version"]
    @property
    def downloads(self): return self.__data["downloads"]
    @property
    def url(self): return self.__data["page_url"]
    @property
    def icon_url(self): return self.__data["icon_url"]
    @property
    def author_url(self): return self.__data["author_url"]
    @property
    def date_created(self): return self.__data["date_created"]
    @property
    def date_modified(self): return self.__data["date_modified"]
    @property
    def license(self): return self.__data["license"]
    @property
    def client_side(self): return self.__data["client_side"]
    @property
    def server_side(self): return self.__data["server_side"]
    

class SearchResults:
    def __init__(self, data : dict):
        self.__results = []
        for mod in data["hits"]:
            self.results.append(SearchResult(mod))
        self.__skipped = data["offset"]
        self.__total = data["total_hits"]

    @property
    def results(self) -> list:
        return self.__results

    @property
    def amount_skipped(self) -> int:
        return self.__skipped

    @property
    def amount_total(self) -> int:
        return self.__total


class Search:
    def __init__(self, query : str = "", categories : list = [], versions : list = [], licenses : list = [], client_support : list = [], server_support : list = [], sort : str = "relevance", start : int = 0, max_results : int = 10):
        self.__query = query
        self.__filters = []
        for e in categories: self.category(e)
        for e in versions: self.version(e)
        for e in licenses: self.license(e)
        for e in client_support: self.client_support(e)
        for e in server_support: self.server_support(e)
        self.__sort = sort
        self.__start = start
        self.__max_results = max_results

    def query(self, query : str):
        self.__query = query
        return self

    def category(self, category : str):
        self.__filters.append([f"categories:{category}"])
        return self

    def version(self, version : str):
        self.__filters.append([f"versions:{version}"])
        return self

    def license(self, license : str):
        self.__filters.append([f"license:{license}"])
        return self

    def client_support(self, requirement : str):
        self.__filters.append([f"client_side:{requirement}"])
        return self

    def server_support(self, requirement : str):
        self.__filters.append([f"server_side:{requirement}"])
        return self

    def faceted_filter(self, filter : list):
        self.__filters.append(filter)
        return self

    def sort(self, sort : str):
        self.__sort = sort
        return self

    def start(self, start : int):
        self.__start = start
        return self

    def max_results(self, max_results : int):
        self.__max_results = max_results
        return self

    def search(self) -> SearchResults:
        global api_prefix
        params = {
            "query": self.__query,
            "facets": json.dumps(self.__filters),
            "index": self.__sort,
            "offset": self.__start,
            "limit": self.__max_results
        }
        response = requests.get(api_prefix+"api/v1/mod", params=params)
        return SearchResults(common.to_json(response))