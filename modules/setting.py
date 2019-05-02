import os
import json

class Settings:

    def __init__(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        file_path = dir_path + "/../settings/settings.json"

        self.__settings = {}
        with open(file_path) as f:
            self.__settings = json.load(f)

    def getAllSettings(self):
        return self.__settings

    def get(self, key):
        settings =  self.__settings

        if key in settings:
            settings = settings[key]
        else:
            return None

        return settings

