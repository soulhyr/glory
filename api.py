from com import utils

class ApiInfo:
    def __init__(self, name, url, params):
        self.name = name
        self.url = url
        self.params = params

    def call(self):
        return utils.callApi(key, self.name, self.url, self.params)
    
class Asset:
    def __init__(self):
        self.apis = []
   
    def add(self, name, url, params):
        api = ApiInfo(name, url, params)
        self.apis.append(api)
    
    def call(self):
        for api in self.apis:
            api.call()



# key = 'OMki2H3uW3djNy%2BvCPQ5VwPBzdMU2ShTVDDUJLa5sTQMyfJxVCW3rwJB9P3900gcnjHwm0WVUI9B2NGZ1WXqoQ%3D%3D'
key = 'OMki2H3uW3djNy+vCPQ5VwPBzdMU2ShTVDDUJLa5sTQMyfJxVCW3rwJB9P3900gcnjHwm0WVUI9B2NGZ1WXqoQ=='
apis = Asset()
apis.add('API01'
        , 'http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList'
        , {'serviceKey' : key, 'YM' : '201201', 'SIDO' : '부산광역시', 'GUNGU' : '해운대구', 'RES_NM' : '부산시립미술관' })

apis.call()


# for url in urls:
#     utils.callApi(key, "", url, {})
