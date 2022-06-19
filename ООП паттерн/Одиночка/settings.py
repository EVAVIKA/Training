from asyncio.windows_events import NULL


class Settings:
    __instance = object 
    __score = NULL
    def __init__(self):
        self.__score = 0
        
    @classmethod
    def get_instance(_class):
        if not isinstance(_class.__instance, Settings):
            _class.__instance = Settings()
        return _class.__instance

    def add_score_points(self, count):
        self.__score += count
        
    def say_score(self):
        print(self.__score)
        
    