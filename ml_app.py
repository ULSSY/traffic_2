import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib
import seaborn as sb
import plotly.express as px
def run_ml_app() :
    st.subheader('Machine Learning 예측')

    df = pd.read_csv('data/도로교통.csv', encoding='CP949')
    df1=df.loc[:,'발생건수':'부상신고']
    # 1. 유저한테, 데이터를 입력받습니다.
    print(df)
    gender=st.radio('시도를 입력하세요',['인천', '경기','강원','서울','세종','충북','충남','광주','대전','전북','전남','대구','부산','울산','경북','경남'])
    
    if gender == '인천' :
        st.selectbox('시군구를 입력하세요.', ['중구', '동구','남구','부평구','남동구','서구','연수구','계양구'])
        selected_column=st.selectbox('컬럼을 선택하세요',df1.columns)
        st.subheader('각 컬럼별 히스토그램 확인')
       
     
        st.subheader('각 컬럼별 통계치')
        st.dataframe(df.describe())

    elif gender == '경기' :
        st.selectbox('시군구를 입력하세요.', ['수원시', '성남시','의정부시','안양시','부천시','안산시','평택시','광명시','구리시','양주시','여주시','화성시','시흥시','고양시','광주시','포천시','가평군','양평군','이천시','용인시','안성시','김포시','군포시','남양주시','오산시','의왕시','하남시'])
        st.subheader('각 컬럼별 히스토그램 확인')

        selected_column=st.selectbox('컬럼을 선택하세요',df1.columns)

        bins=st.slider('bin의 갯수 조절',min_value=10,max_value=50)

        fig1=plt.figure()
        df[selected_column].hist(bins=bins)
        st.pyplot(fig1)

        st.subheader('각 컬럼별 통계치')
        st.dataframe(df.describe())
    elif gender == '강원' :
        st.selectbox('시군구를 입력하세요.', ['춘천시', '원주시','동해시','강릉시','속초시','홍천군','횡성군','평창군','인제군','양양군'])
        st.subheader('각 컬럼별 히스토그램 확인')

        selected_column=st.selectbox('컬럼을 선택하세요',df1.columns)

        bins=st.slider('bin의 갯수 조절',min_value=10,max_value=50)

        fig1=plt.figure()
        df[selected_column].hist(bins=bins)
        st.pyplot(fig1)

        st.subheader('각 컬럼별 통계치')
        st.dataframe(df.describe())
    elif gender == '서울' :
        st.selectbox('시군구를 입력하세요.', ['성북구', '강서구','강남구','강동구','송파구','서초구','양천구','중랑구','노원구','금천구'])
        st.subheader('각 컬럼별 히스토그램 확인')

        selected_column=st.selectbox('컬럼을 선택하세요',df1.columns)

        bins=st.slider('bin의 갯수 조절',min_value=10,max_value=50)

        fig1=plt.figure()
        df[selected_column].hist(bins=bins)
        st.pyplot(fig1)

        st.subheader('각 컬럼별 통계치')
        st.dataframe(df.describe())
    elif gender == '세종' :
        st.selectbox('시군구를 입력하세요.', ['세종'])
        st.subheader('각 컬럼별 히스토그램 확인')

        selected_column=st.selectbox('컬럼을 선택하세요',df1.columns)

        bins=st.slider('bin의 갯수 조절',min_value=10,max_value=50)

        fig1=plt.figure()
        df[selected_column].hist(bins=bins)
        st.pyplot(fig1)

        st.subheader('각 컬럼별 통계치')
        st.dataframe(df.describe())
    elif gender == '충북' :
        st.selectbox('시군구를 입력하세요.', ['청주시', '충주시','제천시','보은군','옥천군','영동군','진천군','괴산군','음성군','단양군','증평군'])
        st.subheader('각 컬럼별 히스토그램 확인')

        selected_column=st.selectbox('컬럼을 선택하세요',df1.columns)

        bins=st.slider('bin의 갯수 조절',min_value=10,max_value=50)

        fig1=plt.figure()
        df[selected_column].hist(bins=bins)
        st.pyplot(fig1)

        st.subheader('각 컬럼별 통계치')
        st.dataframe(df.describe())
    elif gender == '충남' :
        st.selectbox('시군구를 입력하세요.', ['천안시', '보령시','공주시','서산시','금산군','논산시','부여군','서천군','청양군','홍성군','예산군','당진시','계룡시'])
        st.subheader('각 컬럼별 히스토그램 확인')

        selected_column=st.selectbox('컬럼을 선택하세요',df1.columns)

        bins=st.slider('bin의 갯수 조절',min_value=10,max_value=50)

        fig1=plt.figure()
        df[selected_column].hist(bins=bins)
        st.pyplot(fig1)

        st.subheader('각 컬럼별 통계치')
        st.dataframe(df.describe())
    elif gender == '광주' :
        st.selectbox('시군구를 입력하세요.', ['북구', '광산구'])
        st.subheader('각 컬럼별 히스토그램 확인')

        selected_column=st.selectbox('컬럼을 선택하세요',df1.columns)

        bins=st.slider('bin의 갯수 조절',min_value=10,max_value=50)

        fig1=plt.figure()
        df[selected_column].hist(bins=bins)
        st.pyplot(fig1)

        st.subheader('각 컬럼별 통계치')
        st.dataframe(df.describe())
    elif gender == '대전' :
        st.selectbox('시군구를 입력하세요.', ['동구', '중구','서구','유성구','대덕구'])
        st.subheader('각 컬럼별 히스토그램 확인')

        selected_column=st.selectbox('컬럼을 선택하세요',df1.columns)

        bins=st.slider('bin의 갯수 조절',min_value=10,max_value=50)

        fig1=plt.figure()
        df[selected_column].hist(bins=bins)
        st.pyplot(fig1)

        st.subheader('각 컬럼별 통계치')
        st.dataframe(df.describe())
    elif gender == '전북' :
        st.selectbox('시군구를 입력하세요.', ['전주시', '군산시','정읍시','남원시','김제시','완주군','무주군','장수군','임실군','순창군','고창군','부안군','익산시'])
        st.subheader('각 컬럼별 히스토그램 확인')

        selected_column=st.selectbox('컬럼을 선택하세요',df1.columns)

        bins=st.slider('bin의 갯수 조절',min_value=10,max_value=50)

        fig1=plt.figure()
        df[selected_column].hist(bins=bins)
        st.pyplot(fig1)

        st.subheader('각 컬럼별 통계치')
        st.dataframe(df.describe())
    elif gender == '전남' :
        st.selectbox('시군구를 입력하세요.', ['목포시', '순천시','나주시','광양시','담양군','곡성군','구례군','보성군','장흥군','강진군','무안군','함평군','영광군','장성군'])
        st.subheader('각 컬럼별 히스토그램 확인')

        selected_column=st.selectbox('컬럼을 선택하세요',df1.columns)

        bins=st.slider('bin의 갯수 조절',min_value=10,max_value=50)

        fig1=plt.figure()
        df[selected_column].hist(bins=bins)
        st.pyplot(fig1)

        st.subheader('각 컬럼별 통계치')
        st.dataframe(df.describe())
    elif gender == '대구' :
        st.selectbox('시군구를 입력하세요.', ['동구', '서구','북구','수성구','달서구','달성군'])
        st.subheader('각 컬럼별 히스토그램 확인')

        selected_column=st.selectbox('컬럼을 선택하세요',df1.columns)

        bins=st.slider('bin의 갯수 조절',min_value=10,max_value=50)

        fig1=plt.figure()
        df[selected_column].hist(bins=bins)
        st.pyplot(fig1)

        st.subheader('각 컬럼별 통계치')
        st.dataframe(df.describe())
    elif gender == '부산' :
        st.selectbox('시군구를 입력하세요.', ['북구', '해운대구','금정구','강서구','사상구','기장군'])
        st.subheader('각 컬럼별 히스토그램 확인')

        selected_column=st.selectbox('컬럼을 선택하세요',df1.columns)

        bins=st.slider('bin의 갯수 조절',min_value=10,max_value=50)

        fig1=plt.figure()
        df[selected_column].hist(bins=bins)
        st.pyplot(fig1)

        st.subheader('각 컬럼별 통계치')
        st.dataframe(df.describe())
    elif gender == '울산' :
        st.selectbox('시군구를 입력하세요.', ['울주군'])
        st.subheader('각 컬럼별 히스토그램 확인')

        selected_column=st.selectbox('컬럼을 선택하세요',df1.columns)

        bins=st.slider('bin의 갯수 조절',min_value=10,max_value=50)

        fig1=plt.figure()
        df[selected_column].hist(bins=bins)
        st.pyplot(fig1)

        st.subheader('각 컬럼별 통계치')
        st.dataframe(df.describe())
    elif gender == '경북' :
        st.selectbox('시군구를 입력하세요.', ['포항시', '경주시','나주시','김천시','안동시','구미시','영주시','영천시','문경시','상주시','군위군','의성군','청도군','고령군','성주군','칠곡군','예천군','경산시'])
        st.subheader('각 컬럼별 히스토그램 확인')

        selected_column=st.selectbox('컬럼을 선택하세요',df1.columns)

        bins=st.slider('bin의 갯수 조절',min_value=10,max_value=50)

        fig1=plt.figure()
        df[selected_column].hist(bins=bins)
        st.pyplot(fig1)

        st.subheader('각 컬럼별 통계치')
        st.dataframe(df.describe())
    elif gender == '경남' :
        st.selectbox('시군구를 입력하세요.', ['진주시', '통영시','김해시','밀양시','함안군','창녕군','양산시','고성군','사천시','하동군','산청군','함양군','거창군','창원시'])
        st.subheader('각 컬럼별 히스토그램 확인')

        selected_column=st.selectbox('컬럼을 선택하세요',df1.columns)

        bins=st.slider('bin의 갯수 조절',min_value=10,max_value=50)

        fig1=plt.figure()
        df[selected_column].hist(bins=bins)
        st.pyplot(fig1)

        st.subheader('각 컬럼별 통계치')
        st.dataframe(df.describe())