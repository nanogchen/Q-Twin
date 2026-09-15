# Q-Twin
A Digital-Twin Beamline for Molecular Scattering and Coherent Dynamics, with a graphical user interface that can be used locally or in the cloud. 

<p align="center" width="70%">
    <img width="60%" src="schematic.jpg">
</p>

## Core objectives
* Streamline the extraction of static structure factors and dynamical correlation functions from molecular dynamics trajectories.
* Capture long-range spatial correlations and collective dynamics in critical phenomena.
* Apply the framework across unary and binary liquids utilizing both generic coarse-grained and chemically realistic models.
* Enable direct, reciprocal-space comparisons with small-angle scattering and photon correlation spectroscopy experiments.

## How to use
For detailed installation and usage instructions, please refer to the `Q-Twin` [documentation](https://nanogchen.github.io/Q-Twin/). A brief overview of the steps is provided below.

### Local mode
Main packages used are included in the requirements.txt file and can be installed by:
> conda create --name qtwin --file requirements.txt  
> conda activate qtwin

Switch into the python environment with above installation, then launch:
> streamlit run app.py

### GUI version
Use the "install-free" version deployed in the cloud https://q-twin.streamlit.app/. But note that this free version is limited to up to 2 cores and 1 GB standard RAM memory (with a burst maximum of up to 2.7 GB). Only use this for small systems. For production research, use local HPC resources. 

## How to cite
G. Chen, X. Lin, S. Narayanan, S. K.R.S. Sankaranarayanan. "Q-Twin: A Digital Twin Beamline for Molecular Scattering and Coherent Dynamics". In submission (2026).

## Documentation and User Guide
Please refer to the [documentation](https://nanogchen.github.io/Q-Twin/) and user guide of the code. 

## Seek new features or bug reports
Open an [issue](https://github.com/nanogchen/Q-Twin/issues)!
