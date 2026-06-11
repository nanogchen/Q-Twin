# Q-Twin
A Digital Twin for Molecular Scattering, with a graphical user interface that can be used locally or in the cloud. 

<p align="center" width="70%">
    <img width="60%" src="schematic.jpg">
</p>

## Core objectives
* Streamline the extraction of static structure factors and dynamical correlation functions from molecular dynamics trajectories.
* Capture long-range spatial correlations and collective dynamics in critical phenomena.
* Apply the framework across unary and binary liquids utilizing both generic coarse-grained and chemically specific atomistic models.
* Enable direct, reciprocal-space comparisons with small-angle scattering and photon correlation spectroscopy experiments.

## How to use

### Local mode
Main packages used are included in the requirements.txt file and can be installed by one of the following ways:
> (myenv) conda install --file requirements.txt
> 
> (myenv) pip install -r requirements.txt

Switch into the python environment with above installation, then launch:
> streamlit run app.py

### GUI version
Use the "install-free" version deployed in the cloud https://q-twin.streamlit.app/.

## How to cite
G. Chen, X. Lin, S. Narayanan, S. K.R.S. Sankaranarayanan. "Q-Twin: The Digital Twin Beamline for Molecular Scattering". In submission (2026).
