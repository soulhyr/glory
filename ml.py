# # import json
# # import numpy as np
# # from sklearn.model_selection import train_test_split
# # from sklearn.linear_model import LinearRegression
# # from sklearn.metrics import mean_squared_error



# data = utils.loadData()

# # # Feature와 Target 데이터 준비
# # X = []
# # y = []
# # for item in data:
# #     X.append([
# #         float(item['lseoul']),
# #         float(item['lgangneung']),
# #         float(item['ldaejeon']),
# #         float(item['ldaegu']),
# #         float(item['lgwangju']),
# #         float(item['lbusan']),
# #         float(item['anat_dd_avg'])
# #     ])
# #     y.append(float(item['bas_yy']))

# # X = np.array(X)
# # y = np.array(y)

# # # 학습 데이터와 테스트 데이터 분리
# # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # # 선형 회귀 모델 선택 및 학습
# # model = LinearRegression()
# # model.fit(X_train, y_train)

# # # 테스트 데이터로 예측
# # y_pred = model.predict(X_test)

# # # 모델 평가 (예: 평균 제곱 오차)
# # mse = mean_squared_error(y_test, y_pred)
# # print(f"Mean Squared Error: {mse}")

# # # 새로운 데이터에 대한 예측 (예시)
# # new_data = np.array([
# #     [15.5, 20.5, 25.0, 30.0, 22.0, 10.0, 5.2],  # 예를 들어 각 지역의 평균 기온과 강수량을 제공
# #     [14.0, 18.0, 23.0, 28.0, 21.0, 11.0, 4.8]   # 또 다른 새로운 데이터 예시
# # ])
# # predicted_years = model.predict(new_data)
# # for i, year in enumerate(predicted_years):
# #     print(f"Predicted year {i+1}: {year}")



# import numpy as np
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_squared_error


# data = utils.loadData()

# # 머신러닝 모델에 사용할 데이터 구조로 변환
# years = []
# X = []  # 도시별 평균 기온 데이터
# y = []  # 도시별 폭염 일 수 데이터

# for entry in data:
#     year = int(entry["bas_yy"])
#     seoul_temp = float(entry["lseoul"])
#     gangneung_temp = float(entry["lgangneung"])
#     daejeon_temp = float(entry["ldaejeon"])
#     daegu_temp = float(entry["ldaegu"])
#     gwangju_temp = float(entry["lgwangju"])
#     busan_temp = float(entry["lbusan"])
#     avg_rainfall = float(entry["anat_dd_avg"])
    
#     # 각 도시별 데이터를 리스트에 추가
#     years.append(year)
#     X.append([seoul_temp, gangneung_temp, daejeon_temp, daegu_temp, gwangju_temp, busan_temp, avg_rainfall])
#     y.append([float(entry["lseoul"]), float(entry["lgangneung"]), float(entry["ldaejeon"]), float(entry["ldaegu"]), float(entry["lgwangju"]), float(entry["lbusan"])])

# # Numpy 배열로 변환
# years = np.array([int(entry["bas_yy"]) for entry in data])
# X = np.array(X)
# y = np.array(y)

# # 2020년까지는 학습 데이터로, 나머지는 테스트 데이터로 분할
# train_idx = np.where(years <= 2020)[0]
# test_idx = np.where(years > 2020)[0]

# X_train = X[train_idx]
# y_train = y[train_idx]
# X_test = X[test_idx]
# y_test = y[test_idx]

# # 선형 회귀 모델 선택 및 학습
# model = LinearRegression()
# model.fit(X_train, y_train)

# # 검증 데이터에 대한 예측
# y_pred = model.predict(X_test)

# # 검증 결과 평가 (예: 평균 제곱 오차)
# mse = mean_squared_error(y_test, y_pred)
# print(f"Mean Squared Error on test data: {mse}")

# # 2023년 데이터 준비 (예측할 데이터)
# X_2023 = np.array([[18, 11, 21, 23, 14, 3, 11.8]])  # 예를 들어 각 도시의 2023년 평균 기온 및 강수량 데이터

# # 예측
# predicted_heat_days_2023 = model.predict(X_2023)

# # 결과 출력
# print("\nPredicted heat days for each city in 2023:")
# print(f"Seoul: {predicted_heat_days_2023[0][0]}")
# print(f"Gangneung: {predicted_heat_days_2023[0][1]}")
# print(f"Daejeon: {predicted_heat_days_2023[0][2]}")
# print(f"Daegu: {predicted_heat_days_2023[0][3]}")
# print(f"Gwangju: {predicted_heat_days_2023[0][4]}")
# print(f"Busan: {predicted_heat_days_2023[0][5]}")

# # 년도별 각 도시의 폭염 일 수 데이터가 있을 때, 이 데이터를 학습하여 다음 년도의 각 도시별 폭염 일 수를 예측하고 싶어. 어떤 모델을 사용해야할까?


# import pandas as pd
# import matplotlib.pyplot as plt

# from sklearn.ensemble import RandomForestRegressor
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import mean_squared_error

# #========================================= graph =========================================

# # DataFrame 생성
# data = utils.loadData()
# df = pd.DataFrame(data)

# # bas_yy 년도 컬럼을 정수형으로 변환
# df['bas_yy'] = df['bas_yy'].astype(int)

# # 시각화를 위한 그래프 생성
# fig, axs = plt.subplots(2, 3, figsize=(15, 10))

# # 각 도시별 폭염 일수 그래프 그리기
# cities = ['lseoul', 'lgangneung', 'ldaejeon', 'ldaegu', 'lgwangju', 'lbusan']
# for i, city in enumerate(cities):
#     row = i // 3
#     col = i % 3
#     # bas_yy 년도를 기준으로 정렬하여 그래프 그리기
#     sorted_df = df.sort_values(by='bas_yy')
#     axs[row, col].plot(sorted_df['bas_yy'], sorted_df[city].astype(int), marker='o')
#     axs[row, col].set_title(city)
#     axs[row, col].set_xlabel('Year')
#     axs[row, col].set_ylabel('Heat Wave Days')
#     axs[row, col].grid(True)  # 그리드 추가

# # 전국 평균 폭염 일수 그래프 추가
# axs[1, 2].plot(sorted_df['bas_yy'], sorted_df['anat_dd_avg'].astype(float), marker='o', color='r')
# axs[1, 2].set_title('Average Nationwide Heat Wave Days')
# axs[1, 2].set_xlabel('Year')
# axs[1, 2].set_ylabel('Heat Wave Days')
# axs[1, 2].grid(True)  # 그리드 추가

# # 그래프 레이아웃 조정 및 출력
# plt.tight_layout()
# plt.show()
# #========================================= graph =========================================


# # DataFrame 생성
# df = pd.DataFrame(data)

# # bas_yy 년도 컬럼을 정수형으로 변환
# df['bas_yy'] = df['bas_yy'].astype(int)

# # 2020년까지의 데이터를 학습 데이터로, 2021년 데이터를 예측할 데이터로 분할
# X_train = df.loc[df['bas_yy'] <= 2020].drop(['bas_yy', 'anat_dd_avg'], axis=1).astype(float)
# y_train = df.loc[df['bas_yy'] <= 2020, 'anat_dd_avg'].astype(float)
# X_test = df.loc[df['bas_yy'] >= 2021].drop(['bas_yy', 'anat_dd_avg'], axis=1).astype(float)
# y_test = df.loc[df['bas_yy'] >= 2021, 'anat_dd_avg'].astype(float)

# # 랜덤 포레스트 모델 초기화 및 학습
# rf_model = RandomForestRegressor(random_state=42)
# rf_model.fit(X_train, y_train)

# # 2021년과 2022년의 폭염일수 예측
# predicted_values = rf_model.predict(X_test)
# predictions = pd.Series(predicted_values, index=X_test.index)

# # 예측 결과를 기반으로 상위 3개 도시 추출
# top_cities_2021 = predictions.nlargest(3).index.tolist()
# top_cities_2022 = predictions.nlargest(3).index.tolist()

# # 결과 출력
# print("2021년 가장 폭염일수가 많을 것으로 예측되는 도시 Top 3:")
# print(df.loc[top_cities_2021, ['bas_yy'] + X_test.columns.tolist()])

# print("\n2022년 가장 폭염일수가 많을 것으로 예측되는 도시 Top 3:")
# print(df.loc[top_cities_2022, ['bas_yy'] + X_test.columns.tolist()])

