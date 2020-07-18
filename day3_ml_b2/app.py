import json
import pandas as pd 
import numpy as np 
import streamlit as st 
import plotly.express as px
import wget
from IPython.display import Image

#url = "https://phil.cdc.gov//PHIL_Images/23311/23311.tif"

#corona_image=wget.download(url,'corona.png')
st.markdown("<h1 style='text-align: center; color: red;'>COVID-19  IMPACT in INDIA</h1>", unsafe_allow_html=True)

st.markdown('<style>description{color:blue;}</style>',unsafe_allow_html=True)
 
st.markdown('<description> By Philanthropy batch LEAP2.0 </description>',unsafe_allow_html=True)
st.image("corona.png",width=300)
@st.cache(ttl=60* 5,max_entries=20)
def load_data():
    data=pd.read_csv("https://api.covid19india.org/csv/latest/state_wise.csv")
    return data
data= load_data()

total_cases=data['Confirmed'][0]
recovered_cases=data['Recovered'][0]
deaths_cases=data['Deaths'][0]

#st.sidebar.text_area('enter the text')
st.sidebar.title('Select parameter  to analyse covid-19 ')

st.sidebar.markdown(f'''<div class="card text-white bg-info mb-3" style="width: 18rem">
  <div class="card-body">
    <h5 class="card-title">Total Cases</h5>
    <p class="card-text">{total_cases:,d}</p>
  </div>
</div>''', unsafe_allow_html=True)

st.sidebar.markdown(f'''<div class="card text-white bg-danger mb-3" style="width: 18rem">
  <div class="card-body">
    <h5 class="card-title">Total Deaths</h5>
    <p class="card-text">{recovered_cases:,d}</p>
  </div>
</div>''', unsafe_allow_html=True)


st.sidebar.markdown(f'''<div class="card text-white bg-warning mb-3" style="width: 18rem">
  <div class="card-body">
    <h5 class="card-title">Total Deaths</h5>
    <p class="card-text">{deaths_cases:,d}</p>
  </div>
</div>''', unsafe_allow_html=True)




st.sidebar.text('Success!!')
st.sidebar.markdown('Yay!! Philanthropy batch LEAP2.0')
btn=st.sidebar.button('Success!!')
if btn:
    st.balloons()

