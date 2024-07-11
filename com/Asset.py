import ApiInfo

class Asset:
    def __init__(self, key):
        self.key = key
        self.apis = []
   
    def add(self, name, url, params):
        api = ApiInfo(name, url, params)
        self.apis.append(api)
