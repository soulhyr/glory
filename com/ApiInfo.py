import utils

class ApiInfo:
    def __init__(self, name, url, params):
        self.name = name
        self.url = url
        self.params = params

    def get(self, key):
        return utils.callApi(key, self.name, self.url, self.params)