import streamlit as st
import json
import requests

def callHeatWave():
    # 범위 정의
    key = 'OMki2H3uW3djNy+vCPQ5VwPBzdMU2ShTVDDUJLa5sTQMyfJxVCW3rwJB9P3900gcnjHwm0WVUI9B2NGZ1WXqoQ=='
    url = 'http://apis.data.go.kr/1741000/DaysHeatWavesMajorCitiesYear/getDaysHeatWavesMajorCitiesYearList'
    try:
        
        params ={'serviceKey' : key, 'pageNo' : '1', 'numOfRows' : '300', 'type' : 'json', 'bas_yy' : year }
        st.toast('API 를 호출합니다.')
    # time.sleep(.5)
        response = requests.get(url, params=params)
        rst = response.content.decode('utf-8') 
        return rst
    except Exception as e:
        st.write('API Error!!', e)

st.text('Collection')
st.text('데이터를 수집하는 과정을 실시간으로 보여줍니다.')
result = ''
result_ext = ''
result_json = {}
year = st.number_input('수집할 년도 : ', step=1, min_value=2006, max_value=2024)

if st.button('API 연동', type='primary'):
    result = callHeatWave()
    result_json = json.loads(result)
    result_ext = result_json['DaysHeatWavesMajorCitiesYear'][1]['row'][0] if 'DaysHeatWavesMajorCitiesYear' in result_json else None

st.text_area('Result Log', result)
st.text_area('Extraction', result_ext)

if result_json != {}:
    result_json