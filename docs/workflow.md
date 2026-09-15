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
Note that the demonstration shown here was performed using a single frame, so relatively large statistical uncertainties are expected. For more reliable statistics, use a larger number of frames for averaging (e.g., 500 frames). For dynamic analysis, multiple frames are required to obtain meaningful statistics.

<p align="center">
	<img width="100%" src="../assets/step3.jpg" alt="Results view and data download">
</p>
<p align="center"><em>Results view and data download of the Q-Twin analysis.</em></p>

### Command line usage
To facilitate autonomous analysis of multiple systems, the analysis can be performed from the command line or within a Bash/Python script. Here, the same example is used to demonstrate the command-line workflow.

The example script, test.py, is shown below. The file is located under Q-Twin/examples/.
```python
import sys
import numpy as np
import MDAnalysis as mda

sys.path.insert(0, "../")
from srcs.q_gen import get_q_points_all_quads, get_binning_averages
from srcs.calc import get_static_sf

# -----------------------------------------------------------------------------

if __name__ == '__main__':

	u = mda.Universe("unary_scf.data", format="DATA", atom_style="id type x y z")
	system = u.select_atoms("all")
	bx,by,bz=u.dimensions[:3]
	n_atoms = len(system.atoms)
	formfact_all = np.ones(n_atoms)
	
	# lj liquids
	q_end = 15.0
	max_points = 1500
	num_q_bins = 15
	Fr_start = 0
	Fr_stop = 1
	Fr_step = 1

	# gen q-points and calculate structure factor
	q_points = get_q_points_all_quads(np.array([bx, by, bz]), q_end, max_points=max_points)
	ssf = get_static_sf(q_points, system, u.trajectory[Fr_start:Fr_stop+1:Fr_step], formfact_all)
	qr, ssf_qr = get_binning_averages(num_q_bins, q_end, ssf, q_points)

	# # save
	# np.save("qr.npy", qr)
	# np.save("ssf_qr.npy", ssf_qr)
```

Then in a command line:
```bash
conda activate qtwin
(qtwin) python test.py
```
