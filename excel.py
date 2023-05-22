import streamlit as st

import pip
pip.main(["install", "openpyxl"])

st.title('Aprende a subir tu archivo de excel a la Web')


df = pd.read_excel('USD-COP.xlsx')

st.write(df)
                   
                   