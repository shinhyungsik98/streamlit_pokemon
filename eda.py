import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

df=pd.read_csv('./data/Pokemon.csv')

def search_pokemon(input_text, df):
    filtered_data = df[df['이름'].str.contains(input_text, case=False)]
    return filtered_data



def run_eda() :
    df=pd.read_csv('./data/Pokemon.csv')
    st.subheader('탐색적 데이터 분석')
    st.image('./image/dogam.png')
    st.subheader('이름 검색')
    search_name = st.text_input('포켓몬 이름을 입력하세요')
    if search_name:
        filtered_data = search_pokemon(search_name, df)
        if not filtered_data.empty:
            st.write("검색 결과:")
            st.write(filtered_data)
        else:
            st.write("일치하는 포켓몬이 없습니다.")



    st.subheader('전체 포켓몬 정보/ 통계치 보기')

    radio_menu = ['전체 포켓몬 정보 확인','통계수치']

    

    choice_radio=st.radio('선택하세요',radio_menu)

    if choice_radio == radio_menu [0] :
        st.dataframe(df)
        st.text('모든 포켓몬 정보')
    elif choice_radio == radio_menu [1] :
        st.dataframe(df.describe())

    
    st.subheader('컬럼을 선택하면 , 각 컬럼별 최대/최소 데이터를 보여드립니다')
    column_list = ['총합','체력','공격','방어','특수공격','특수방어','속도']
    choice_column = st.selectbox('컬럼을 선택하세요',column_list)

    st.info(f'선택한 스탯 {choice_column}이 가장 높은 포켓몬은 다음과 같습니다')
    st.dataframe(df.loc[df[choice_column] == df[choice_column].max(),])

    st.info(f'선택한 스탯 {choice_column}이 가장 낮은 포켓몬은 다음과 같습니다')
    st.dataframe(df.loc[df[choice_column] == df[choice_column].min(),])



    # Pokemon 데이터 설정
    labels = ['Water', 'Normal', 'Grass', 'Bug', 'Psychic', 'Fire', 'Electric', 'Rock', 'Other']
    sizes = [112, 98, 70, 69, 57, 52, 44, 44, 175]
    colors = ['SkyBlue', '#E8BEAC', '#7CFC00', 'Lightgreen', 'Purple', 'Red', 'Yellow', 'Brown', 'Pink']
    explode = (0, 0, 0, 0, 0, 0, 0, 0, 0)  # 3번째 파이만 띄움

    # Streamlit 앱 제목 설정
    st.subheader("각 포켓몬 타입의 비율")

    # 파이차트 플롯 생성
    fig, ax = plt.subplots()
    ax.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Streamlit에 플롯 출력
    st.pyplot(fig)




