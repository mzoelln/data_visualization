import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np
from bokeh.plotting import figure

filename_ls = []
for i in os.listdir():
  if i.endswith('.csv'):
    filename_ls.append(i)

st.write('Plotting data with bokeh in Streamlit')

select = st.radio('Select a data file', (filename_ls[0], filename_ls[1], filename_ls[-1]))

df = pd.read_csv(select)
el_list = df.columns.tolist()[27:80]
# st.dataframe(df)

options = st.multiselect('select location', filename_ls)

tab1, tab2, tab3 = st.tabs(['Data', 'Plot', 'Stats'])

x_axis = st.selectbox('select x-axis element', el_list)
y_axis = st.selectbox('select y-axis element', el_list)

# plot with matplotlib (not interctive)
# fig = plt.figure()
# plt.scatter(df[x_axis]/10000, df[y_axis]/10000)
# plt.title('with matplotlib without multiselectbox')
# st.pyplot(fig)

# plot with bokeh

for i in options:
  data = pd.read_csv(i)
  
  with tab1:
    st.write(i[:-4])
    st.dataframe(data)
    
  # with tab2:
  #  p = figure(x_axis_label=x_axis+' (wt%)', y_axis_label=y_axis+' (wt%)', title=i[:-4])
  #  p.circle(data[x_axis]/10000, data[y_axis]/10000)
  #  p.line([data[x_axis].min()/10000, data[x_axis].max()/10000], [data[y_axis].mean()/10000,data[y_axis].mean()/10000], line_color='green' )
  #  p.rect(x=data[x_axis].mean()/10000, y=data[y_axis].mean()/10000, width=data[x_axis].std()/10000, height=data[y_axis].std()/10000, color='blue', fill_alpha=0.25)
  #  p.line([data[x_axis].mean()/10000, data[x_axis].mean()/10000], [data[y_axis].min()/10000,data[y_axis].max()/10000], line_color='red' )
  #  st.bokeh_chart(p, use_container_width=True)
    
  with tab3:
    st.write('Mean of '+ str(x_axis) +' in wt%: ' + str(round(data[x_axis].mean()/10000, 2)))
    st.write('Mean of '+ str(y_axis) +' in wt%: ' + str(round(data[y_axis].mean()/10000, 2)))



