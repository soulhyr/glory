import streamlit as st

# """
# 여기에 streamlit 사이트에서 본 것 중 맘에 드는 템플릿 하나 넣어서 화면 만들어도 되요!! 아니면 직접 꾸미셔도 됩니다!!


# 요구 기능 1 : API 호출 기능
# 클릭 시 연동한 API 를 호출하여 즉시 데이터를 갱신하게 해주는 기능. (설정할 수 있는 변수들도 있어야 함. 년도 범위 라던가~)

# => 터미널에서 아래 코드 실행 시 api 연동됩니다. 개발에 참고하세요.
# python api.py


# 요구 기능 2 : 저장된 데이터(json)를 토대로 그래프와 표로 시각화!! (pandas, streamlit-echarts 등 모듈 사용!)
#         (해당 데이터로 인사이트를 도출해보세요!)

# 요구 기능 3 : About
# 조원 및 프로젝트, 결과물 설명 등.
# """

about = st.Page("view/about.py", title="About", icon=":material/search:", default=True)
member = st.Page("view/member.py", title="Member", icon=":material/history:")
collection = st.Page("view/collection.py", title="Collection", icon=":material/history:")
bugs = st.Page("view/analysis.py", title="Analysis", icon=":material/dashboard:")
alerts = st.Page("view/ml.py", title="Machine Learning", icon=":material/notification_important:")

# history = st.Page("view/history.py", title="History", icon=":material/history:")

pg = st.navigation(
    {
        "About": [about, member],
        "Works": [collection, bugs, alerts],
    }
)

pg.run()

# import streamlit as st

# # Define function to render different pages
# def main():
#     st.sidebar.title('Navigation')
#     page = st.sidebar.radio('Go to', ('Home', 'About', 'Contact'))

#     if page == 'Home':
#         st.title('Home Page')
#         st.write('Welcome to the Home Page')

#     elif page == 'About':
#         st.title('About Page')
#         st.write('This is the About Page')

#     elif page == 'Contact':
#         st.title('Contact Page')
#         st.write('Contact us here')

# if __name__ == "__main__":
#     main()
