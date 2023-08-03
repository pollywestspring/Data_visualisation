import streamlit as st
import pandas as pd
import os

file_name_list=[]
for i in os.listdir(): #select every csv file in my directory
  if i.endswith('csv'):
                file_name_list.append(i)

st.write('Hello world')

df=pd.read_csv('Bastar Craton.csv')
st.dataframe(df)

el_list=df.columns.tolist()[27:80]
x_axis=st.selectbox('select element", el_list)

st.selectbox('select location', file_name_list)
