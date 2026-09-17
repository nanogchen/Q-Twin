import sys,os
from pathlib import Path
from ovito.io import import_file
from ovito.vis import ParticlesVis, TachyonRenderer, Viewport, BondsVis
from ovito.modifiers import WrapPeriodicImagesModifier,CreateBondsModifier,SliceModifier

def hex_to_rgb(hex_str):
	hex_str = hex_str.lstrip("#")
	return [int(hex_str[i : i + 2], 16) / 255.0 for i in (0, 2, 4)]

def color_bonds(frame, data):
	bond_topology = data.particles.bonds.topology
	colors = [hex_to_rgb(hex_colors) for i in range(len(bond_topology)) ]
		
	if data.particles.bonds:
		print(f"Color changed\n")
		data.particles_.bonds_.create_property("Color", data=colors)

if __name__ == '__main__':
	
	fname = "../../../data/colloids/L30_vf60_rate1.0.data"
	hex_colors = "#808080"  # use gray
	views = ['xy', 'xz']

	# 1. Load the LAMMPS data file
	pipeline = import_file(fname, atom_style="sphere")  
	pipeline.modifiers.append(WrapPeriodicImagesModifier())

	for view in views:

		if view == 'xy':

			# selection
			slice_mod1 = SliceModifier()
			slice_mod1.normal = (0, 0, 1)  # Cut along the X-axis instead
			slice_mod1.distance = 16.0     # Position of the plane along the normal
			slice_mod1.inverse = False      # Invert which side of the slice is kept/removed    
			pipeline.modifiers.append(slice_mod1)

			slice_mod2 = SliceModifier()
			slice_mod2.normal = (0, 0, 1)  # Cut along the X-axis instead
			slice_mod2.distance = 14.0     # Position of the plane along the normal
			slice_mod2.inverse = True      # Invert which side of the slice is kept/removed    
			pipeline.modifiers.append(slice_mod2)

		else:
			# selection
			# turn off previous selection
			pipeline.modifiers[1].enabled = False
			pipeline.modifiers[2].enabled = False

			slice_mod1 = SliceModifier()
			slice_mod1.normal = (0, 1, 0)  # Cut along the X-axis instead
			slice_mod1.distance = 16.0     # Position of the plane along the normal
			slice_mod1.inverse = False      # Invert which side of the slice is kept/removed    
			pipeline.modifiers.append(slice_mod1)

			slice_mod2 = SliceModifier()
			slice_mod2.normal = (0, 1, 0)  # Cut along the X-axis instead
			slice_mod2.distance = 14.0     # Position of the plane along the normal
			slice_mod2.inverse = True      # Invert which side of the slice is kept/removed    
			pipeline.modifiers.append(slice_mod2)

		# create bonds 
		bonds_vis = BondsVis()
		bondModifier = CreateBondsModifier(cutoff=0.98,  
									mode=CreateBondsModifier.Mode.Uniform,
									vis=bonds_vis,
									)

		pipeline.modifiers.append(bondModifier)
		pipeline.modifiers.append(color_bonds)
		bonds_vis.width = 0.2

		data = pipeline.compute()
		# Disable the Particles visual element
		# This will hide the particles from the visualization
		data.particles.vis.enabled = False
		data.particles.bonds.vis.enabled = True
		cell_vis = data.cell.vis
		cell_vis.line_width = 0.1
		cell_vis.render_cell = True

		pipeline.add_to_scene()
		# 5. Set up the viewport and camera position		
		if view == "xy":
			vp = Viewport(type = Viewport.Type.Top)
		else:
			vp = Viewport(type = Viewport.Type.Front)
			
		vp.zoom_all(size=(900,900))  # Automatically fits the camera to the simulation box

		# 6. Configure and run the Tachyon Renderer
		renderer = TachyonRenderer(
			shadows=True,  # Enable realistic shadows
			ambient_occlusion=True,  # Enhanced depth perception
		)

		# Render the image
		outname = view+'.png'

		vp.render_image(
			filename=outname,
			size=(900, 900),
			background=(1.0, 1.0, 1.0),  # White background
			renderer=renderer,
		)

		print(f"Rendering complete! Saved as {outname}.")
