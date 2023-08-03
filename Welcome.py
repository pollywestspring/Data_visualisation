import streamlit as st
import pandas as pd
import os

file_name_list=[]
for i in os.listdir(): #select every csv file in my directory
  if i.endswith('csv'):
                file_name_list.append(i)

st.write('Hello world of visualisation')

st.selectbox('select location', file_name_list, file_name_list[0])
df=pd.read_csv(file_name_list)
st.dataframe(df)

el_list=df.columns.tolist()[27:80]

x = st.selectbox('select element', el_list)
y = st.selectbox('select element2', el_list)

from bokeh.plotting import figure

p = figure(
    title='example from file',
    x_axis_label='x',
    y_axis_label='y')

p.circle(df[x], df[y])

st.bokeh_chart(p, use_container_width=True)
