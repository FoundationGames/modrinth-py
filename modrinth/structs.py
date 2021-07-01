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
    def created(self) -> str: return DateTime(self.__data["created"])
    @property
    def role(self) -> str: return self.__data["role"]


class Mod:
    def __init__(self, data : dict):
        self.__data = data

    @property
    def id(self) -> str: return self.__data["id"]

    @property
    def slug(self) -> str: return self.__data["slug"]

    @property
    def team(self) -> str: return self.__data["team"]

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
    def license(self) -> dict: return self.__data["license"]

    @property
    def client_side(self) -> str: return self.__data["client_side"]

    @property
    def server_side(self) -> str: return self.__data["server_side"]

    @property
    def downloads(self) -> int: return self.__data["downloads"]

    @property
    def categories(self) -> list: return self.__data["categories"]

    @property
    def versions(self) -> list: return self.__data["versions"]

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
    def donation_urls(self) -> list: return self.__data["donation_urls"]


class Version:
    def __init__(self, data : dict):
        self.__data = data

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
    def version_number(self) -> str: return self.__data["version_number"]

    @property
    def changelog(self) -> str: return self.__data["changelog"]

    @property
    def changelog_url(self) -> str: return self.__data["changelog_url"]

    @property
    def date_published(self) -> DateTime: return DateTime(self.__data["date_published"])

    @property
    def downloads(self) -> int: return self.__data["downloads"]

    @property
    def version_type(self) -> int: return self.__data["version_type"]

    #skipped "files"

    @property
    def dependencies(self) -> list: return self.__data["dependencies"]

    @property
    def game_versions(self) -> list: return self.__data["game_versions"]

    @property
    def loaders(self) -> list: return self.__data["loaders"]



class Team:
    def __init__(self, data : dict):
        self.__data = data

    @property
    def team_id(self) -> list:
        return self.__data

    @property
    def user_id(self) -> list:
        team_id = []
        for i in range(len(self.__data)):
            team_id.append(self.__data[i]['user_id'])
        return team_id