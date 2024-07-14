import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error

# 데이터 준비
years_korea = [
    {'year': 2021, 'city': 'a', 'visitor': 311},
    {'year': 2021, 'city': 'b', 'visitor': 364},
    {'year': 2021, 'city': 'c', 'visitor': 323},
    {'year': 2022, 'city': 'a', 'visitor': 371},
    {'year': 2022, 'city': 'b', 'visitor': 464},
    {'year': 2022, 'city': 'c', 'visitor': 423}
]

years_abroad = [
    {'year': 2021, 'city': 'a', 'visitor': 341},
    {'year': 2021, 'city': 'b', 'visitor': 514},
    {'year': 2021, 'city': 'c', 'visitor': 443}
]

# 데이터를 DataFrame으로 변환
data_korea = pd.DataFrame(years_korea)
data_abroad = pd.DataFrame(years_abroad)

# 도시(city)별로 데이터를 분리하여 ARIMA 모델 학습 및 예측
forecast_results = []

cities = data_korea['city'].unique()
print(11111111111111111)
for city in cities:
    # 해당 도시의 데이터 추출
    data_city_korea = data_korea[data_korea['city'] == city][['year', 'visitor']].set_index('year')
    data_city_abroad = data_abroad[data_abroad['city'] == city][['year', 'visitor']].set_index('year')
    data_city_korea
    print(2222222222222222)
    # ARIMA 모델 생성 및 학습
    model = ARIMA(data_city_korea, order=(1, 1, 1))
    print(model)
    print(333333333333333333)
    model_fit = model.fit()
    # 2022년 예측
    forecast = model_fit.forecast(steps=1)
    print(444444444444444444)
    # 결과 저장
    forecast_results.append({
        'city': city,
        'year': 2022,
        'predicted_visitor': forecast[0],
        'actual_visitor_2021': data_city_abroad.loc[2021, 'visitor']  # 인덱스를 정수로 지정
    })

# 예측 결과 출력
print("도시별 2022년 해외 방문객 예측 결과:")
for result in forecast_results:
    print(f"{result['city']}: 예측 방문객 수 = {result['predicted_visitor']:.2f}, 실제 2021년 방문객 수 = {result['actual_visitor_2021']}")

# 예측 결과 시각화 (선택적으로)
plt.figure(figsize=(10, 6))
for result in forecast_results:
    plt.bar(result['city'], result['predicted_visitor'], label=f"{result['city']} 예측")
plt.title('2022년 도시별 해외 방문객 예측')
plt.xlabel('도시')
plt.ylabel('방문객 수')
plt.legend()
plt.grid(True)
plt.show()
