import streamlit as st
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def run_eda_app():
    

    df=pd.read_csv('data/���α���.csv',encoding='CP949')
    df1=df.loc[:,'�߻��Ǽ�':'�λ�Ű�']
    fig = px.bar(        
        df,
        x = "�õ�",
        y = "�߻��Ǽ�",
        title = "�õ��� �߻��Ǽ�"
        )
    st.plotly_chart(fig)    
    fig1 = px.bar(        
        df,
        x = "�õ�",
        y = "����ڼ�",
        title = "�õ��� ����ڼ�"
        )
    st.plotly_chart(fig1)    
    fig2 = px.bar(        
        df,
        x = "�õ�",
        y = "�λ��ڼ�",
        title = "�õ��� �λ��ڼ�"
        )
    st.plotly_chart(fig2)    
    fig3 = px.bar(        
        df,
        x = "�õ�",
        y = "�߻�",
        title = "�õ��� �߻�"
        )
    st.plotly_chart(fig3)    
    fig4 = px.bar(        
        df,
        x = "�õ�",
        y = "���",
        title = "�õ��� ���"
        )
    st.plotly_chart(fig4)    
    fig5 = px.bar(        
        df,
        x = "�õ�",
        y = "�λ�Ű�",
        title = "�õ��� �λ�Ű�"
        )   
    st.plotly_chart(fig5)    

   
    st.line_chart(data=df1, width=0, height=0, use_container_width=True)
    