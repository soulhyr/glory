import os
from com import utils

# 범위 정의
key = 'OMki2H3uW3djNy+vCPQ5VwPBzdMU2ShTVDDUJLa5sTQMyfJxVCW3rwJB9P3900gcnjHwm0WVUI9B2NGZ1WXqoQ=='
years = [y for y in range(2006, 2024, 1)]

# API 연동 : 데이터 수집
utils.callHeatWave(key, years)

# 데이터 로드 : 수집된 데이터 로드
fileList = os.listdir('raw')

# 데이터 정제 및 추출
for file in fileList:
    # 정제 및 추출
    data = utils.extractionData('raw/' + file)
    # 저장
    utils.saveData(data)

# 불러오기
d = utils.loadData()
