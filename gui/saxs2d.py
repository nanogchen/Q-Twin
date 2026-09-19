import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import sys
sys.path.insert(0, "../")
from gui.fileIO import create_zip_download
from srcs.q_gen import get_binning_averages
from srcs.calc import get_scattering_image

def saxs2d(u):

    st.subheader("2D Scattering Intensity S(q1, q2)")
    Fr_start = st.session_state.input['frame_start']
    Fr_end = st.session_state.input['frame_end']
    Fr_step = st.session_state.input['frame_step']
    
    if st.session_state.input['length_unit'] == "LJ" and st.session_state.input["traj_file"].endswith(".xtc"):
        unit_conv = 10.0
    else:
        unit_conv = 1.0

    bx, by, bz = u.dimensions[:3] / unit_conv
    L = max(bx, by, bz) 

    col1, col2, col3 = st.columns(3)
    with col1:
        ag_str = st.text_input("Select system of interest", 
                    value="all", 
                    help="MDAnalysis atom group selection",
                    )
    with col2:
        # select plane            
        plane_selected = st.radio("Choose scattering plane:", 
                            ["xy", "xz", "yz"], 
                            horizontal=True,
                            index=1,  # Default to 'xz'
                            )
        st.session_state.input["saxs_2d_plane"] = plane_selected
    with col3:
        if st.session_state.input['length_unit'] == "real":
            q_temp = 2.0
        else:
            q_temp = 10.0

        q_max = st.number_input(
                "q_max (Å⁻¹ or $\\sigma$)", 
                value=float(q_temp), 
                min_value=float(2*np.pi/L), 
                step=1.0, 
                format="%.2f",
                )

    # do scattering
    # if st.button("Calculate SAXS-2D"): 
    system = u.select_atoms(ag_str)         
    q_points, ssf_1d, qpts1, qpts2, ssf_2d = get_scattering_image(
                                        np.array([bx, by, bz]), 
                                        q_max,
                                        system, 
                                        u.trajectory[Fr_start:Fr_end+1:Fr_step], 
                                        plane=st.session_state.input['saxs_2d_plane'],
                                        unit_conv=unit_conv,
                                        )
    
    num_q_bins = int(q_max/round(1.5*2*np.pi/L, 2))
    qr, ssf_r = get_binning_averages(num_q_bins, q_max, ssf_1d, q_points)
    ssf_qr_mean = np.mean(ssf_r, axis=1)
    ssf_2d_mean = np.mean(ssf_2d, axis=-1)
    ssf_2d_mean[ssf_2d_mean.shape[0]//2, ssf_2d_mean.shape[1]//2] = 0.0

    # Dynamic contrast limits: prevent high peaks from crushing outer rings
    v_min = 0.0
    v_max = float(np.percentile(ssf_2d_mean, 99.5))
    if v_max <= v_min:
        v_max = float(np.max(ssf_2d_mean))
    
    # Coordinate labels
    plane = st.session_state.input["saxs_2d_plane"]
    axis_labels = {
        "xz": ("q<sub>x</sub>", "q<sub>z</sub>"),
        "xy": ("q<sub>x</sub>", "q<sub>y</sub>"),
        "yz": ("q<sub>y</sub>", "q<sub>z</sub>"),
    }
    xlabel, ylabel = axis_labels.get(plane, ("q<sub>1</sub>", "q<sub>2</sub>"))
    unit_str = (
        "Å<sup>-1</sup>"
        if st.session_state.input["length_unit"] == "real"
        else "σ<sup>-1</sup>"
    )

    # Heatmap render
    fig = go.Figure(
        go.Heatmap(
            z=ssf_2d_mean.T,  # Transpose to map axis 0 -> x, axis 1 -> y
            x=qpts1,
            y=qpts2,
            zmin=v_min,
            zmax=v_max,
            connectgaps=True,
            zsmooth="best",
            colorscale="jet",
            colorbar=dict(
                title=dict(text="<i>S</i>(<b>q</b>)", side="right"),
                thickness=20,
                len=0.9,
            ),
        )
    )

    fig.update_layout(
        autosize=False,
        width=520,
        height=500,
        margin=dict(l=60, r=40, t=30, b=60),
        xaxis=dict(
            title=f"{xlabel} ({unit_str})",
            zeroline=False,
            showgrid=False,
        ),
        yaxis=dict(
            title=f"{ylabel} ({unit_str})",
            scaleanchor="x",  # Enforce 1:1 aspect ratio to avoid elliptical distortion
            scaleratio=1,
            zeroline=False,
            showgrid=False,
        ),
    )

    st.plotly_chart(fig, width='content')

    # --- Download Button ---
    data_to_zip = {
        "q_points": q_points,
        "qpts1": qpts1,
        "qpts2": qpts2,
        "saxs_2d_t":ssf_2d,
        "saxs_2d":ssf_2d_mean.transpose()
    }

    zip_data = create_zip_download(data_to_zip)

    st.download_button(
        label="📥 Download All Results (.zip)",
        data=zip_data,
        file_name=f"saxs2d_{st.session_state.input['saxs_2d_plane']}_results.zip",
        mime="application/zip"
    )

    if st.button("Get SAXS-1D results"):

        fig_saxs1d = px.line(x=qr[1:], y=ssf_qr_mean[1:], 
            # log_x=True, log_y=True, 
            markers=True,
            labels={'x':'q', 'y':'S(q)'})
        # Update Layout for better visibility
        fig_saxs1d.update_layout(
                    # title=f"saxs 1d profile",
                    # title_x=0.3,
                    autosize=False,
                    # height=500, # Set a specific height to help control the overall figure size
                )              
        st.plotly_chart(fig_saxs1d, width='content')
