import streamlit as st
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def run_eda_app():
    

    df=pd.read_csv('data/도로교통.csv',encoding='CP949')
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
    