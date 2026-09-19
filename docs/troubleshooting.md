## Issues and Caveats

#### Network Issue

1. go to `chrome://net-internals/#sockets`, and click `Flush socket pools`.
2. go to `chrome://net-internals/#dns`, and click `Clear host cache`.
3. go to `chrome://net-internals/#hsts`, navigate to Delete domain security policies, and enter `nanogchen.github.io`, click `Delete`.
4. open terminal and run: `ipconfig /flushdns`.

---

#### Saxs2d Plotting Caveat

In the development version of the code, the 2D SAXS scattering data have the shape  `[Nt, Nq, Nq]`. Accordingly, the averaging was performed along the first axis (`axis=0`), as reflected in the data uploaded to Zenodo and in `figs.ipynb`.

In the most recent version, the data shape has been changed to `[Nq, Nq, Nt]`. Therefore, the averaging should now be performed along the last axis (`axis=-1`).

---

#### LAMMPS Data Parsing Caveat

The `atom_style` setting in trajectory loading is critical for correctly extracting particle positions during analysis. If it is not specified correctly, the postprocessing results can be incorrect.

--- 

#### q-Averaging Caveat

The number of q-bins, or the value of wavenumber step, used for q-averaging can affect the exact values of the resulting wavenumber array. As requested by the reviewer, the default setting in the GUI and the saxs2d example has been set to `int(q_max / round(1.5 * 2 * np.pi / L, 2))`.

Note that this setting is not incorrect; rather, it is an adjustable parameter that controls the q-binning and does not affect the underlying results.
