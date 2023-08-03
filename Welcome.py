import streamlit as st
import pandas as pd

st.write('Hello world')

df=pd.read_csv('Bastar Craton.csv')
st.dataframe(df)

el_listdf.columns.tolist()[27:80]
st.selectbox('select element", el_list)
