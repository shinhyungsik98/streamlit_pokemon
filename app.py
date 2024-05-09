import streamlit as st
from home import run_home
from eda import run_eda
from ml import run_ml
from graph import run_graph

def main () :
    st.title('포켓몬 데이터 측정')

    menu = ['메인화면','분석정보','파워랭크','그래프']

    choice = st.sidebar.selectbox('메뉴',menu)
    image_path = ('./image/poke4.jpg')
    st.sidebar.image(image_path)

    if choice == menu[0]:
        run_home()
    elif choice == menu[1] :
        run_eda()
    elif choice == menu[2] :
        run_ml()
    elif choice == menu[3] :
        run_graph()


if __name__ == '__main__' :
    main()