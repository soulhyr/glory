"""
Project 제출용
"""
import os
import json
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from com import utils
from com.utils import Report


xlsx = 'xlsx/2023 외래관광객조사 DATA.xlsx'
df = pd.read_excel(xlsx)
df['year'] = int(xlsx.split('/')[1][:4])
df.columns = df.columns.str.lower()

# print(df['year', '서울일tot','경기일tot','인천일tot','강원일tot','대전일tot','충북일tot','충남일tot','세종일tot','경북일tot','경남일tot','대구일tot','울산일tot','부산일tot','광주일tot','전북일tot','전남일tot','제주일tot'])

# df2 컬럼들 sum 구하면 2023년 각 지역별 숙박 수
df2 = df[['year', '서울일tot','경기일tot','인천일tot','강원일tot','대전일tot','충북일tot','충남일tot','세종일tot','경북일tot','경남일tot','대구일tot','울산일tot','부산일tot','광주일tot','전북일tot','전남일tot','제주일tot']]
# print(df2)

df2_sum = df2.drop('year', axis=1).sum()
# print('각 지역별 숙박 수 총합:')
print(df2_sum)

# # df3 평균은 1인 1일 지출 경비 평균
df3 = df[['year', 'mday전체tot_raw61항공제외2']]
mean_money = df3['mday전체tot_raw61항공제외2'].mean()
print('====================1')
print(mean_money)
print('====================2')
# df2 * df3 = 2023년 각 지역별 1인당 지출 평균액
df_final = df2_sum.mul(mean_money)
# df_numeric['각 지역별 1인당 지출 평균액'] = df_numeric.apply(lambda x:x * 223)
print('====================3')
print(df_final)

# 방문객 1명이 늘어 날 시 df4 만큼의 지역 경제 활성화 효과가 발생.
# 2023년 기준 


# 각 도시별 insight 도출.
# report = Report()
# cities = [a for a in df.columns if a != 'bas_yy' and a != 'anat_dd_avg']
# for city in cities:
#     # lseoul 도시의 시계열 데이터 추출
#     time_series = df[city]

#     # 차분 계산
#     diff = time_series.diff().dropna()

#     # ARIMA 모델 학습
#     model = ARIMA(time_series, order=(1, 1, 1))  # ARIMA(p, d, q): p=1, d=1, q=1로 설정
#     model_fit = model.fit()

#     # 예측
#     forecast = model_fit.forecast(steps=2)  # 2021년, 2022년 예측

#     # 예측 결과 출력
#     report.insert(f"Predicted values for {city[1:]} ({city}) in 2021 and 2022:")
#     report.insert(f"Year 2021: Predicted - {forecast.iloc[0]:.2f} days")
#     report.insert(f"Year 2022: Predicted - {forecast.iloc[1]:.2f} days")

# # report 출력.
# report.print()
