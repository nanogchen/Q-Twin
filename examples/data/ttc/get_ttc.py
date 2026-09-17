import sys
import numpy as np
import MDAnalysis as mda

sys.path.insert(0, "../../../")
from srcs.q_gen import get_q_points_plane, get_q_points_on_principal_axis, get_binning_averages_ttc
from srcs.calc import get_ttc

# -----------------------------------------------------------------------------

if __name__ == '__main__':

	traj_file = "cessation_rate1.xtc" # a very large file
	unit_conv = 10 # unit conversion
	Fr_start = 5000
	Fr_step = 1
	Fr_stop = 6000
	q_end = 10

	u = mda.Universe(traj_file)
	system = u.select_atoms("all")
	bx,by,bz=u.dimensions[:3]/unit_conv
	n_atoms = len(system.atoms)
	formfact_all = np.ones(n_atoms)

	# gen q-points and calculate two-time correlation

	####################################################################### do xy plane
	_,_,q_points = get_q_points_plane(np.array([bx, by, bz]), q_end, plane='xy')
	q_points_1, q_points_2 = get_q_points_on_principal_axis(q_points, qTarget=7.6, dq=0.4, dtheta=10, plane='xy')
	# if generate q-points for a given bin
	# q_points = get_q_points_angular_bin(box, q_min, q_max, Nbins, angle_deg, plane)

	ssf, I_q_t1_t2 = get_ttc(q_points_1, system, u.trajectory[Fr_start:Fr_stop+1:Fr_step], formfact_all, unit_conv)
	_, c2 = get_binning_averages_ttc(q_points_1, ssf, I_q_t1_t2, form="G")
	# save
	np.save(f"c2_ttc_xy1.npy", c2)
	
	ssf, I_q_t1_t2 = get_ttc(q_points_2, system, u.trajectory[Fr_start:Fr_stop+1:Fr_step], formfact_all, unit_conv)
	_, c2 = get_binning_averages_ttc(q_points_2, ssf, I_q_t1_t2, form="G")
	# save
	np.save(f"c2_ttc_xy2.npy", c2)

	####################################################################### do xz plane
	_,_,q_points = get_q_points_plane(np.array([bx, by, bz]), q_end, plane='xz')
	q_points_1, q_points_2 = get_q_points_on_principal_axis(q_points, qTarget=7.6, dq=0.4, dtheta=10, plane='xz')

	ssf, I_q_t1_t2 = get_ttc(q_points_1, system, u.trajectory[Fr_start:Fr_stop+1:Fr_step], formfact_all, unit_conv)
	_, c2 = get_binning_averages_ttc(q_points_1, ssf, I_q_t1_t2, form="G")	
	# save
	np.save(f"c2_ttc_xz1.npy", c2)
	
	ssf, I_q_t1_t2 = get_ttc(q_points_2, system, u.trajectory[Fr_start:Fr_stop+1:Fr_step], formfact_all, unit_conv)
	_, c2 = get_binning_averages_ttc(q_points_2, ssf, I_q_t1_t2, form="G")		
	# save
	np.save(f"c2_ttc_xz2.npy", c2)
