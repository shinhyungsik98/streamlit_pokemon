import streamlit as st
import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt

def run_graph () :
    df=pd.read_csv('./data/Pokemon.csv')

    st.subheader('그래프 분석')
    st.text('세대별 포켓몬 스탯분포')

    radio_menu = ['체력','공격','방어','특수공격','특수방어','속도']

    choice=st.selectbox('선택하세요',radio_menu)
    if choice == radio_menu [0] :
        fig, ax = plt.subplots()
        sb.regplot(x='세대', y='체력', data=df, ax=ax)

        st.pyplot(fig)

        

    elif choice == radio_menu [1] :
        fig, ax = plt.subplots()
        sb.regplot(x='세대', y='공격', data=df, ax=ax)

        st.pyplot(fig)


    elif choice == radio_menu [2] :
        fig, ax = plt.subplots()
        sb.regplot(x='세대', y='방어', data=df, ax=ax)

        st.pyplot(fig)

    elif choice == radio_menu [3] :
        fig, ax = plt.subplots()
        sb.regplot(x='세대', y='속도', data=df, ax=ax)

        st.pyplot(fig)

    elif choice == radio_menu [4] :
        fig, ax = plt.subplots()
        sb.regplot(x='세대', y='특수공격', data=df, ax=ax)

        st.pyplot(fig) 

    elif choice == radio_menu [5] :
        fig, ax = plt.subplots()
        sb.regplot(x='세대', y='특수방어', data=df, ax=ax)

        st.pyplot(fig)  

    elif choice == radio_menu [6] :
        fig, ax = plt.subplots()
        sb.regplot(x='세대', y='속도', data=df, ax=ax)

        st.pyplot(fig)  


    st.text('속성별 스탯 비교')

    radio_menu = ['체력','공격','방어','특수공격','특수방어','속도']

    choice=st.radio('선택하세요',radio_menu)
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