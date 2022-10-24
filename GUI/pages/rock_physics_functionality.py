import streamlit as st
from pandas import read_csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from streamlit_setup import mantis_dark_theme as cl
def app():
    st.title('wavefield modeller')
    st.write('Nothing to see yet')
    col1, col2 = st.columns([20,50])