## Issues and Caveats

#### Network issue

1. go to `chrome://net-internals/#sockets`, and click `Flush socket pools`.
2. go to `chrome://net-internals/#dns`, and click `Clear host cache`.
3. go to `chrome://net-internals/#hsts`, navigate to Delete domain security policies, and enter `nanogchen.github.io`, click `Delete`.
4. open terminal and run: `ipconfig /flushdns`.

---

#### Saxs2d plotting issue

In the development version of the code, the 2D SAXS scattering data have the shape  `[Nt, Np, Np]`. Accordingly, the averaging was performed along the first axis (`axis=0`), as reflected in the data uploaded to Zenodo and in `figs.ipynb`.

In the most recent version, the data shape has been changed to `[Np, Np, Nt]`. Therefore, the averaging should now be performed along the last axis (`axis=-1`).

---

#### LAMMPS Data Parsing Caveat

The `atom_style` setting in trajectory loading is critical for correctly extracting particle positions during analysis. If it is not specified correctly, the postprocessing results can be incorrect.

--- 

