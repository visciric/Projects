import streamlit as st
import numpy as np
import pandas as pd 
import fastf1 as ff1

left_column, right_column = st.columns(2)

year = st.selectbox('Select Race Season', (2018, 2019, 2020, 2021, 2022, 2023,2024))

session = ff1.get_session(2024, 'Jeddah', 'R')
gp_event = st.text_input('Enter the Grand Prix location', value='Monza')
session_type = st.selectbox('Select the session type', ('FP1', 'FP2', 'FP3', 'Q', 'SQ', 'R'))
driver_code = st.text_input('Enter the driver code', value='VER')

@st.cache_data 
def load_session(year, event, session):
    return ff1.get_session(year, event, session)

session = load_session(year, gp_event, session_type)
session.load()


laps = session.laps
results = session.results
# Prepare the data
laps = session.laps
results = session.results
results = results[['DriverNumber', 'BroadcastName', 'Time', 'Status']]

# Display the data in the right column
with right_column:
    st.write("Race Results")
    st.dataframe(results)