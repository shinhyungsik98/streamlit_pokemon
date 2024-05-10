import streamlit as st

def run_home() :
    st.subheader('포켓몬들의 스탯을 분석하여 파워랭킹을 확인가능')
    st.text('데이터는 kaggle의 pokemon.csv 파일을 사용하였습니다.')
    st.text('출처 주소')
    kaggle_link = "[Kaggle Pokemon Pokedex](https://www.kaggle.com/datasets/arnavvvvv/pokemon-pokedex)"
    st.markdown(kaggle_link, unsafe_allow_html=True)

    st.text('탐색적 데이터분석, 수치 그래프화, 머신러닝을 활용하여 다양정보를 볼수있습니다.')
    st.image('./image/poke.png',use_column_width=True)
    
    st.subheader('문맥')
    st.text('이 데이터 세트에는 포켓몬 수, 이름, 첫 번째 타입,두 번째 타입과 기본 통계')
    st.text('HP, 공격, 방어, 특수 공격, 특수 방어 및 속도')
    st.text('를 포함한 1025종류의 포켓몬이 포함되어 있습니다')
    st.text('아이들에게 통계를 가르칠 때 매우 유용하게 사용되었습니다.')
    
    st.subheader('기능요약')
    st.text('분석정보탭 에서 기본적인 EDA를 확인할수 있습니다.')
    st.text('높은 정확도를 기반으로 인공지능이 수치를 계산화 해줍니다')
    st.text('그래프를 통해 시각적인 정보를 확인할수 있습니다.')