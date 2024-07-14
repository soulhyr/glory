import json
import time
import streamlit as st
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

# 저장된 데이터(json 파일) 로드
def loadData():
    filePath = 'json/heatWave.json'
    try:
        st.toast('json 데이터를 로드합니다.')
        with open(filePath, 'r') as f:
            data = json.load(f)
        # time.sleep(2)
    except FileNotFoundError as e:
        st.toast('기존 파일이 존재하지 않아 새로 생성합니다.')
        data = None
    except Exception as e:
        st.toast('Data load Error!!')
    return data

data = None
result = []

if st.button('Get Data'):
    # 데이터프레임 생성
    data = loadData()
    
    df = pd.DataFrame(data)

    # 데이터 전처리: 문자열 숫자 변환
    st.toast('데이터 전처리 작업을 수행합니다.')
    for col in df.columns:
        df[col] = pd.to_numeric(df[col])

    # 각 도시별 insight 도출.
    st.toast('ARIMA ML model 을 통해 각 도시의 폭염일을 예측합니다.')
    cities = [a for a in df.columns if a != 'bas_yy' and a != 'anat_dd_avg']
    for city in cities:
        # 도시의 시계열 데이터 추출
        time_series = df[city]

        # 차분 계산
        diff = time_series.diff().dropna()

        # ARIMA 모델 학습
        model = ARIMA(time_series, order=(1, 1, 1))  # ARIMA(p, d, q): p=1, d=1, q=1로 설정
        model_fit = model.fit()

        # 예측
        forecast = model_fit.forecast(steps=2)  # 2021년, 2022년 예측

        # 예측 결과 출력
        result.append(f"Predicted values for :blue-background[{city[1:]}] ({city}) in 2021 and 2022")
        result.append(f"- Year 2021: Predicted : :green-background[{forecast.iloc[0]:.2f} days]")
        result.append(f"- Year 2022: Predicted : :green-background[{forecast.iloc[1]:.2f} days]")

def resultPrint():
    n = 1
    for txt in result:
        if n == 1:
            st.toast('예축결과를 Stream 으로 출력합니다.')
        if n % 3 == 1:
            yield ':black[**' + txt + '**]\n\n'
        else:
            yield txt + '\n\n'
        n=n+1
        time.sleep(0.05)

col1, col2 = st.columns(2)
with col1:
    st.header("Data")
    data
with col2:
    st.header("Predicte")
    # 출략
    placeholder = st.empty()
    with placeholder.container():
        st.write_stream(resultPrint)
        # for txt in result:
        #     st.write(txt)
