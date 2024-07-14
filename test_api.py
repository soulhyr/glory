import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# 주어진 데이터
data = [
    {"bas_yy": "2007", "lseoul": "4", "lgangneung": "13", "ldaejeon": "5", "ldaegu": "23", "lgwangju": "12", "lbusan": "0", "anat_dd_avg": "8.9"},
    {"bas_yy": "2008", "lseoul": "3", "lgangneung": "13", "ldaejeon": "3", "ldaegu": "36", "lgwangju": "18", "lbusan": "0", "anat_dd_avg": "11.2"},
    {"bas_yy": "2009", "lseoul": "4", "lgangneung": "4", "ldaejeon": "0", "ldaegu": "18", "lgwangju": "6", "lbusan": "0", "anat_dd_avg": "3.6"},
    {"bas_yy": "2010", "lseoul": "2", "lgangneung": "19", "ldaejeon": "10", "ldaegu": "41", "lgwangju": "20", "lbusan": "3", "anat_dd_avg": "12.2"},
    {"bas_yy": "2011", "lseoul": "3", "lgangneung": "8", "ldaejeon": "1", "ldaegu": "29", "lgwangju": "13", "lbusan": "1", "anat_dd_avg": "6.5"},
    {"bas_yy": "2012", "lseoul": "14", "lgangneung": "10", "ldaejeon": "17", "ldaegu": "30", "lgwangju": "25", "lbusan": "7", "anat_dd_avg": "14.0"},
    {"bas_yy": "2013", "lseoul": "2", "lgangneung": "26", "ldaejeon": "16", "ldaegu": "54", "lgwangju": "22", "lbusan": "13", "anat_dd_avg": "16.6"},
    {"bas_yy": "2014", "lseoul": "10", "lgangneung": "9", "ldaejeon": "5", "ldaegu": "22", "lgwangju": "8", "lbusan": "0", "anat_dd_avg": "6.6"},
    {"bas_yy": "2015", "lseoul": "8", "lgangneung": "9", "ldaejeon": "12", "ldaegu": "21", "lgwangju": "14", "lbusan": "1", "anat_dd_avg": "9.6"},
    {"bas_yy": "2016", "lseoul": "24", "lgangneung": "12", "ldaejeon": "29", "ldaegu": "32", "lgwangju": "31", "lbusan": "9", "anat_dd_avg": "22.0"},
    {"bas_yy": "2017", "lseoul": "13", "lgangneung": "12", "ldaejeon": "14", "ldaegu": "33", "lgwangju": "29", "lbusan": "6", "anat_dd_avg": "13.5"},
    {"bas_yy": "2018", "lseoul": "35", "lgangneung": "23", "ldaejeon": "37", "ldaegu": "40", "lgwangju": "43", "lbusan": "18", "anat_dd_avg": "31.0"},
    {"bas_yy": "2019", "lseoul": "15", "lgangneung": "20", "ldaejeon": "18", "ldaegu": "29", "lgwangju": "12", "lbusan": "3", "anat_dd_avg": "13.1"},
    {"bas_yy": "2020", "lseoul": "4", "lgangneung": "16", "ldaejeon": "13", "ldaegu": "31", "lgwangju": "13", "lbusan": "4", "anat_dd_avg": "7.7"},
    {"bas_yy": "2021", "lseoul": "18", "lgangneung": "11", "ldaejeon": "21", "ldaegu": "23", "lgwangju": "14", "lbusan": "3", "anat_dd_avg": "11.8"},
    {"bas_yy": "2022", "lseoul": "10", "lgangneung": "16", "ldaejeon": "22", "ldaegu": "45", "lgwangju": "19", "lbusan": "1", "anat_dd_avg": "10.6"}
]

# 데이터 프레임으로 변환
df = pd.DataFrame(data)

# 각 도시의 폭염 일 수 데이터만 추출
X = df[['bas_yy']].astype(int)  # 연도 정보를 정수형으로 변환하여 사용
y_seoul = df['lseoul'].astype(int)
y_gangneung = df['lgangneung'].astype(int)
y_daejeon = df['ldaejeon'].astype(int)
y_daegu = df['ldaegu'].astype(int)
y_gwangju = df['lgwangju'].astype(int)
y_busan = df['lbusan'].astype(int)

# 선형 회귀 모델 초기화
model_seoul = LinearRegression()
model_gangneung = LinearRegression()
model_daejeon = LinearRegression()
model_daegu = LinearRegression()
model_gwangju = LinearRegression()
model_busan = LinearRegression()

# 모델 훈련
model_seoul.fit(X, y_seoul)
model_gangneung.fit(X, y_gangneung)
model_daejeon.fit(X, y_daejeon)
model_daegu.fit(X, y_daegu)
model_gwangju.fit(X, y_gwangju)
model_busan.fit(X, y_busan)

# 2023년 데이터 생성
X_2023 = np.array([[2023]])

# 각 도시의 폭염 일 수 예측
pred_seoul = model_seoul.predict(X_2023)[0]
pred_gangneung = model_gangneung.predict(X_2023)[0]
pred_daejeon = model_daejeon.predict(X_2023)[0]
pred_daegu = model_daegu.predict(X_2023)[0]
pred_gwangju = model_gwangju.predict(X_2023)[0]
pred_busan = model_busan.predict(X_2023)[0]

# 예측 결과 출력
print(f"서울 예상 폭염 일 수 (2023년): 약 {pred_seoul:.1f}일")
print(f"강릉 예상 폭염 일 수 (2023년): 약 {pred_gangneung:.1f}일")
print(f"대전 예상 폭염 일 수 (2023년): 약 {pred_daejeon:.1f}일")
print(f"대구 예상 폭염 일 수 (2023년): 약 {pred_daegu:.1f}일")
print(f"광주 예상 폭염 일 수 (2023년): 약 {pred_gwangju:.1f}일")
print(f"부산 예상 폭염 일 수 (2023년): 약 {pred_busan:.1f}일")


