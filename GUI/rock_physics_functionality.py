import streamlit as st
from pandas import read_csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from mantis import rock_physics as rp
from mantis import reflectivity as mr
from streamlit_setup import mantis_dark_theme as cl



@st.cache
def load_fluids(data_link):
    dataset = read_csv(data_link)
    return dataset

# def set_conditions(temp = temp, pres = pres, fluid = fwd_fluid, saturation = sat, patch = patch):
#     return {'fluid_temperature':temp, 'fluid_pressure':pres, 'fluid':'Water', 'forward_fluid':fwd_fluid, 's1':sat, 'q':patch}
# @st.cache
# def plot_fluids():
    
#     return fig
fluids = load_fluids('./mantis/core_data/fluids.csv')
rock_presets = rp.isotropicRockMatrix(
    name="sandstone",
    grain_modulus=36,
    dry_bulk_modulus=12,
    dry_shear_modulus=6,
    porosity=0.1,
    mineral_density=2.65,
)
freq = np.linspace(-2.,7.,100)

def app():
    st.title('rock physics modeller')
    st.write('Define up to four rocks for the rock physics interface')
    st.subheader('Select injection fluid and reservoir conditions')
    forward_fluids = fluids['Fluid'].unique()
    saturation = np.linspace(0,1,100)
    if "current_rock" not in st.session_state:
        st.session_state.rock = None
    
    if "conditions" not in st.session_state:
    # set the initial default value of the slider widget
        st.session_state.conditions = {'fluid_temperature':28.5, 'fluid_pressure':40, 'fluid':'Water', 'forward_fluid':'CarbonDioxide'}
    if "temp" not in st.session_state:
        st.session_state.temp = 28.5
    if "pres" not in st.session_state:
        st.session_state.pres = 40
    if "current_fluid" not in st.session_state:
        st.session_state.current_fluid = 'CarbonDioxide'
    if "sat" not in st.session_state:
        st.session_state.sat = 1.
    if "patch" not in st.session_state:
        st.session_state.patch = 1.
    if "eps" not in st.session_state:
        st.session_state.eps = 0.05
    if "epsf" not in st.session_state:
        st.session_state.epsf = 0.01
    if "epsfX" not in st.session_state:
        st.session_state.epsfX = 0.01

    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    st.session_state.current_fluid = st.radio('Injection fluid',forward_fluids)
    st.session_state.rock = mr.ForwardRockPhysicsModeller(Vp = 2.1, Vs =1., Rho = 2.01,**st.session_state.conditions, mineral = 'QuartzS')
    
    def fluid_modulus(s):
        return st.session_state.rock.fluid_mix.modulus(s1=s, q=st.session_state.patch)
    fl = [fluid_modulus(s) for s in saturation]
    current_rock = st.session_state.rock.forward_cij(viscoelastic = True, anisotropic = True)(**{'eps':st.session_state.eps, 'epsfX':st.session_state.epsfX, 'epsf':st.session_state.epsf,  'tauf':1/5, 'taufX':1/1000,'tau':1/100000, 's1':st.session_state.sat,'q':st.session_state.patch})

    col1, col2, col3 =  st.columns([30,70, 10])
    with col1:
        pres_range = np.array(fluids['Pres-MPa'].unique())
        st.slider("Pressure (MPa)", min_value=int(pres_range.min()), max_value=int(pres_range.max()), step=5, key='pres')
        temp_range = np.array(fluids['Temp-degC'].unique())
        st.slider("Temperature (deg C)", min_value=float(temp_range.min()), max_value=float(temp_range.max()), step=3.5, key='temp')
        st.slider("Saturation", min_value=0., max_value=1., step=.05, key='sat')
        st.slider("Patchiness (small is patchy)", min_value=0., max_value=1., value = 1.,step=.1, key='patch')
    with col2:
        fig, ax = plt.subplots()
        ax.set_anchor((0.1,0.1), share=True)
        ax.set_xlabel('Water Saturation')
        ax.set_ylabel('Fluid modulus (MPa)')
        ax.plot(saturation, fl)
        ax.scatter(st.session_state.sat,fluid_modulus(st.session_state.sat))
        # ax.scatter(x_axis, y_axis, color=cl['text'])
        st.pyplot(fig=fig)


    with col3:
            if st.button('Store as scenario 1'):
                st.write('Scenario 1 not stored')
            else:
                st.write(f'{current_rock}')
            if st.button('Store as scenario 2'):
                st.write('Why hello there')
            else:
                st.write('Goodbye')
            if st.button("Store as scenario 3"):
                st.write('Why hello there')
            else:
                st.write('Goodbye')
            if st.button('Store as scenario 4'):
                st.write('Why hello there')
            else:
                st.write('Goodbye')
    st.session_state.conditions ={'fluid_temperature':st.session_state.temp, 'fluid_pressure':st.session_state.pres, 'fluid':'Water', 'forward_fluid':st.session_state.current_fluid}
    # st.write(st.session_state.conditions)
    st.subheader('Enter fracture information')
    col1, col2, col3 = st.columns([30,70, 10])
    with col1:
        eps = st.slider("crack density", min_value=0., max_value=0.1, step=0.01, value = 0.05,key='eps')
        epsf = st.slider("horizontal fracture density", min_value=0., max_value=0.1, value = 0.01, step=0.01, key='epsf')
        epsfX = st.slider("vertical fracture density", min_value=0., max_value=0.1, value = 0.01, step=0.01, key='epsfX')
    with col2:
        
        test = np.real(np.stack([current_rock(i) for i in freq]))

        plt.figure(figsize=(3,1))
        fig, ax = plt.subplots()
        ax.set_anchor((0.1,0.1), share=True)
        # Create a Rectangle patch
        rect = patches.Rectangle((-.5,0.), 1.5, 10., linewidth=1, edgecolor='0.', facecolor='.2', alpha=.8)


        # Add the patch to the Axes
        ax.add_patch(rect)
        # ax.set_xlim()
        ax.set_ylim(0.85*test[0,0,0],1.05*test[-1,0,0])
        ax.set_xlabel('log frequency')
        ax.set_ylabel('elastic modulus (MPa)')
        ax.plot(freq, test[:,0,0],linewidth=5, label = "$C_{11}$")
        ax.plot(freq, test[:,1,1],linewidth=4, label = "$C_{22}}$")
        ax.plot(freq, test[:,2,2], label = "$C_{33}$")
        ax.legend(bbox_to_anchor=[0.9, 0.3],labelcolor='linecolor')
        st.pyplot(fig=fig)

    # with col1:
    #     st.subheader('Fluid modelling')
    #     current_fluid = st.selectbox('Injection fluid', fluids['Fluid'].unique())
    #     pres_range = np.array(fluids['Pres-MPa'].unique())
    #     pres = st.slider("Pressure", min_value=5, max_value=100, step=5)
    #     propty = st.radio('Property',['Modulus-GPa', 'Density-Kg/m^3', 'Viscosity-uPa.s'])
    #     data = fluids[(fluids['Pres-MPa']<pres+delta) & (pres-delta<fluids['Pres-MPa']) & (fluids['Fluid']==current_fluid)]
    #     x_axis = data['Temp-degC']
    #     y_axis = data[propty]
    #     fig, ax = plt.subplots()
    #     ax.scatter(x_axis, y_axis, color=cl['text'])
    #     st.pyplot(fig=fig)
    # with col2:
    #     st.subheader('Rock modelling')
    #     fractured = st.checkbox('Fractures', key='frac')
    #     frequency_dependent = st.checkbox('Frequency Dependence', key='freq')
    #     if fractured:
    #         st.slider('horizontal fracture density', min_value=0., max_value=.1, step=.01)
    #         st.slider('vertical fracture density', min_value=0., max_value=.1, step=.01)
        
    #     reservoir = rp.isotropicRockMatrix(
    #         name="sandstone",
    #         grain_modulus=36,
    #         dry_bulk_modulus=12,
    #         dry_shear_modulus=6,
    #         porosity=0.1,
    #         mineral_density=2.65
    #     )
    #     wat_co2 = 
    #     co2reservoir = rp.rock(reservoir, wat_co2, anisotropic=True, viscoelastic=True)
    #     spec  = np.array([co2reservoir.cij(s1=sat, omega=i, q=1., eps=0.005, epsf=0.002, epsfX=0.003, tau=1, tauf=1e3, taufX=1e7) for i in wAxis])
    #     fig, ax = plt.subplots()
    #     ax.set_xlim([0.,2])
    #     ax.set_ylim([0.,1.])
    #     ax.yaxis.set_visible(False)
    #     ax.xaxis.set_visible(False)
    #     ax.set_axis_off()
    #     ax.set_aspect(5.)
    #     ax.invert_yaxis()
    #     ax.plot(wAxis, np.real(spec))
    #     # [ax.add_patch(r) for r in rectangles]
    #     # ax.add_patch(rec(xy=(0.,0.), width=10., height = 20., facecolor='b', fill = True))
    #     # ax.add_patch(rec(xy=(0., 21.), width=10., height = 30., facecolor='r', fill = True))
    #     st.pyplot(fig=fig)