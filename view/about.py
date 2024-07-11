import streamlit as st

about = """
본 사이트는 실습 프로젝트의 계획부터 실습 결과까지 그 내용을 설명하는데 목적이 있습니다.
이에 아래와 같이 각 파트별로 내용을 소개합니다.

** Site Guide **

:blue-background[**1. About**]

- **About** : 사이트에 대한 간략한 설명 기재.
- **Member** : 실습 프로젝트의 구성원 및 역할에 대한 소개.
- **Plan** : 실습 프로젝트 진행에 대한 전반적 계획 소개.

:green-background[**2. Works**]

- **Collection** : 수집에 대한 기능 실습 내용.
- **Analysis** : 분석에 대한 기능 실습 내용.
- **Machine Learnin** : ML 에 대한 기능 실습 내용.
"""
st.markdown(about)
