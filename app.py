import streamlit as st
from home import run_home

def main () :
    st.title('포켓몬 데이터 측정')

    menu = ['메인화면','분석정보','랭크측정','그래프','그룹 군집']

    choice = st.sidebar.selectbox('메뉴',menu)

    if choice == menu[0]:
        run_home()
    