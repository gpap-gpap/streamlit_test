import streamlit as st
st.set_page_config(
    page_title="Mantis - phasor",
    layout="wide"
)
from streamlit_option_menu import option_menu
from matplotlib import style 
style.use(['dark_background', './mantis/mantis.mplstyle'])
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


# with st.sidebar:
#     st.title('depth modeller')
#     # cell_width = 212
#     # cell_height = 22
#     # swatch_width = 48
#     # margin = 12
#     # topmargin = 40
#     # emptycols=0
#     # n = 200
#     # ncols = 4 - emptycols
#     # nrows = n // ncols + int(n % ncols > 0)

#     # width = cell_width * 4 + 2 * margin
#     # height = cell_height * nrows + margin + topmargin + 400
#     # dpi = 72
#     # # rec_test = pt.Rectangle((0.,0.), 5., 1.)
#     # fig, ax = plt.subplots(figsize=(width / dpi, height / dpi), dpi=dpi)
#     # x_min, x_max = 0., 100.
#     # y_min, y_max = 0., 500.
#     # x_range = x_max - x_min
#     # y_range = y_max - y_min
#     fig, ax = plt.subplots()
#     # margin = 10
#     # fig.subplots_adjust(5, 10, 15, 20)
#     # ax.plot([0,500],[0,100])
#     ax.set_xlim([0.,10.])
#     ax.set_ylim([0,50.])
#     ax.yaxis.set_visible(False)
#     ax.xaxis.set_visible(False)
#     ax.set_axis_off()
#     ax.add_patch(rec(xy=(0.,0.), width=10., height = 20., facecolor='b', fill = True))
#     ax.add_patch(rec(xy=(0., 21.), width=10., height = 30., facecolor='r', fill = True))
#     st.pyplot(fig=fig)
#     model = load_well("test_well.las", "test_tops.csv")
#     tmp = model.layers()
#     st.write(tmp["TopDepth"])
#     # with st.echo():
#     #     st.write("this is on the sidebar")
#     selected_iso = st.radio("Select isotropic/anisotropic", ['isotropic', 'anisotropic'])
#     selected_visco = st.radio("Select Class", ['elastic', 'viscoelastic'])
#     st.write("Anisostropic:", selected_iso)
#     st.write("Frequency dependence:", selected_visco)


# col1.title('rock physics module test')

# fluids = load_fluids(getcwd() + "/mantis/core_data/fluids.csv")

# # selected_fluid = st.selectbox("fluids", fluids['Fluid'].unique())
# # st.write("Selected Decks:", selected_fluid)

# # st.write("Selected Class Type:", type(selected_iso))

# reservoir = rp.isotropicRockMatrix(
#     name="sandstone",
#     grain_modulus=36,
#     dry_bulk_modulus=12,
#     dry_shear_modulus=6,
#     porosity=0.1,
#     mineral_density=2.65,
# )

# optionals = st.expander("Optional Configurations", True)
# fare_pres = optionals.slider(
#     "Pressure (MPa)",
#     min_value=float(fluids['Pres-MPa'].min()),
#     max_value=float(fluids['Pres-MPa'].max()),
#     step=5.
# )
# fare_temp = optionals.slider(
#     "Temperature (C)",
#     min_value=float(fluids['Temp-degC'].min()),
#     max_value=float(fluids['Temp-degC'].max()),
#     step=3.5
# )
# subset_fare = titanic_data[(titanic_data['fare'] <= fare_max) & (fare_min <= titanic_data['fare'])]
# st.write(f"Number of Records With Fare Between {fare_min} and {fare_max}: {subset_fare.shape[0]}")


# fluid1 = rp.fluid(name=selected_fluid, modulus=2.1, viscosity=1e-5, density=1.0)
# st.write(fluid1)
# water = rp.fluid(name="water", modulus=2.1, viscosity=1e-5, density=1.0)
# co2 = rp.fluid(name="scCO2", modulus=0.8, viscosity=1e-6, density=0.9)

# wat_co2 = rp.fluidMix(water, co2)
# co2reservoir = rp.rock(reservoir, wat_co2, anisotropic=True, viscoelastic=True)
# co2elastic = rp.rock(reservoir, wat_co2, anisotropic=False, viscoelastic=False)

# sat = st.slider("Saturation", min_value=0., max_value=1., step=.01)
# pat = st.slider("Patchiness", min_value=0.5, max_value=1., step=.01)

# wAxis = np.arange(-9, 3, 0.05)
# spec  = np.array([co2reservoir.cij(s1=sat, omega=i, q=pat, eps=0.005, epsf=0.002, epsfX=0.003, tau=1, tauf=1e3, taufX=1e7) for i in wAxis])
# st.set_option('deprecation.showPyplotGlobalUse', False)
# fig, ax = plt.subplots()
# test_plot = ax.plot(wAxis, spec[:,0,0])
# st.pyplot(fig=fig)
# instance1 = co2reservoir.cij(s1=0.1, q=1, eps=0.0, epsf=0.01, epsfX=0.0)
# instance1el = co2elastic.cij(s1=0.1, q=1, eps=0.02, epsf=0.01)



# 


# plt.plot(wAxis, spectrum[:, 0, 0])
# plt.plot(wAxis, spectrum[:, 1, 1])
# plt.plot(wAxis, spectrum[:, 2, 2])
# st.write(df)