import streamlit as st
import pandas as pd

import pip
pip.main(["install", "openpyxl"])

st.title('Aprende a subir tu base de datos de Excel a la Web')

df = pd.read_excel('USD-COP.xlsx')

st.write(df)
                   
                   