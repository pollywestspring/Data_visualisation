import streamlit as st
import pandas as pd
import os

file_name_list=[]
for i in os.listdir(): #select every csv file in my directory
  if i.endswith('csv'):
                file_name_list.append(i)

st.write('Hello world of visualisation')

df=pd.read_csv('Bastar Craton.csv')
st.dataframe(df)

el_list=df.columns.tolist()[27:80]
x_axis=st.selectbox('select element', el_list)

st.multiselect('select location', file_name_list, file_name_list[0])


from bokeh.plotting import figure

x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

p = figure(
    title='simple line example',
    x_axis_label='x',
    y_axis_label='y')

p.line(x, y, legend_label='Trend', line_width=2)

st.bokeh_chart(p, use_container_width=True)
