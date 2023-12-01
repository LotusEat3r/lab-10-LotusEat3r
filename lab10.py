import os
import pandas as pd
import numpy as np
import streamlit as st
import seaborn as sns

st.title('Penguins Interactive')
penguins = sns.load_dataset('penguins')

species = st.selectbox("Select a Species", penguins['species'].unique())
island = st.selectbox("Select an Island", penguins[penguins['species'] == species]['island'].unique())