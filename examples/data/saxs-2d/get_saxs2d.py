import sys
import numpy as np
import MDAnalysis as mda

sys.path.insert(0, "../../../")
from srcs.calc import get_scattering_image

# -----------------------------------------------------------------------------

if __name__ == '__main__':

	traj_file = "/pscratch/sd/g/guangc/shear/vf60_L50/rate1.0/shear_rate1.xtc" # a very large file
	unit_conv = 10.0 # unit conversion
	Fr_start = 2000
	Fr_step = 1
	Fr_stop = 3000
	q_max = 20

	u = mda.Universe(traj_file)
	system = u.select_atoms("all")
	bx,by,bz=u.dimensions[:3]/unit_conv

	# gen q-points and calculate structure factor 2d
	_,_,_,_,ssf_2d = get_scattering_image(np.array([bx,by,bz]), q_max, system, u.trajectory[Fr_start:Fr_stop+1:Fr_step], plane='xz', unit_conv=unit_conv)

	# save
	np.save("ssf_2d_xz.npy", ssf_2d)

	# another plane
	_,_,_,_,ssf_2d = get_scattering_image(np.array([bx,by,bz]), q_max, system, u.trajectory[Fr_start:Fr_stop+1:Fr_step], plane='xy', unit_conv=unit_conv)

	# save
	np.save("ssf_2d_xy.npy", ssf_2d)
	