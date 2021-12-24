import streamlit as st
import pandas as pd
import numpy as np
import os
import pickle
from PIL import Image
from ml_app import run_ml_app
import matplotlib.pyplot as plt
import matplotlib.image as img
import plotly.express as px
from eda_app import run_eda_app
from now_app import run_now_app 
# from 
# 자동으로 비주얼 코드가 임포트 해준다


def main():
    st.title('교통사고 현황 확인하기')
    

    #사이드바 메뉴
    menu=['처음화면','시도별 현황','시군구 현황','데이터분석']
    choice=st.sidebar.selectbox('메뉴',menu)

    if choice=='처음화면':
        
        df=pd.read_csv('data/도로교통.csv',encoding='CP949')
        df1=df.loc[:,'발생건수':'부상신고']
        st.image('data/교통.jpg',use_column_width=True)
        st.write('교통사고 현황을 확인하실 수 있습니다.')
        st.write('왼쪽의 사이드바에서 선택하세요')
        
    elif choice =='시도별 현황' :
        run_eda_app()

    elif choice =='시군구 현황':
        run_now_app()
    elif choice == '데이터분석':
        run_ml_app()
        
      
if __name__ =='__main__':
    main()