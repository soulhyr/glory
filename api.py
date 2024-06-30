import os
from com import utils

# 범위 정의
key = 'zNSBCOfkaU4z5NBg5mcjygq8BwxvEOmWZkEd2KTlgthaLAaNQPlMIqQGLBncvjSbICAMNOkQMqczzaJxX6IAfQ=='
years = [y for y in range(2009, 2020, 1)]

# 수집
utils.callHeatWave(key, years)

fileList = os.listdir('raw')

for file in fileList:
    # 정제(추출)
    data = utils.extractionData('raw/' + file)
    # 저장
    utils.saveData(data)

# 불러오기
d = utils.loadData()
