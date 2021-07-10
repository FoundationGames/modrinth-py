import json

from .structs import *

from . import common

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

    async def _search(self, session) -> SearchResults:
        params = {
            "query": self.__query,
            "index": self.__sort,
            "offset": self.__start,
            "limit": self.__max_results
        }
        if len(self.__filters) > 0:
            params["facets"] = json.dumps(self.__filters)
        return await api._search(session, params)