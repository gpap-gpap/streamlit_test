import streamlit as st
st.set_page_config(
    page_title="Mantis - phasor",
    layout="wide"
)
from streamlit_option_menu import option_menu
from matplotlib import style 
style.use(['dark_background', './test.mplstyle'])
from GUI.pages import rock_physics_functionality
from GUI.pages import interface_functionality
from GUI.pages import well_loader
from GUI.pages import wave_modelling_functionality
from GUI.pages import inversion_functionality
from streamlit_setup import mantis_dark_theme as cl
from PIL import Image

logo_image = Image.open('./GUI/pages/images/phasor_logo.png') 
logo_text = '<span style = "font-family:Courier; font-weight:800; color:black; font-size: 16px;">phasor</span>'
# ,'./mantis/mantis.mplstyle'


PAGES = {
    'well':well_loader,
    'rock':rock_physics_functionality,
    'interface':interface_functionality,
    'wave':wave_modelling_functionality,
    'inversion':inversion_functionality,
    }


with st.sidebar:
    
    st.markdown(logo_text, unsafe_allow_html=True)
    selected3 = option_menu(None, ['well', 'rock',  'interface', 'wave', 'inversion'], 
    icons=['bookshelf', 'box', 'arrow-down-up', 'activity', 'bullseye'], 
    menu_icon="cast", default_index=0, orientation="vertical",
    styles={
        "container": {"padding": "0!important", "background-color":cl['background_light']},
        "icon": {"color": cl['highlight'], "font-size": "24px"}, 
        "nav-link": {"font-size": "24px", "text-align": "left", "margin":"0px", "--hover-color": cl['background_dark']},
        "nav-link-selected": {"background-color": cl['background_dark'], "text-align": "left", "margin":"0px"},
    }
    )
    st.image(logo_image, width=300, clamp=True)
    page = PAGES[selected3]
page.app()