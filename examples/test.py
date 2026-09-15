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