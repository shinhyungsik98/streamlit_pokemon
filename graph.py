import streamlit as st
import seaborn as sb
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import platform
from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False
if platform.system() == 'Linux':
    rc('font', family='NanumGothic')

def run_graph () :
    df=pd.read_csv('./data/Pokemon.csv')


    st.image('./image/poke3.png')

    st.subheader('스탯별 개체수 분포도')

    numeric_columns = ['체력','공격','방어','특수공격','특수방어','속도']
    pokemon_numeric = df[numeric_columns].to_numpy()


    # 선택 상자에 숫자 열 표시
    selected_column = st.selectbox("원하는 데이터 선택", numeric_columns)

    # 선택한 열에 대한 인덱스 가져오기
    selected_index = numeric_columns.index(selected_column)

    # 선택한 열에 대한 히스토그램 생성
    plt.hist(pokemon_numeric[:, selected_index], bins=20, color='skyblue', edgecolor='black')
    plt.title(f"{selected_column}")
    plt.xlabel(selected_column)
    plt.ylabel('개체수')
    plt.xlabel('스탯수치')

    

    # 스트림릿에 플롯 출력
    st.pyplot(plt.gcf())





    st.subheader('세대별 포켓몬 스탯분포')

    radio_menu = ['체력','공격','방어','특수공격','특수방어','속도']

    choice=st.selectbox('선택하세요',radio_menu)
    if choice == radio_menu[0]:
       fig, ax = plt.subplots()
       sb.boxplot(x='세대', y='체력', data=df, ax=ax)
       ax.set_title('각 세대에 체력 분포')
       st.pyplot(fig)

        

    elif choice == radio_menu [1] :
        fig, ax = plt.subplots()
        sb.boxplot(x='세대', y='공격', data=df, ax=ax)
        ax.set_title('각 세대별 공격력 분포')
        st.pyplot(fig)

    elif choice == radio_menu [2] :
        fig, ax = plt.subplots()
        sb.boxplot(x='세대', y='방어', data=df, ax=ax)
        ax.set_title('각 세대별 방어력 분포')
        st.pyplot(fig)

    elif choice == radio_menu [3] :
        fig, ax = plt.subplots()
        sb.boxplot(x='세대', y='특수공격', data=df, ax=ax)
        ax.set_title('각 세대별 특수공격력 분포')
        st.pyplot(fig)

    elif choice == radio_menu [4] :
        fig, ax = plt.subplots()
        sb.boxplot(x='세대', y='특수방어', data=df, ax=ax)
        ax.set_title('각 세대별 특수방어력 분포')
        st.pyplot(fig)


    elif choice == radio_menu [5] :
        fig, ax = plt.subplots()
        sb.boxplot(x='세대', y='속도', data=df, ax=ax)
        ax.set_title('각 세대별 속도 분포')
        st.pyplot(fig)


    st.subheader('속성별 평균스탯 비교')

    radio_menu = ['체력','공격','방어','특수공격','특수방어','속도']

    choice=st.selectbox('선택하세요',radio_menu,key=1)
    if choice == radio_menu [0] :
        average_health = df.groupby('속성')['체력'].mean()
        st.bar_chart(average_health)
    elif choice == radio_menu [1] :
        average_attack = df.groupby('속성')['공격'].mean()
        st.bar_chart(average_attack)
    elif choice == radio_menu [2] :
        average_defense = df.groupby('속성')['방어'].mean()
        st.bar_chart(average_defense)   
    elif choice == radio_menu [3] :
        average_spa = df.groupby('속성')['특수공격'].mean()
        st.bar_chart(average_spa)   
    elif choice == radio_menu [4] :
        average_spd = df.groupby('속성')['특수방어'].mean()
        st.bar_chart(average_spd)    
    elif choice == radio_menu [5] :
        average_speed = df.groupby('속성')['속도'].mean()
        st.bar_chart(average_speed)        