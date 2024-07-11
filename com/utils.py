import os
import json
from com.logHelper import logger
import requests
from datetime import datetime
# from datetime import datetime

# 폭염 api 호출
def callHeatWave(key, years):
    url = 'http://apis.data.go.kr/1741000/DaysHeatWavesMajorCitiesYear/getDaysHeatWavesMajorCitiesYearList'
    folderPath = "raw"
    try:
        for y in years:
            params ={'serviceKey' : key, 'pageNo' : '1', 'numOfRows' : '300', 'type' : 'json', 'bas_yy' : y }
            logger.info('API 를 호출합니다.')
            response = requests.get(url, params=params)
            fileName = 'result_' + str(y) + '.raw'
            filePath = os.path.join(folderPath, fileName)
            with open(filePath, 'w') as f:  # 기존 파일 있으면 덮어씀
                f.write(response.content.decode('utf-8')) 
            logger.info('API 호출 결과를 저장합니다.')
                # json.dump(response.content.decode('utf-8'), f)
    except Exception as e:
        logger.error('API Error!!')

# api 호출 기능
def callApi(key, tp, url, params):
    folderPath = "raw"
    try:
        logger.info('API 를 호출합니다.')
        response = requests.get(url, params=params)
        dt = datetime.now().strftime("%Y%m%d%H%S%f")
        fileName = tp + '_result_' + dt + '.raw'
        filePath = os.path.join(folderPath, fileName)
        with open(filePath, 'w') as f:  # 기존 파일 있으면 덮어씀
            f.write(response.content.decode('utf-8')) 
        logger.info('API 호출 결과를 저장합니다.')

        return fileName
    except Exception as e:
        logger.error("API Error!!")


# log 파일에서 데이터 추출
def extractionData(filePath):
    result = None
    try:
        logger.info('파일에서 데이터를 추출 합니다.')
        with open(filePath, 'r') as f:
            result = f.read()
            result = json.loads(result)
            result = result['DaysHeatWavesMajorCitiesYear'][1]['row'][0] if 'DaysHeatWavesMajorCitiesYear' in result else None
        logger.info(result)
    except Exception as e:
        print('=================================')
        print(e)
        print('=================================')
        logger.error('Extraction Error!!')
        result = None
    return result

# 저장된 데이터(json 파일) 로드
def loadData():
    filePath = 'json/heatWave.json'
    try:
        logger.info('json 데이터를 로드합니다.')
        with open(filePath, 'r') as f:
            data = json.load(f)
        logger.info('로드 결과 : ')
    except FileNotFoundError as e:
        logger.info('기존 파일이 존재하지 않아 새로 생성합니다.')
        data = None
    except Exception as e:
        logger.error('Data load Error!!')
    return data

def fileSave(data):
    logger.info('파일을 저장합니다.')
    try:
        filePath = os.path.join('json', 'heatWave.json')
        with open(filePath, 'w') as f:
            json.dump(data, f, indent = 4)
        logger.info('저장 결과 : ')
    except Exception as e:
        logger.error('Save File Error!!')

# 추출 데이터 저장
def saveData(data):
    try:
        logger.info('추출 데이터를 저장합니다.')
        if data != None:
            db = loadData()
            if db == None:
                fileSave(data)
            else:
                db = {'rows': db if isinstance(db, list) else [db]}
                filter_db = [d for d in db['rows'] if d['bas_yy'] != data['bas_yy']]
                filter_db.append(data)
                fileSave(filter_db)
        logger.info('저장 완료!')
    except Exception as e:
        logger.error('Data save Error!!')

class Report:
    def __init__(self):
        self.report = []

    def insert(self, str):
        self.report.append(str)

    def print(self):
        print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[ Report ]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
        for r in self.report:
            print(r)
        print("==========================================================================")


