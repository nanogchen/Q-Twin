import os
import tempfile
import MDAnalysis as mda
import streamlit as st
import numpy as np

EXAMPLE_DIR = "data"
LMP_TRAJ_EXTS = (".dump", ".lammpsdump", ".lammpstraj", ".lammps")

def list_files(path):
    try:
        # Filter for MD-specific formats
        exts = (
            ".xtc",
            ".lammpstraj",
            ".pdb",
            ".gro",
            ".data",
            ".dcd",
            ".trr",
            ".dump",
            ".lammps",
        )
        files = [f for f in os.listdir(path) if f.lower().endswith(exts)]
        return sorted(files)
    except Exception as e:
        st.sidebar.error(f"Error accessing path: {e}")
        return []

def get_example_list():
    """Returns a list of folder names inside the examples directory."""
    if os.path.exists(EXAMPLE_DIR):
        return [
            f
            for f in os.listdir(EXAMPLE_DIR)
            if os.path.isdir(os.path.join(EXAMPLE_DIR, f))
        ]
    return []

def cleanup_session_files():
    """Removes temporary files created by previous manual uploads to avoid disk leaks."""
    if "temp_files" in st.session_state:
        for fpath in st.session_state.temp_files:
            if os.path.exists(fpath):
                try:
                    os.remove(fpath)
                except OSError:
                    pass
    st.session_state.temp_files = []

def load_universe_web(topo_upload, traj_upload, mode, atom_style=None):
    """Saves Streamlit uploaded buffer(s) to temporary files that persist

    during analysis so MDAnalysis can stream frames without raising FileNotFoundError.
    """
    cleanup_session_files()

    def save_temp(uploaded_obj):
        ext = os.path.splitext(uploaded_obj.name)[1].lower()
        tfile = tempfile.NamedTemporaryFile(delete=False, suffix=ext)
        tfile.write(uploaded_obj.getbuffer())
        tfile.flush()
        tfile.close()
        st.session_state.temp_files.append(tfile.name)
        return tfile.name

    if mode == "single_topo":
        path = save_temp(topo_upload)
        u = mda.Universe(
            path, topology_format="DATA", format="DATA", atom_style=atom_style
        )

    elif mode == "single_traj":
        path = save_temp(traj_upload)
        u = mda.Universe(path, format="LAMMPSDUMP", atom_style=atom_style)

    elif mode == "lammps_pair":
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
        t_path = save_temp(topo_upload)
        tr_path = save_temp(traj_upload)
        u = mda.Universe(t_path, tr_path)

    return u

def load_traj():
    st.subheader("Upload Trajectory Files")
    st.write(
        "Please upload your topology and trajectory files to begin analysis."
    )

    if "temp_files" not in st.session_state:
        st.session_state.temp_files = []

    mode = st.radio(
        "Select Data Source:",
        ["Manual Upload", "Pre-installed Examples"],
        horizontal=True,
    )

    # ----------------------------------------------------
    # Pre-installed Examples Mode
    # ----------------------------------------------------
    if mode == "Pre-installed Examples":
        examples = get_example_list()

        if examples:
            selected_example = st.selectbox(
                "Choose a system to analyze:", examples
            )
            ex_path = os.path.join(EXAMPLE_DIR, selected_example)

            col1, col2 = st.columns(2)
            with col1:
                topo_file = st.selectbox(
                    "Choose coordinate (PDB/GRO/DATA) to analyze:",
                    list_files(ex_path),
                )
            with col2:
                traj_file = st.selectbox(
                    "Choose trajectory (XTC/DCD/GRO/DATA/LAMMPSTRAJ) to analyze:",
                    list_files(ex_path),
                )

            if topo_file and traj_file:
                topo_ext = os.path.splitext(topo_file)[1].lower()
                traj_ext = os.path.splitext(traj_file)[1].lower()

                topo_path = os.path.join(ex_path, topo_file)
                traj_path = os.path.join(ex_path, traj_file)

                # Determine if LAMMPS formatting options are needed
                is_lammps = (
                    topo_ext in [".data"] + list(LMP_TRAJ_EXTS)
                    or traj_ext in [".data"] + list(LMP_TRAJ_EXTS)
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
                        elif topo_ext == ".data" and traj_ext in LMP_TRAJ_EXTS:
                            u = mda.Universe(
                                topo_path,
                                traj_path,
                                topology_format="DATA",
                                format="LAMMPSDUMP",
                                atom_style=atom_style_str,
                            )
                        elif (
                            topo_ext in LMP_TRAJ_EXTS
                            and traj_ext in LMP_TRAJ_EXTS
                        ):
                            st.warning(
                                "Both files are dump trajectories. Loading trajectory dump only."
                            )
                            u = mda.Universe(
                                traj_path,
                                format="LAMMPSDUMP",
                                atom_style=atom_style_str,
                            )
                        elif (
                            topo_ext in LMP_TRAJ_EXTS and traj_ext == ".data"
                        ):
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

    # ----------------------------------------------------
    # Manual Upload Mode
    # ----------------------------------------------------
    else:
        col1, col2 = st.columns(2)
        with col1:
            topo_file = st.file_uploader(
                "Upload coordinate (PDB/GRO/DATA)", type=["pdb", "gro", "data"]
            )
        with col2:
            traj_file = st.file_uploader(
                "Upload trajectory (XTC/DCD/GRO/DATA/LAMMPSTRAJ)",
                type=[
                    "xtc",
                    "dcd",
                    "gro",
                    "data",
                    "lammpstraj",
                    "dump",
                    "lammps",
                ],
            )

        if topo_file and traj_file:
            topo_name = topo_file.name.lower()
            traj_name = traj_file.name.lower()

            topo_ext = os.path.splitext(topo_name)[1]
            traj_ext = os.path.splitext(traj_name)[1]

            is_lammps = (
                topo_ext in [".data"] + list(LMP_TRAJ_EXTS)
                or traj_ext in [".data"] + list(LMP_TRAJ_EXTS)
            )

            atom_style_str = None
            if is_lammps:
                atom_style_str = st.text_input(
                    "Atom style for LAMMPS dump/data file",
                    value="id type x y z",
                    help="Specify LAMMPS column mapping (e.g., 'id type x y z' or 'full')",
                )

            # Route reading mode
            if topo_ext == ".data" and traj_ext == ".data":
                st.warning(
                    "Both files are DATA files. The trajectory slot will be ignored; loading DATA file only."
                )
                mode = "single_topo"
            elif topo_ext in LMP_TRAJ_EXTS and traj_ext in LMP_TRAJ_EXTS:
                st.warning(
                    "Both files are dump trajectories. The coordinate slot will be ignored; loading trajectory dump only."
                )
                mode = "single_traj"
            elif topo_ext == ".data" and traj_ext in LMP_TRAJ_EXTS:
                mode = "lammps_pair"
            elif topo_ext in LMP_TRAJ_EXTS and traj_ext == ".data":
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


                    