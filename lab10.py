import os
import pandas as pd
import numpy as np
import streamlit as st
import seaborn as sns

st.title('Penguin Bill Length and Depth by Species and Island')
penguins = sns.load_dataset('penguins')

species = st.selectbox("Select a Species", penguins['species'].unique())
island = st.selectbox("Select an Island", penguins[penguins['species'] == species]['island'].unique())
graph_penguins = penguins[(penguins['species'] == species) & (penguins['island'] == island)]
x_axis = st.selectbox("Select two traits to compare", ['Bill Length', 'Bill Depth', 'Flipper Length', 'Body Mass'])
y_axis = st.selectbox("Select", ['Bill Length', 'Bill Depth', 'Flipper Length', 'Body Mass'], label_visibility='hidden')

plot = sns.scatterplot(graph_penguins, x = 'bill_depth_mm', y = 'bill_length_mm')

st.pyplot(plot.figure)