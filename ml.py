import streamlit as st
import joblib
import numpy as np


def calculate_grade(power):
    if power >= 150:
        return "SS급"
    elif power >= 100:
        return "S급"
    elif power >= 75:
        return "A급"
    elif power >= 50:
        return "B급"
    elif power >= 25:
        return "C급"
    else:
        return "D급"

def run_ml():
    st.subheader('나의 포켓몬 파워랭크 예측')
    st.subheader('내가 잡은 포켓몬의 데이터를 기입하자!')

    st.image('./image/poke1.png')
    
    st.text('● 체력을 입력하세요')
    hp = st.number_input('체력입력', min_value=0, max_value=300, value=100, step=5)

    st.text('● 공격력을 입력하세요')
    atk = st.number_input('공격력 입력', min_value=0, max_value=200, value=100, step=5)

    st.text('● 방어력을 입력하세요')
    defense = st.number_input('방어력 입력', min_value=0, max_value=250, value=100, step=5)

    st.text('● 특수공격력을 입력하세요')
    spatk = st.number_input('특수공격력 입력', min_value=0, max_value=200, value=100, step=5)

    st.text('● 특수방어력을 입력하세요')
    spdef = st.number_input('특수방어력 입력', min_value=0, max_value=250, value=100, step=5)

    st.text('● 속도를 입력하세요')
    speed = st.number_input('속도입력', min_value=0, max_value=200, value=100, step=5)

    st.subheader('내 포켓몬의 파워랭크는???')

    if st.button('예측하기'):
        regressor = joblib.load('./model/regressor.pkl')
        new_data = np.array([hp, atk, defense, spatk, spdef, speed]).reshape(1, -1)
        y_pred = regressor.predict(new_data)
        grade = calculate_grade(y_pred)

        y_pred=y_pred[0]
        y_pred = round(y_pred)

        
        st.write(f'예측된 포켓몬의 파워: {y_pred}')
        st.write(f'등급: {grade}')