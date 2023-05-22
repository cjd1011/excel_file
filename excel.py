import streamlit as st
import pandas as pd

st.title('Aprende a subir tu base de datos de Excel a la Web')

df = pd.read_excel('USD-COP.xlsx')

st.write(df)
                   
                   