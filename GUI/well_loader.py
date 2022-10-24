import streamlit as st
from mantis import well as wl
from pandas import read_csv
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle as rec
from matplotlib import cm
import numpy as np




@st.cache(allow_output_mutation=True)
def load_well(data_link, data_tops, vel="Backus"):
    dataset = wl.WellToInputModel(data_link, data_tops, velocity_averaging=vel)
    return dataset

@st.cache(allow_output_mutation = True)
def load_preset(input_csv):
    
    read_csv()
    model = wl.InputModel()
    return
mod0 = load_well("test_well.las", "test_tops.csv")
tmp = mod0.layers
lengths = (np.add.accumulate(tmp['Thickness'])).to_numpy()
thicknesses = tmp['TopDepth'].to_numpy()
lengths = np.append([0.],lengths)/lengths[-1]
colors = cm.terrain(np.linspace(0,1,len(thicknesses)))



def app():
    st.title('load a well and tops file or set a blocky model')
    log_file = st.file_uploader('Upload well file (las) and tops file (csv)', type=['las', 'csv'])
    if log_file is not None:
        file_details = {'filename':log_file.name, 'file size':log_file.size}
        st.write(file_details)
    # col1, col2 =  st.columns([50,50])
    # with col1:
    # menu = ['well log','tops file']
    # choice = st.selectbox('Upload Menu', menu)
    # if choice == 'well log':
    #     st.subheader('well log')
    #     log_file = st.file_uploader('upload well', type=['las'])
    #     if log_file is not None:
    #         file_details = {'filename':log_file.name, 'file size':log_file.size}
    #         st.write(file_details)
    # elif choice == 'tops file':
    #     st.subheader('tops')
    #     tops_file = st.file_uploader('upload tops', type=['csv'])
    col1, col2 = st.columns([10,20])
    with col1:
        choice = st.radio("Select Averaging Between Tops",('Slowness','Arithmetic','Dix','Backus'))
        model = load_well("test_well.las", "test_tops.csv", vel=choice)
    with col2:
        rectangles = [rec(xy=(0.,0.+i[0]), width=10, height=i[1], facecolor=i[2], edgecolor='w', fill=True) for i in zip(lengths, thicknesses, colors)]
        x_ax = model.layers["TopDepth"].values
        y_ax = model.layers["Vp"].values
        y2_ax = model.layers["Vs"].values
        y3_ax = model.layers['Rho'].values
        fig, (ax1, ax2, ax3) = plt.subplots(1,3)
        # ax.set_xlim([0.,2])
        # ax.set_ylim([0.,1.])
        # [ax2.add_patch(r) for r in rectangles]
        ax1.yaxis.set_visible(False)
        ax1.xaxis.set_visible(False)
        ax1.set_axis_off()
        ax2.yaxis.set_visible(False)
        ax2.xaxis.set_visible(False)
        ax2.set_axis_off()
        ax3.yaxis.set_visible(False)
        ax3.xaxis.set_visible(False)
        ax3.set_axis_off()
        ax1.set_aspect(.01, 'box')
        ax2.set_aspect(.01, 'box')
        ax3.set_aspect(.01, 'box')
        ax1.invert_yaxis()
        ax2.invert_yaxis()
        ax3.invert_yaxis()
        ax1.step(model.lasData["VS"],model.lasData["TD"])
        ax1.step(y2_ax, x_ax)
        ax2.plot(model.lasData["VP"],model.lasData["TD"])
        ax2.step(y_ax, x_ax)
        ax3.plot(model.lasData["RHOB"],model.lasData["TD"])
        ax3.step(y3_ax, x_ax)
        # plt.show()
        # [ax1.add_patch(r) for r in rectangles]
        # # ax.add_patch(rec(xy=(0.,0.), width=10., height = 20., facecolor='b', fill = True))
        # # ax.add_patch(rec(xy=(0., 21.), width=10., height = 30., facecolor='r', fill = True))
        # st.pyplot(fig=fig)
        # fig = plt.plot(x_ax, y_ax)
        plt.tight_layout()
        st.pyplot(fig=fig)
        # st.write(x_ax,y_ax)

    # # This will get the value of the slider widget
    # st.write(st.session_state.celsius)
    # col1, col2 = st.columns([5,20])
    # with col1:
    #     rectangles = [rec(xy=(0.,0.+i[0]), width=10, height=i[1], facecolor=i[2], edgecolor='w', fill=True) for i in zip(lengths, thicknesses, colors)]
    #     fig, ax = plt.subplots()
    #     ax.set_xlim([0.,2])
    #     ax.set_ylim([0.,1.])
    #     ax.yaxis.set_visible(False)
    #     ax.xaxis.set_visible(False)
    #     ax.set_axis_off()
    #     ax.set_aspect(5.)
    #     ax.invert_yaxis()
    #     [ax.add_patch(r) for r in rectangles]
    #     # ax.add_patch(rec(xy=(0.,0.), width=10., height = 20., facecolor='b', fill = True))
    #     # ax.add_patch(rec(xy=(0., 21.), width=10., height = 30., facecolor='r', fill = True))
    #     st.pyplot(fig=fig)
    # with col2:
    #     st.write(thicknesses)