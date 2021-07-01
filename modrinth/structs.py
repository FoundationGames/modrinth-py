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