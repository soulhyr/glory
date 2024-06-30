"""
LSTM model
"""
import pandas as pd
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler
from com import utils
from com.utils import Report

# ++ 입력 데이터 준비
def prepare_data(df, target_city, lookback_years=5):
    # LSTM 모델의 입력 데이터는 과거 lookback_years 만큼의 데이터를 사용
    X, y = [], []
    for i in range(len(df) - lookback_years):
        X.append(df[target_city].values[i:i+lookback_years])
        y.append(df[target_city].values[i+lookback_years])
    return np.array(X), np.array(y)

# DataFrame 생성
data = utils.loadData()
df = pd.DataFrame(data)

# 데이터 전처리: 문자열 숫자 변환
for col in df.columns:
    df[col] = pd.to_numeric(df[col])

# 학습 데이터 세트 준비 (2015년까지 데이터를 학습에 사용)
train_df = df[df['bas_yy'] <= 2015]

# 예측할 시퀀스 데이터 세트 준비 (2016년부터 2022년까지 데이터 사용)
test_df = df[df['bas_yy'] >= 2016]

report = Report()
max_heat_days = {}
cities = [a for a in df.columns if a != 'bas_yy' and a != 'anat_dd_avg']
for city in cities:
    # 학습 데이터 준비
    X_train, y_train = prepare_data(train_df, city)
    # report.insert(f"X_train:{X_train}")
    # report.insert(f"y_train:{y_train}")
    
    # LSTM 모델 정의
    model = Sequential()
    model.add(LSTM(50, activation='relu', input_shape=(X_train.shape[1], 1)))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mse')

    # 데이터 형태 변환: LSTM 입력 형태로 변환 (samples, time steps, features)
    X_train = X_train.reshape((X_train.shape[0], X_train.shape[1], 1))

    # LSTM 모델 학습
    model.fit(X_train, y_train, epochs=100, verbose=0)

    # 테스트 데이터 준비
    X_test, y_test = prepare_data(test_df, city)
    X_test = X_test.reshape((X_test.shape[0], X_test.shape[1], 1))
    # report.insert(f"X_test:{X_test}")
    # report.insert(f"y_test:{y_test}")

    # LSTM 모델을 사용한 예측
    predicted_values = model.predict(X_test)
    
    max_heat_days[city] = np.mean(predicted_values[-2:])  # 평균값을 구하여 2021년과 2022년 예측값 사용

    # 예측 결과
    report.insert(f"Predicted values for {city[1:]} ({city}) in 2021 and 2022:")
    for i in range(len(predicted_values)):
        report.insert(f"Year {2021 + i}: Predicted - {predicted_values[i][0]:.2f} days")

# 가장 폭염 일수가 높을 것으로 예상되는 도시 3개 예측
top_3_cities = sorted(max_heat_days, key=max_heat_days.get, reverse=True)[:3]
report.insert(f"\nTop 3 cities with highest predicted heat wave days in 2021 and 2022:")
for i, city in enumerate(top_3_cities):
    report.insert(f"{i+1}. {city} - Average predicted heat wave days: {max_heat_days[city]:.2f}")

# report 출력.
report.print()
