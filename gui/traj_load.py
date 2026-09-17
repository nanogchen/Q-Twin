import streamlit as st
import MDAnalysis as mda
import os
import numpy as np
# import tkinter as tk
# from tkinter import filedialog
import tempfile

# # Function to trigger the Tkinter folder picker
# def browse_folder():
#     root = tk.Tk()
#     root.withdraw()  # Hide the main tkinter window
#     root.attributes('-topmost', True)  # Bring the dialog to the front
#     directory = filedialog.askdirectory(master=root)
#     root.destroy()
#     if directory:
#         st.session_state.current_path = directory

# @st.cache_resource
# def load_trajectory(path, topo, traj):
#     if topo and traj:
#         try:
#             u = mda.Universe(os.path.join(path, topo), os.path.join(path, traj))
#             return u
#         except Exception as e:
#             st.error(f"Failed to load: {e}")
#     return None

def list_files(path):
    try:
        # Filter for MD specific formats
        exts = ('.xtc', '.lammpstraj', '.pdb', '.gro', '.data', '.dcd', '.trr')
        files = [f for f in os.listdir(path) if f.lower().endswith(exts)]
        return sorted(files)
    except Exception as e:
        st.sidebar.error(f"Error accessing path: {e}")
        return []

EXAMPLE_DIR = "data"
def get_example_list():
    """Returns a list of folder names inside the examples directory."""
    if os.path.exists(EXAMPLE_DIR):
        return [f for f in os.listdir(EXAMPLE_DIR) if os.path.isdir(os.path.join(EXAMPLE_DIR, f))]
    return []

@st.cache_resource
def load_universe_web_deprecated(topo, traj, atom_style_str, format_str, topology_format_str):
    if topo and traj:
        # MDAnalysis needs file paths, so we save uploaded bytes to temp files
        with tempfile.NamedTemporaryFile(suffix=topo.name, delete=False) as tmp_topo:
            tmp_topo.write(topo.getvalue())
            topo_path = tmp_topo.name
            
        with tempfile.NamedTemporaryFile(suffix=traj.name, delete=False) as tmp_traj:
            tmp_traj.write(traj.getvalue())
            traj_path = tmp_traj.name
        
        if atom_style_str is not None and format_str is not None and topology_format_str is not None:
            return mda.Universe(topo_path, traj_path, atom_style = atom_style_str, format=format_str, topology_format=topology_format_str)
        else:
            return mda.Universe(topo_path, traj_path)
    return None

def load_traj():

    st.subheader("Upload Trajectory Files")
    st.write("Please upload your topology and trajectory files to begin analysis.")
    
    # ------------------------------------tkinter based for file processing
    # # Button to load local directory
    # if st.button("📂 Browse Directory"):
    #     browse_folder()

    # # Manual path override
    # st.session_state.current_path = st.text_input(
    #     "Active path:", 
    #     st.session_state.current_path
    # )

    # # load files
    # files = list_files(st.session_state.current_path) 

    # col1, col2 = st.columns(2)
    # if files:
    #     with col1:
    #         # topo_file = st.file_uploader("1. Topology (PDB, GRO)", type=['pdb', 'gro'])
    #         selected_topo = st.selectbox("1. Select coordinate (PDB/GRO/DATA)", files)
        
    #     with col2:
    #         # traj_file = st.file_uploader("2. Trajectory (XTC, DCD)", type=['xtc', 'dcd'])
    #         selected_traj = st.selectbox("2. Select trajectory (XTC/DCD/LAMMPSTRAJ)", files)

    # else:
    #     st.warning("No MD files found in this directory. Please select your directory first!")

    # ------------------------------------cloud
    
    # Toggle for Example Mode
    # use_example = st.toggle("💡 Use Example Trajectory", value=False)
    mode = st.radio("Select Data Source:", ["Manual Upload", "Pre-installed Examples"], horizontal=True)
    lmp_traj_exts = ('.dump', '.lammpstraj', '.lammps', '.lammpsdump')

    if mode == "Pre-installed Examples":
        examples = get_example_list()

        if examples:

            selected_example = st.selectbox("Choose a system to analyze:", examples)
            ex_path = os.path.join(EXAMPLE_DIR, selected_example)

            col1,col2 = st.columns(2)
            with col1:
                topo_file = st.selectbox("Choose coordinate (PDB/GRO/DATA) to analyze:", list_files(ex_path))
            with col2:
                traj_file = st.selectbox("Choose trajectory (XTC/DCD/GRO/DATA/LAMMPSTRAJ) to analyze:", list_files(ex_path))

            if topo_file and traj_file:
                topo_ext = os.path.splitext(topo_file)[1].lower()
                traj_ext = os.path.splitext(traj_file)[1].lower()

                topo_path = os.path.join(ex_path, topo_file)
                traj_path = os.path.join(ex_path, traj_file)

                # Determine atom_style if any LAMMPS file is present
                is_lammps = (
                    topo_ext in [".data"] + list(lmp_traj_exts)
                    or traj_ext in [".data"] + list(lmp_traj_exts)
                )
                atom_style_str = None
                if is_lammps:
                    atom_style_str = st.text_input(
                        "Atom style for LAMMPS dump/data file",
                        value="id type x y z",
                        help="Specify LAMMPS column mapping (e.g. 'id type x y z' or 'full')",
                    )

                st.session_state.input["topo_file"] = topo_file
                st.session_state.input["traj_file"] = traj_file

                if st.button("🚀 Load Example"):
                    try:
                        # Case 1: Both files are .data -> Single-frame data Universe
                        if topo_ext == ".data" and traj_ext == ".data":
                            st.warning(
                                "Both files are DATA files. Loading single topology file only."
                            )
                            u = mda.Universe(
                                topo_path,
                                topology_format="DATA",
                                format="DATA",
                                atom_style=atom_style_str,
                            )

                        # Case 2: Standard LAMMPS workflow -> .data topology + dump trajectory
                        elif topo_ext == ".data" and traj_ext in lmp_traj_exts:
                            u = mda.Universe(
                                topo_path,
                                traj_path,
                                topology_format="DATA",
                                format="LAMMPSDUMP",
                                atom_style=atom_style_str,
                            )

                        # Case 3: Both files are dump -> Single dump trajectory Universe
                        elif topo_ext in lmp_traj_exts and traj_ext in lmp_traj_exts:
                            st.warning(
                                "Both files are dump trajectories. Loading trajectory dump only."
                            )
                            u = mda.Universe(
                                traj_path,
                                format="LAMMPSDUMP",
                                atom_style=atom_style_str,
                            )

                        # Case 4: Reverse order input (.dump in box 1, .data in box 2)
                        elif topo_ext in lmp_traj_exts and traj_ext == ".data":
                            st.info(
                                "Detected DATA file in trajectory slot. Inverting roles."
                            )
                            u = mda.Universe(
                                traj_path,
                                topo_path,
                                topology_format="DATA",
                                format="LAMMPSDUMP",
                                atom_style=atom_style_str,
                            )

                        # Case 5: Standard Bio / General formats (PDB, GRO, XTC, DCD, etc.)
                        else:
                            u = mda.Universe(topo_path, traj_path)

                        st.session_state.u = u
                        st.success(
                            f"Successfully loaded {len(u.atoms)} atoms and {len(u.trajectory)} frame(s)!"
                        )

                    except Exception as e:
                        st.error(f"MDAnalysis failed to load files: {str(e)}")
        else:
            st.error("Example files not found in the 'data' directory.")
            
    else:
        # Manual Upload Mode
        col1, col2 = st.columns(2)
        with col1:
            topo_file = st.file_uploader("Upload coordinate (PDB/GRO/DATA)", type=['pdb', 'gro', 'data'])
        with col2:
            traj_file = st.file_uploader("Upload trajectory (XTC/DCD/GRO/DATA/LAMMPSTRAJ)", type=['xtc', 'dcd', 'gro', 'data', 'lammpstraj', '.dump', '.lammps'])
        
        def load_universe_web(topo_upload, traj_upload, mode, atom_style=None):
            """Saves Streamlit uploaded buffer(s) to temporary files with matching extensions,

            constructs the MDAnalysis.Universe, and ensures temporary files are cleaned up.
            """
            temp_files = []

            def save_temp(uploaded_obj):
                ext = os.path.splitext(uploaded_obj.name)[1].lower()
                tfile = tempfile.NamedTemporaryFile(delete=False, suffix=ext)
                tfile.write(uploaded_obj.getbuffer())
                tfile.flush()
                tfile.close()
                temp_files.append(tfile.name)
                return tfile.name

            try:
                if mode == "single_topo":
                    # Only topo file is loaded (e.g. standalone DATA file)
                    path = save_temp(topo_upload)
                    u = mda.Universe(
                        path,
                        topology_format="DATA",
                        format="DATA",
                        atom_style=atom_style,
                    )

                elif mode == "single_traj":
                    # Only traj file is loaded (e.g. standalone DUMP file)
                    path = save_temp(traj_upload)
                    u = mda.Universe(path, format="LAMMPSDUMP", atom_style=atom_style)

                elif mode == "lammps_pair":
                    # DATA topology + DUMP trajectory
                    t_path = save_temp(topo_upload)
                    tr_path = save_temp(traj_upload)
                    u = mda.Universe(
                        t_path,
                        tr_path,
                        topology_format="DATA",
                        format="LAMMPSDUMP",
                        atom_style=atom_style,
                    )

                elif mode == "lammps_pair_inverted":
                    # User uploaded DUMP into slot 1 and DATA into slot 2
                    tr_path = save_temp(topo_upload)
                    t_path = save_temp(traj_upload)
                    u = mda.Universe(
                        t_path,
                        tr_path,
                        topology_format="DATA",
                        format="LAMMPSDUMP",
                        atom_style=atom_style,
                    )

                else:
                    # Standard formats: PDB + XTC, GRO + DCD, etc.
                    t_path = save_temp(topo_upload)
                    tr_path = save_temp(traj_upload)
                    u = mda.Universe(t_path, tr_path)

                return u

            finally:
                # Remove temporary disk artifacts after Universe construction
                for temp_path in temp_files:
                    if os.path.exists(temp_path):
                        os.remove(temp_path)

        if topo_file and traj_file:
            topo_name = topo_file.name.lower()
            traj_name = traj_file.name.lower()

            topo_ext = os.path.splitext(topo_name)[1]
            traj_ext = os.path.splitext(traj_name)[1]

            # Check if LAMMPS inputs are present to determine whether atom_style input is needed
            is_lammps = (
                topo_ext in [".data"] + list(lmp_traj_exts)
                or traj_ext in [".data"] + list(lmp_traj_exts)
            )

            atom_style_str = None
            if is_lammps:
                atom_style_str = st.text_input(
                    "Atom style for LAMMPS dump/data file",
                    value="id type x y z",
                    help="Specify LAMMPS column mapping (e.g., 'id type x y z' or 'full')",
                )

            # Determine resolution mode
            if topo_ext == ".data" and traj_ext == ".data":
                st.warning(
                    "Both files are DATA files. The trajectory slot will be ignored; loading DATA file only."
                )
                mode = "single_topo"

            elif topo_ext in lmp_traj_exts and traj_ext in lmp_traj_exts:
                st.warning(
                    "Both files are dump trajectories. The coordinate slot will be ignored; loading trajectory dump only."
                )
                mode = "single_traj"

            elif topo_ext == ".data" and traj_ext in lmp_traj_exts:
                mode = "lammps_pair"

            elif topo_ext in lmp_traj_exts and traj_ext == ".data":
                st.info("Detected DATA file in trajectory slot. Inverting roles.")
                mode = "lammps_pair_inverted"

            else:
                mode = "standard"

            st.session_state.input["topo_file"] = topo_name
            st.session_state.input["traj_file"] = traj_name
            st.session_state.input["atom_style"] = atom_style_str

            if st.button("🚀 Load System"):
                try:
                    u = load_universe_web(
                        topo_file, traj_file, mode, atom_style=atom_style_str
                    )
                    st.session_state.u = u
                    st.success(
                        f"System loaded successfully! ({len(u.atoms)} atoms, {len(u.trajectory)} frame(s))"
                    )
                except Exception as e:
                    st.error(f"MDAnalysis failed to load system: {str(e)}")

    # Display system info if loaded
    if st.session_state.u:
        u = st.session_state.u
        st.divider()
        st.subheader("System Summary")

        # box info
        bx, by, bz = u.dimensions[:3]
        st.write(f"Box sizes: Lx={bx:.2f}, Ly={by:.2f}, Lz={bz:.2f}")
        st.write(f"Minimum q: 2π/Lmax={2*np.pi/max([bx, by, bz]):.2f}")

        stats_col1, stats_col2, stats_col3 = st.columns(3)
        stats_col1.metric("Atoms", f"{len(u.atoms):,}")        
        stats_col2.metric("Residues", f"{len(u.residues):,}")        
        stats_col3.metric("Frames", f"{len(u.trajectory)}")

        # # If u.atoms has element attributes
        # if hasattr(u.atoms, 'elements'):
        #     # Use .types or .elements to get the string representations
        #     unique_elements = np.unique(u.atoms.elements)
        #     st.write(f"Elements: {', '.join(unique_elements)}")

        if hasattr(u.atoms, 'names'):
            unique_names = np.unique(u.atoms.names)

            st.write("Atom Names")
            st.info(", ".join(unique_names))

        if hasattr(u.atoms, 'types'):
            try: # if types are numbers
                unique_names = np.unique(u.atoms.types).astype(float).astype(int).astype(str)

                st.write("Atom Types")
                st.info(", ".join(unique_names))

            except (ValueError, TypeError): # types are strings
                unique_names = np.unique(u.atoms.types)

                st.write("Atom Types")
                st.info(", ".join(unique_names))

        if hasattr(u.atoms, 'resnames'):
            unique_resnames = np.unique(u.atoms.resnames) 

            st.write("Residue Names")
            st.info(", ".join(unique_resnames))

        # atom selection
        st.write("MDAnalysis atom selection examples:")
        st.code('''
# Select atoms by index (inclusive, 0-based)
u.select_atoms(\"index 0:5\")\n
# Select atoms by id (inclusive, 1-based)
u.select_atoms(\"id 1:5\")\n
# Select atoms by property range
u.select_atoms(\"prop index < 5\")\n
# Select atoms by type
u.select_atoms(\"type 1\")\n
# Select atoms by residue name
u.select_atoms(\"resname DDP\")''')


                    