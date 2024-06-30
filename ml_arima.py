"""
ARIMA model
"""
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from com import utils
from com.utils import Report

# 데이터프레임 생성
data = utils.loadData()
df = pd.DataFrame(data)

# 데이터 전처리: 문자열 숫자 변환
for col in df.columns:
    df[col] = pd.to_numeric(df[col])

# 각 도시별 insight 도출.
report = Report()
cities = [a for a in df.columns if a != 'bas_yy' and a != 'anat_dd_avg']
for city in cities:
    # lseoul 도시의 시계열 데이터 추출
    time_series = df[city]

    # 차분 계산
    diff = time_series.diff().dropna()

    # ARIMA 모델 학습
    model = ARIMA(time_series, order=(1, 1, 1))  # ARIMA(p, d, q): p=1, d=1, q=1로 설정
    model_fit = model.fit()

    # 예측
    forecast = model_fit.forecast(steps=2)  # 2021년, 2022년 예측

    # 예측 결과 출력
    report.insert(f"Predicted values for {city[1:]} ({city}) in 2021 and 2022:")
    report.insert(f"Year 2021: Predicted - {forecast.iloc[0]:.2f} days")
    report.insert(f"Year 2022: Predicted - {forecast.iloc[1]:.2f} days")

# report 출력.
report.print()
