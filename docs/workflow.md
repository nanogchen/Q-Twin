## Workflow

The software workflow consists of the following steps:

1. Trajectory Setup: Upload a simulation trajectory or load one of the preinstalled trajectories.
2. System Summary: Review the automatically generated summary of the simulation system.
3. (q,t) Setup: Specify the parameters of interest for q and time, and select the desired analysis tasks.
4. Review Outputs: Navigate to the corresponding tabs to review the analysis results. Note that only the selected tasks will be activated and displayed.

### Example
Here the supercritical Lennard-Jones liquid is used as an example.

<p align="center">
    <img width="100%" src="../assets/step1.jpg" alt="Load the trajectory">
</p>
<p align="center"><em>Trajectory loading for the Q-Twin analysis.</em></p>

<p align="center">
    <img width="100%" src="../assets/step2.jpg" alt="Set the (q,t) and tasks">
</p>
<p align="center"><em>Set the (q,t) and tasks for the Q-Twin analysis.</em></p>

For demonstration, the following parameters were used:
```json
{
    "topo_file": "unary_scf.data",
    "traj_file": "unary_scf.data",
    "atom_style": "id type x y z",
    "length_unit": "LJ",
    "q_end": 15.0,
    "max_q_points": 1500,
    "frame_start": 0,
    "frame_end": 1,
    "frame_step": 10, 
    "traj_dt": 1.0,
    "tasks": "SAXS-1D",
}
```
Note that the analysis was done for a single frame. Large uncertainty is expected. To get better statistics, use more frames for averages (e.g., 500 frames).

<p align="center">
    <img width="100%" src="../assets/step3.jpg" alt="Results view and data download">
</p>
<p align="center"><em>Results view and data download of the Q-Twin analysis.</em></p>

### Command line usage

