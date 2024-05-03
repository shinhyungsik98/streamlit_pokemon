import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt



def run_eda() :
    df=pd.read_csv('./data/Pokemon.csv')
    st.subheader('탐색적 데이터 분석')
    st.image('./image/dogam.png')
    st.subheader('이름 검색')
    search_name = st.text_input('포켓몬 이름을 입력하세요')
    if search_name:
        result = df[df['이름'] == search_name]
        if not result.empty:
            st.write('포켓몬 정보')
            st.write(result)
        else:
            st.write('해당 이름을 찾을 수 없습니다.')


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




    '''st.subheader('상관관계 분석')
    st.text('컬럼들을 2개 이상 선택하면, 컬럼들의 상관계수를 보여드립니다.')

    corr_column_list = ['속성','속성2','총합','체력','공격','방어','특수공격','특수방어','속도','세대']
    selected_columns = st.multiselect('컬럼을 선택하세요',corr_column_list)


    if len(selected_columns) >=2 :
        fig1 =sb.pairplot(data=df,vars=selected_columns)
        st.pyplot(fig1)

        #2 상관관계 보여준다
        st.dataframe((df[selected_columns]).corr())

    else :
        st. text('컬럼은 2개 이상 선택해야 합니다.')'''
