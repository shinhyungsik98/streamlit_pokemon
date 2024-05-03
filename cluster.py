import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np



def run_cluster () :
    st.image('./image/poke2.png')
    st.subheader('비슷한 파워수준의 포켓몬 찾기')

    df=pd.read_csv('./data/Pokemon.csv')

    column_names = df.columns.tolist()


    selected_columns = ['체력', '공격', '방어', '특수공격', '특수방어', '속도']


    selected_columns_only = [col for col in column_names if col in selected_columns]
    

    st.subheader('어떤 수치가 비슷한걸 원하시나요?')
    selected_columns = st.multiselect('X로 사용할 컬럼을 선택하세요', selected_columns_only)
    
    X= df[selected_columns]

    if len(selected_columns ) >=2 :
            
        X_new = pd.DataFrame()

        print(X_new)

        for column in X.columns :
                print(X[column])

                #컬럼의 데이터가 문자열이면 , 레이블 인코딩 원핫인코딩 해야한다.
                if X[column].dtype == object :
                    if X[column].nunique() >= 3 :
                        
                        column_names = sorted(X[column].unique())
                        #비어있는 데이터 프레임에 컬럼 추가 
                        #원핫인코딩
                        X_new[column_names]=pd.get_dummies(X[column].to_frame())
                    else :
                        #레이블 인코딩
                        encoder = LabelEncoder()
                        X_new[column]=encoder.fit_transform(X[column])
                else :
                    #숫자 데이터처리
                    X_new[column] = X[column]
            
            #X_new는 숫자로만 되어있는 데이터프레임.
            #4-1 유저한테 보여주자

        X_new.reset_index(inplace=True, drop=True)
 
            
        st.subheader('클러스터링에 실제 사용할 데이터')
        st.dataframe(X_new)



            #5. k의 갯수를 1개부터 10개까지 해서 wcss를 구한다.

        wcss=[]
        for k in np.arange(1,1+10) :
            kmeans = KMeans(n_clusters=k,random_state=5)
            kmeans.fit(X_new)
            wcss.append(kmeans.inertia_)

        fig1 = plt.figure()
        x = np.arange(1,10+1)
        plt.plot(x,wcss)
        plt.plot('엘보우 메소드')
        plt.xlabel('클러스터의 갯수')
        plt.ylabel('WCSS')
        st.pyplot(fig1)


        k = st.slider('클러스터 갯수설정',1,10)

            

    
        kmeans = KMeans(n_clusters= k, random_state= 5)
        y_pred = kmeans.fit_predict(X_new)
        # 9. 원래 있던 df 에 Group 이라는 컬럼을 만들어준다. 
        df['Group'] = y_pred


        st.subheader('클러스터링 결과')

        st.dataframe(df)


        #12유저가 그룹을 선택하면 해당 그룹의 정보를 보여준다.
        choice = st.selectbox('그룹을 선택하세요', np.arange(0,k))
        st.dataframe(df.loc[df['Group']==choice ,])


    


