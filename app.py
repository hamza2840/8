import os
import glob
import time
import multiprocessing

import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go

from Inputs_Parallel import get_possible_scenarios

message = 'streamlit POC'
st.header(message)

# Side Bar #######################################################
project_title = st.sidebar.text_input(label="Title of Project",
                                      value="Example Project")

username = st.sidebar.selectbox(label="Username",
                                options=("a_name",
                                         "b_name"))

buildable_land_folder = st.sidebar.text_input(label="Buildable Land Folder",
                                              value=r"\\filepath\example")

config_file_location = st.sidebar.text_input(label="Config File",
                                             value=r"\\filepath\example")

gcr_config = st.sidebar.slider(label="Ground Coverage Ratio Range Selection",
                               min_value=10,
                               max_value=60,
                               step=1,
                               value=(28, 45))

sr_config = st.sidebar.slider(label="Sizing Ratio Range Selection",
                              min_value=1.0,
                              max_value=2.0,
                              step=0.1,
                              value=(1.0, 1.5))

run_button = st.sidebar.button(label='Run Optimization')

progress_bar = st.sidebar.progress(0)
