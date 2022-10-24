import streamlit as st
from pandas import read_csv
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle as rec
from matplotlib import cm
import numpy as np





def app():
    st.title('wavefield modeller')
    st.write('Nothing to see yet')
    col1, col2 = st.columns([20,50])