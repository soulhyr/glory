import streamlit as st

st.text('''인원별 할수 있는 일과 하고 싶은 일을 나열하여, 이를 토대로 어떠한 역할을 맡을 지 협의하였습니다.''')


tab1, tab2 = st.tabs(["황영록", "김연진", ])

with tab1:
   st.header("황영록")
   st.code('''
할 수 있는 일 : Python, Machine Learning, Data Analysis
하고 싶은 역할 : 머신러닝
Main Job : Data Collection, Data Analysis, Machine Learning
           ''')
   st.image("https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjA5MTBfMTY3%2FMDAxNjYyODEwNDg0NjAw.4_Dq0XubE16neXJQn28ozDY3a0mAfnzrAP4f6YZ7Izgg.GMapOCzOaW1SGtr-94vxpEwdQE9ikRVh8NI3duogeFAg.JPEG.rothmans17%2FScreenshot%25A3%25DF20220910%25A3%25AD204733%25A3%25DFNAVER.jpg&type=a340", 
            width=400)

with tab2:
   st.header("김연진")
   st.code('''
할 수 있는 일 : Python, Graph module, Data Analysis
하고 싶은 역할 : 수집 및 시각화
Main Job : Data Analysis, Web-App (with Graph)
           ''')
   st.image("https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMzAyMDVfMTk0%2FMDAxNjc1NTYxMDUzMjk2.wS-TXN2YQTcAD8Em2Ujb3Y0jAqnnbn8fmFWStIybRRQg.83Q6ULEQwgdv-6--t2dXvaraU042f0ooCQiX4MEg6Dsg.PNG.lenglishdream%2Fimage.png&type=a340", 
            width=400)