import os
os.system('conda activate stat386')
import pandas as pd
import seaborn as sns
import streamlit as st

st.title('Stock Data for March 1 - March 5')
url = 'https://github.com/esnt/Data/blob/main/ClassExamples/stocks.csv'
df = pd.read_csv(url)

st.selectbox("Company", df['symbol'])