import requests
import pandas as pd
import json
import streamlit as st
import numpy as np

st.set_page_config(
    page_title = "Data skills"
)

st.title("Data skills")

st.write("Job title:")

## Global variables
skills_options = ['All', 'Languages', 'Tools', 'Databases', 'Cloud', 'Libraries', 'Frameworks']
col1, col2 = st.columns(2)

with col1:
    st.write('Column 1')
    st.selectbox('Job Title', [1,2,3])

with col2:
    st.write('Column 2')
    st.selectbox('Country', [1,2,3])
    st.write('X jobs analyzed')

selected_skill = st.radio('Skills:', skills_options)

st.write(f'The selected skill is: {selected_skill}')