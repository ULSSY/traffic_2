import streamlit as st
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def run_eda_app():
    

    
    df1=df.loc[:,'발생건수':'부상신고']
    fig = px.bar(        
        df,
        x = "시도",
        y = "발생건수",
        title = "시도별 발생건수"
        )
    st.plotly_chart(fig)    
    fig1 = px.bar(        
        df,
        x = "시도",
        y = "사망자수",
        title = "시도별 사망자수"
        )
    st.plotly_chart(fig1)    
    fig2 = px.bar(        
        df,
        x = "시도",
        y = "부상자수",
        title = "시도별 부상자수"
        )
    st.plotly_chart(fig2)    
    fig3 = px.bar(        
        df,
        x = "시도",
        y = "중상",
        title = "시도별 중상"
        )
    st.plotly_chart(fig3)    
    fig4 = px.bar(        
        df,
        x = "시도",
        y = "경상",
        title = "시도별 경상"
        )
    st.plotly_chart(fig4)    
    fig5 = px.bar(        
        df,
        x = "시도",
        y = "부상신고",
        title = "시도별 부상신고"
        )   
    st.plotly_chart(fig5)    

   
    st.line_chart(data=df1, width=0, height=0, use_container_width=True)
    
    
    # radio_menu=['인천','경기','강원','서울']
    # selected_radio=st.radio('시도를 선택하세요',radio_menu)
    # if radio_menu=='인천':
    #         radio_menu=['중구','동구','남구']
    #         selected_radio=st.radio('시군구를 선택하세요',radio_menu)
    #         if radio_menu=='중구':
                # st.dataframe(df)
                # st.subheader('Nan 데이터 확인')
                # st.dataframe(df.isna().sum())
                # st.subheader('각 컬럼별 히스토그램 확인')

                # selected_column=st.selectbox('컬럼을 선택하세요',df.columns)

                # bins=st.slider('bin의 갯수 조절',min_value=10,max_value=50)

                # fig1=plt.figure()
                # df[selected_column].hist(bins=bins)
                # st.pyplot(fig1)

       
    # #컬럼을 선택하면 해당 컬럼들만 데이터프레임 표시하는 화면
    # print(df.columns)

    # selected_columns=st.multiselect('컬럼을 선택하세요',df.columns)
    # if len(selected_columns) !=0:
    #     st.dataframe(df[selected_columns])
    # else: 
    #     st.write('선택한 컬럼이 없습니다.')

    # # 상관계수 분석을 위한, 상관계수 보여주는 화면 개발
    # st.subheader('상관계수')
     
    # #st.dataframe(df.corr())
    # df_corr=df.iloc[:,3:]
    # st.dataframe(df_corr)

    # selected_corr=st.multiselect('상관계수 컬럼 선택',df_corr.columns)

    # if len(selected_corr)>0:
    #     st.dataframe(df_corr[selected_corr].corr())

    #     #상관계수를 수치로도 구하고 차트로도 표시하라
    #     fig1=sns.pairplot(data=df_corr[selected_corr])

    #     st.pyplot(fig1) 

    # #유저가 컬럼을 선택하지 않은 경우
    # else:
    #     st.write('선택한 컬럼이 없습니다.')

    # #유저가 컬럼을 선택하면
    # #해당 컬럼의min과 max에 해당하는 사람이 누구인지
    # #그 사람의 데이터를 화면에 보여주는 기능 개발

    # #문자열 데이터가 아닌 컬럼들만 가져오는 코드
    # print(df.columns)

    # print(df.dtypes != object)

    # print(df.columns[df.dtypes != object])
    # number_columns=df.columns[df.dtypes != object]

    # selected_minmax_column=st.selectbox('컬럼선택',number_columns)

    # #선택한 컬럼의 최소값에 해당되는 사람의 데이터 출력
    # min_data=df[selected_minmax_column]==df[selected_minmax_column].min
    # st.dataframe(min_data)
    # #선택한 컬럼의 최대값에 해당되는 사람의 데이터 출력
    
    # max_data=df[selected_minmax_column]==df[selected_minmax_column].max
    # st.dataframe(max_data)
    # #고객의 이름을 검색할 수 있는 기능 개발
    # st.subheader('발생건수')
    # #1. 유저한테 검색어 입력을 받습니다.
    # word=st.text_input('검색어를 입력하세요')
    # print(word)
    # #2.검색어를 데이터프레임의 Customer Name컬럼에서 검색해서 가져온다
    
    # df_search=df.loc[df['시군구'].str.lower().str.contains(word),]
    # #3.화면에 결과를 보여준다
    # st.dataframe(df_search)