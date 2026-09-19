# 
# Copyright (C) Guang Chen et al.
# 
# This file is part of Q-Twin program
#

import itertools
import numpy as np
from numba import njit, prange

idx_dict = {"xz":[0,2],
			"xy":[0,1],
			"yz":[1,2],
			}

def get_q_points_plane(box, q_max, plane='xz'):
	"""Construct q-points in a plane: xz with norm-y or xy with norm-z

	Args:
		box (np.array): simulation box [bx, by, bz]
		q_max (float): max q
		plane (str): scattering plane xy/xz/yz

	Returns:
		q1 (np.array): the q-points in the first direction or x
		q2 (np.array): the q-points in the first direction or z
		q_points (np.array): the generated q-points in a plane
	"""

	idx_list=idx_dict[plane]

	box2 = box[idx_list]
	dq = np.diagflat(2*np.pi/box2)
	N = np.ceil(q_max/np.diag(dq)).astype(int)

	# form the q-points in each of the two direction
	q1 = np.arange(-N[0], N[0]+1) * dq[0,0] # 2*N+1
	q2 = np.arange(-N[1], N[1]+1) * dq[1,1]

	# the q-points
	qpts1, qpts2 = np.meshgrid(q1, q2)
	q_points2 = np.stack((qpts1.ravel(), qpts2.ravel()), axis=-1)
	q_points = np.zeros((q_points2.shape[0], 3))
	q_points[:, idx_list] = q_points2

	return q1,q2,q_points

def get_q_points_ring(box, qmin, qmax, plane):
	"""Construct q-points along a ring: xz with norm-y or xy with norm-z

	Args:
		box (np.array): simulation box [bx, by, bz]
		qmin (float): min q
		qmax (float): max q
		plane (str): scattering plane xy/xz/yz

	Returns:
		q_points (np.array): the generated q-points
	"""

	# in a circle
	_,_,q_points = get_q_points_plane(box, qmin+qmax, plane)

	# distance measure and sort out
	q_dist = np.linalg.norm(q_points, axis=1)
	argsort = np.argsort(q_dist)
	q_dist = q_dist[argsort]
	q_points = q_points[argsort]

	# prune based on q-range
	mask = (q_dist >= qmin) & (q_dist <= qmax)
	q_points = q_points[mask]

	return q_points

def get_q_points_angular_bin(box, qmin, qmax, Nbins, angle_deg, plane):
	"""Construct q-points in an angular bin along a ring: xz with norm-y or xy with norm-z

	Args:
		box (np.array): simulation box [bx, by, bz]
		qmin (float): min q
		qmax (float): max q
		Nbins (int): the number of q-bins along the ring
		angle_deg (float): the angle of the target bin
		plane (str): scattering plane xy/xz/yz

	Returns:
		q_points (np.array): the generated q-points
	"""

	idx_list=idx_dict[plane]

	# generate the q-ring
	q_points = get_q_points_ring(box, qmin, qmax, plane)
	q_points2 = q_points[:, idx_list]
	
	# Calculate q-angles in radians (range -pi to pi)
	angles = np.arctan2(q_points2[:, 1], q_points2[:, 0])
	bin_edges = np.linspace(-np.pi, np.pi, Nbins + 1)
	bin_indices = np.digitize(angles, bin_edges, right=True)
	
	bin_idx_target = np.digitize(np.deg2rad(angle_deg), bin_edges)
	qpoints2_bin = q_points2[bin_indices == bin_idx_target]

	q_points = np.zeros((qpoints2_bin.shape[0], 3))
	q_points[:, idx_list] = qpoints2_bin

	return q_points

def get_q_points_on_principal_axis(q_points, qTarget=7.6, dq=0.4, dtheta=10, plane='xz'):
	"""Construct q-points in two principal bins (0 and 90 degree) along a ring: xz with norm-y or xy with norm-z

	Args:
		q_points (np.array): the raw q-points in the plane
		qTarget (float): the target wavenumber
		dq (float): the bin step for q-points selection
		dtheta (float): the angle step for q-points selection
		plane (str): scattering plane xy/xz/yz

	Returns:
		q_points_x (np.array): the q-points in the 0-direction
		q_points_y (np.array): the q-points in the 90-direction
	"""

	idx_list=idx_dict[plane]

	q_norms = np.linalg.norm(q_points, axis=1)
	q_indices = np.where(np.abs(q_norms - qTarget) <= dq)[0]

	# selection by norm
	q_points_norm2d = q_points[q_indices]
	q_points_2d = q_points_norm2d[:, idx_list]

	# selection by direction (on a plane)
	q_list_x = []
	q_list_y = []

	for iq in q_points_2d:
		# along x: cos
		costheta = iq[0] / np.linalg.norm(iq)
		if costheta >= np.cos(dtheta/180.0*np.pi):
			q_list_x.append(iq)

		# along y: sin
		sintheta = iq[1] / np.linalg.norm(iq) 
		if sintheta >= np.sin(0.5*np.pi - dtheta/180.0*np.pi):
			q_list_y.append(iq)

	# return it in 3d
	q_list_x = np.array(q_list_x)
	q_list_y = np.array(q_list_y)
	q_points_x = np.zeros((q_list_x.shape[0], 3))
	q_points_x[:, idx_list] = q_list_x
	q_points_y = np.zeros((q_list_y.shape[0], 3))
	q_points_y[:, idx_list] = q_list_y

	return q_points_x, q_points_y

def filter_q_points_shell(q_points, qmin, qmax):
	"""filter q-points in a 3-d shell by a q-range

	Args:
		q_points (np.array): the wavevectors with dimensions [Nq, 3]
		qmin (float): min q
		qmax (float): max q

	Returns:
		q_points (np.array): the generated q-points
	"""

	q_dist = np.linalg.norm(q_points, axis=1)
	argsort = np.argsort(q_dist)
	q_dist = q_dist[argsort]
	q_points = q_points[argsort]

	mask = (q_dist >= qmin) & (q_dist <= qmax)
	q_points_shell = q_points[mask]

	return q_points_shell

"""from dynasor, with some modification"""

@njit(fastmath=True, nogil=True)
def dot3(a,b):
	return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]

@njit(fastmath=True, nogil=True, parallel=True)
def get_rho_q(x, q, formfact_all):
	"""get density field over all q-points with given form factor

	Args:
		x (np.array): the coordinates of the system [Np, 3]
		q (np.array): the wavevectors with dimensions [Nq, 3]
		formfact_all (np.array): the form factor for the systems [Np]

	Returns:
		rho_q (np.array): the density field
	"""

	Nx = len(x)
	Nq = len(q)

	rho_q = np.zeros(Nq, dtype=np.complex128)

	# parallel
	for iq in prange(Nq):

		rho = 0.0j
		for ix in range(Nx):
			alpha = dot3(x[ix], q[iq])
			rho += np.exp(-1j * alpha) * formfact_all[ix]

		rho_q[iq] = rho

	return rho_q

@njit(fastmath=True, nogil=True, parallel=True)
def get_rho_q_noFF(x, q):
	"""get density field over all q-points without given form factor

	Args:
		x (np.array): the coordinates of the system [Np, 3]
		q (np.array): the wavevectors with dimensions [Nq, 3]
	
	Returns:
		rho_q (np.array): the density field	
	"""

	Nx = len(x)
	Nq = len(q)

	rho_q = np.zeros(Nq, dtype=np.complex128)

	# prange is like OMP
	for iq in prange(Nq):

		rho = 0.0j
		for ix in range(Nx):
			alpha = dot3(x[ix], q[iq])
			rho += np.exp(-1j * alpha)

		rho_q[iq] = rho

	return rho_q

def get_prune_distance(max_points, q_max, q_vol):
	#from dynasor: originally just first-quadrant
	Q = q_max
	V = q_vol
	N = max_points

	# Coefs
	a = 1.0
	b = -3 / 2 * Q
	c = 0.0
	d = 3 / 2 * V * N / (4 * np.pi)

	# Eq tol solve
	def original_eq(x):
		return a * x**3 + b * x**2 + c * x + d
	# original_eq = lambda x:  a * x**3 + b * x**2 + c * x + d

	# Discriminant
	p = (3 * a * c - b**2) / (3 * a**2)
	q = (2 * b**3 - 9 * a * b * c + 27 * a**2 * d) / (27 * a**3)

	D_t = - (4 * p**3 + 27 * q**2)
	if D_t < 0:
		return q_max

	x = Q * (np.cos(1 / 3 * np.arccos(1 - 4 * d / Q**3) - 2 * np.pi / 3) + 0.5)

	# assert np.isclose(original_eq(x), 0, rtol=1e-05, atol=1e-06), original_eq(x)

	return x

def get_q_points_all_quads(box, q_max, max_points, seed=42):
	"""Construct q-points in 3d space (all-quads)

	Args:
		box (np.array): simulation box [bx, by, bz]
		q_max (float): max q
		max_points (int): the maximum number of q-points
		seed (int): the seed for the q-points sampling

	Returns:
		q_points (np.array): the generated q-points
	"""

	dq = np.diagflat(2*np.pi/box)
	N = np.ceil(q_max/np.diag(dq)).astype(int)

	lattice_points = list(itertools.product(*[range(-n, n+1) for n in N]))
	q_points = lattice_points @ dq

	# distance measure and sort out
	q_dist = np.linalg.norm(q_points, axis=1)
	argsort = np.argsort(q_dist)
	q_dist = q_dist[argsort]
	q_points = q_points[argsort]

	# prune based on max_q
	q_points = q_points[q_dist <= q_max]
	q_dist = q_dist[q_dist <= q_max]

	# prune based on max_Npoints
	if max_points < len(q_points):

		q_vol = dq[0,0]*dq[1,1]*dq[2,2]
		q_prune = get_prune_distance(max_points, q_max, q_vol)

		if q_prune < q_max:
			print(f'Pruning q-points from the range {q_prune:.3} < |q| < {q_max}')
			p = np.ones(len(q_points))
			assert np.isclose(q_dist[0], 0)
			p[1:] = (q_prune / q_dist[1:]) ** 2

			rs = np.random.RandomState(seed)
			q_points = q_points[p > rs.rand(len(q_points))]
			print(f'Pruned from {len(q_dist)} q-points to {len(q_points)}')

	return q_points

def get_binning_averages(num_q_bins, q_end, data_in_q_t, q_points):
	"""Get q-averaged data by q-binning

	Args:
		num_q_bins (int): the number of q-bins
		q_end (float): max q
		data_in_q_t (np.array): the data for q-binning [Nq, Nt]
		q_points (np.array): the q-points

	Returns:
		q_bincenters (np.array): the bin centers of the 1-d q
		averaged_data (np.array): the binned data
	"""

	# do binning
	Nframes = data_in_q_t.shape[1]
	q_norms = np.linalg.norm(q_points, axis=1)

	# setup bins
	bin_counts, edges = np.histogram(q_norms, bins=num_q_bins, range=(0.0, q_end))
	q_bincenters = 0.5 * (edges[1:] + edges[:-1])

	# calculate average for each bin
	averaged_data = np.zeros((num_q_bins, Nframes))
	for bin_index in range(num_q_bins):
		# find q-indices that belong to this bin
		bin_min = edges[bin_index]
		bin_max = edges[bin_index + 1]
		bin_count = bin_counts[bin_index]
		q_indices = np.where(np.logical_and(q_norms >= bin_min, q_norms < bin_max))[0]

		# average over q-indices, if no indices then np.nan
		if bin_count == 0:
			print(f'No q-points for bin {bin_index}')
			data_bin = np.array([np.nan for _ in range(Nframes)])
		else:
			data_bin = data_in_q_t[q_indices, :].mean(axis=0)
		averaged_data[bin_index, :] = data_bin

	return q_bincenters, averaged_data

def get_binning_averages_by_range(num_q_bins, q_min, q_max, data_in_q_t, q_points):
	"""Get q-averaged data by q-binning in a q-range

	Args:
		num_q_bins (int): the number of q-bins
		q_min (float): min q
		q_max (float): max q
		data_in_q_t (np.array): the data for q-binning [Nq, Nt]
		q_points (np.array): the q-points

	Returns:
		q_bincenters (np.array): the bin centers of the 1-d q
		averaged_data (np.array): the binned data
	"""	

	# do binning
	Nframes = data_in_q_t.shape[1]
	q_norms = np.linalg.norm(q_points, axis=1)

	# setup bins
	bin_counts, edges = np.histogram(q_norms, bins=num_q_bins, range=(q_min, q_max))
	q_bincenters = 0.5 * (edges[1:] + edges[:-1])

	# calculate average for each bin
	averaged_data = np.zeros((num_q_bins, Nframes))
	for bin_index in range(num_q_bins):
		# find q-indices that belong to this bin
		bin_min = edges[bin_index]
		bin_max = edges[bin_index + 1]
		bin_count = bin_counts[bin_index]
		q_indices = np.where(np.logical_and(q_norms >= bin_min, q_norms < bin_max))[0]

		# average over q-indices, if no indices then np.nan
		if bin_count == 0:
			print(f'No q-points for bin {bin_index}')
			data_bin = np.array([np.nan for _ in range(Nframes)])
		else:
			data_bin = data_in_q_t[q_indices, :].mean(axis=0)
		averaged_data[bin_index, :] = data_bin

	return q_bincenters, averaged_data

def get_binning_averages_ttc(q_points, ssf, I_q_t1_t2, form="G"):
	"""Get q-averaged two-time correlation function by q-binning

	Args:
		q_points (np.array): the q-points
		ssf (np.array): the static structure factor [Nq, Nt]
		I_q_t1_t2 (np.array): the two-time correlation function [Nq, Nt, Nt]
		form (str): the form of binning average

	Returns:
		q_bincenters (np.array): the bin centers of the 1-d q
		averaged_c2 (np.array): the binned two-time correlation		
	"""	
	Nframes = I_q_t1_t2.shape[1]

	# 1 q-bin (either along x or y or z)
	averaged_c2 = np.zeros((Nframes, Nframes))
	q_bincenters = np.mean(np.linalg.norm(q_points, axis=1))

	if form == "G": #  = (<I1*I2> - <I1>*<I2>) / (sigma(I1)*sigma(I2)); G=C-1

		for i in range(Nframes):
			for j in range(i, Nframes):

				nominator = np.mean(I_q_t1_t2[:, i, j],axis=0) - (np.mean(ssf[:, i],axis=0)) * (np.mean(ssf[:, j], axis=0))
				denominator = np.std(ssf[:, i], axis=0) * np.std(ssf[:, j], axis=0) 

				averaged_c2[i, j] = nominator / denominator
				averaged_c2[j, i] = averaged_c2[i, j]

	elif form == "C": #  = <I1*I2> / (<I1>*<I2>)

		for i in range(Nframes):
			for j in range(i, Nframes):

				nominator = I_q_t1_t2[:, i, j].mean(axis=0)
				denominator = (np.mean(ssf[:, i],axis=0)) * (np.mean(ssf[:, j],axis=0))

				averaged_c2[i, j] = nominator / denominator
				averaged_c2[j, i] = averaged_c2[i, j]
	else:
		print(f"Unknown form ({form}) for calculating two-time correlation! Can ONLY be G or C()")

	return q_bincenters, averaged_c2
