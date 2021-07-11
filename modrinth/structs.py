from . import common, api


class DateTime:
    def __init__(self, date_time : str):
        pass


class User:
    def __init__(self, data : dict):
        self.__data = data

    @property
    def id(self) -> str: return self.__data["id"]
    @property
    def github_id(self) -> str: return self.__data["github_id"] if "github_id" in self.__data else None
    @property
    def username(self) -> str: return self.__data["username"]
    @property
    def display_name(self) -> str: return self.__data["name"] if not self.__data["name"] is None else self.username
    @property
    def email(self) -> str: return self.__data["email"] if "email" in self.__data else None
    @property
    def avatar_url(self) -> str: return self.__data["avatar_url"]
    @property
    def bio(self) -> str: return self.__data["bio"]
    @property
    def created(self) -> str: return self.__data("created")
    @property
    def role(self) -> str: return self.__data["role"]


class TeamMember:
    def __init__(self, data : dict):
        self.__data = data

    @property
    def team_id(self) -> str: return self.__data["team_id"]

    async def get_team(self): return await api._team(self.team_id)

    @property
    def user_id(self) -> str: return self.__data["user_id"]

    async def get_user(self): return await api._user(self.user_id)

    @property
    def role(self) -> str: return self.__data["role"]
    @property
    def permissions(self) -> int: return self.__data["permissions"]


class Team:
    def __init__(self, id : str, data : dict):
        self.__id = id
        self.__data = data
        self.__members = []
        for user in data:
            self.__members.append(TeamMember(user))

    @property
    def id(self) -> str: return self.__id
    @property
    def members(self) -> list: return self.__members

    @property
    def team_info(self) -> list:
        team_ = []
        for i in range(len(self.__data)): # Loops through a list with a dictionary nested in it.  
            user_dict = {"user_id" : self.__data[i]["user_id"], "role" : self.__data[i]["role"], "accepted" : self.__data[i]["accepted"]}
            team_.append(user_dict)
        return team_

    @property
    def user_ids(self) -> list:
        team_user_id = []
        for i in range(len(self.__data)):
            team_user_id.append(self.__data[i]['user_id'])
        return team_user_id




class License:
    def __init__(self, data : dict):
        self.__data = data

    @property
    def id(self) -> str: return self.__data["id"]
    @property
    def name(self) -> str: return self.__data["name"]
    @property
    def url(self) -> str: return self.__data["url"]


class DonationLink:
    def __init__(self, data : dict):
        self.__data = data

    @property
    def id(self) -> str: return self.__data["id"]
    @property
    def platform(self) -> str: return self.__data["platform"]
    @property
    def url(self) -> str: return self.__data["url"]


class VersionFile:
    def __init__(self, data : dict):
        self.__data = data

    @property
    def sha1(self) -> str: return self.__data["hashes"]["sha1"]
    @property
    def sha512(self) -> str: return self.__data["hashes"]["sha512"]
    @property
    def filename(self) -> str: return self.__data["filename"]
    @property
    def url(self) -> str: return self.__data["url"]


class Version:
    def __init__(self, data : dict):
        self.__data = data
        self.__files = []
        for file in data["files"]:
            self.__files.append(VersionFile(file))

    @property
    def id(self) -> str: return self.__data["id"]
    @property
    def mod_id(self) -> str: return self.__data["mod_id"]
    @property
    def author_id(self) -> str: return self.__data["author_id"]
    @property
    def featured(self) -> str: return self.__data["featured"]
    @property
    def name(self) -> str: return self.__data["name"]
    @property
    def number(self) -> str: return self.__data["version_number"]
    @property
    def changelog(self) -> str: return self.__data["changelog"]
    @property
    def changelog_url(self) -> str: return self.__data["changelog_url"]
    @property
    def date_published(self): return DateTime(self.__data["date_published"])
    @property
    def downloads(self) -> int: return self.__data["downloads"]
    @property
    def version_type(self) -> int: return self.__data["version_type"]
    @property
    def files(self) -> list: return self.__files
    @property
    def dependencies(self) -> list: return self.__data["dependencies"]
    @property
    def game_versions(self) -> list: return self.__data["game_versions"]
    @property
    def loaders(self) -> list: return self.__data["loaders"]


class Mod:
    def __init__(self, data : dict):
        self.__data = data
        self.__donation_links = []
        for link in data["donation_urls"]:
            self.__donation_links.append(DonationLink(link))

    @property
    def id(self) -> str: return self.__data["id"]
    @property
    def slug(self) -> str: return self.__data["slug"]
    @property
    def team_id(self) -> str: return self.__data["team"]

    async def get_team(self): return await api._team(self.__data["team"])

    @property
    def title(self) -> str: return self.__data["title"]
    @property
    def description(self) -> str: return self.__data["description"]
    @property
    def body(self) -> str: return self.__data["body"]
    @property
    def body_url(self) -> str: return self.__data["body_url"]
    @property
    def published(self) -> str: return self.__data["published"]
    @property
    def updated(self) -> str: return self.__data["updated"]
    @property
    def status(self) -> str: return self.__data["status"]
    @property
    def license(self): return License(self.__data["license"])
    @property
    def client_side(self) -> str: return self.__data["client_side"]
    @property
    def server_side(self) -> str: return self.__data["server_side"]
    @property
    def downloads(self) -> int: return self.__data["downloads"]
    @property
    def categories(self) -> list: return self.__data["categories"]
    
    async def get_versions(self) -> list:
        versions = []
        for id in self.__data["versions"]:
            versions.append(await api._version(id))
        return versions

    @property
    def icon_url(self) -> str: return self.__data["icon_url"]
    @property
    def issues_url(self) -> str: return self.__data["issues_url"]
    @property
    def source_url(self) -> str: return self.__data["source_url"]
    @property
    def wiki_url(self) -> str: return self.__data["wiki_url"]
    @property
    def discord_url(self) -> str: return self.__data["discord_url"]
    @property
    def donation_links(self) -> list: return self.__donation_links


class SearchResult():
    def __init__(self, data : dict):
        self.__data = data
        self.__id = data["mod_id"].replace("local-", "")


    @property
    def id(self): return self.__id
    
    async def get_mod(self): return await api._mod(self.__id)

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
        self.__data = data
        self.__results = []
        for hit in data["hits"]:
            self.results.append(SearchResult(hit))

    @property
    def results(self) -> list: return self.__results
    @property
    def amount_skipped(self) -> int: return self.__data["offset"]
    @property
    def amount_total(self) -> int: return self.__data["total_hits"]