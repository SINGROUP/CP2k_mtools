# -*- coding: utf-8 -*-
#!/usr/bin/python

import numpy as np
import sys

from ase import Atoms
from ase.lattice.surface import fcc111
from ase.constraints import FixAtoms
from ase.visualize import view

from pycp2k.cp2k import CP2K
from cp2k_init import CP2k_init

# Parameters
project_name = 'Ir111_pyramid111_efield'
ir_cells = 10
ir_slab_depth = 3
ir_pyramid_depth = 3
vacuum = 8.0
bn_cells = 11
a_bn = 2.514
a_ir = bn_cells*a_bn/ir_cells*np.sqrt(2)
efield = 0.1 # V/Å

# Calculate normal vectors of the sides of the pyramid
theta = np.arctan(1/np.sqrt(2.0))
phi_1 = np.pi/2.0
phi_2 = 11.0*np.pi/6.0
phi_3 = 7.0*np.pi/6.0
evec_1 = np.array([np.sin(theta)*np.cos(phi_1), np.sin(theta)*np.sin(phi_1), np.cos(theta)])
evec_2 = np.array([np.sin(theta)*np.cos(phi_2), np.sin(theta)*np.sin(phi_2), np.cos(theta)])
evec_3 = np.array([np.sin(theta)*np.cos(phi_3), np.sin(theta)*np.sin(phi_3), np.cos(theta)])
nvec_12 = np.cross(evec_1, evec_2)
nvec_23 = np.cross(evec_2, evec_3)
nvec_31 = np.cross(evec_3, evec_1)

# Build a thick slab and remove atoms from the bottom layers to form a pyramid
ir111_pyramid = fcc111('Ir', size=(ir_cells, 2*ir_cells, ir_slab_depth+ir_pyramid_depth), a=a_ir, orthogonal=True)
ir111_pyramid.positions = np.array([ir111_pyramid.positions[:, 0], ir111_pyramid.positions[:, 1], -ir111_pyramid.positions[:, 2]]).T
ir111_pyramid.center(vacuum = 0, axis=2)
dr_atom_1 = ir111_pyramid.cell[0, :]/ir_cells
dr_atom_2 = ir111_pyramid.cell[1, :]/ir_cells
tip_atom_pos = int(ir_cells/2)*(dr_atom_1 + dr_atom_2)
atom_delete_list = []
for atom in ir111_pyramid:
    dr_atom_tip = atom.position - tip_atom_pos
    if atom.tag <= ir_pyramid_depth:
        if (np.dot(dr_atom_tip, nvec_12) > 0.1 or
            np.dot(dr_atom_tip, nvec_23) > 0.1 or
            np.dot(dr_atom_tip, nvec_31) > 0.1):
            atom_delete_list.append(atom.index)
del ir111_pyramid[atom_delete_list]
ir111_pyramid.center(vacuum = vacuum, axis=2)

# Rotate the non-periodic z axis to be along y axis so that wavelet solver with surface BC can be used
ir111_pyramid.rotate('y', -np.pi/2.0, rotate_cell=False)
ir111_pyramid.rotate('z', -np.pi/2.0, rotate_cell=False)
cell = np.array([[ir111_pyramid.cell[1, 1], ir111_pyramid.cell[1, 2], -ir111_pyramid.cell[1, 0]],
                 [ir111_pyramid.cell[2, 1], ir111_pyramid.cell[2, 2], ir111_pyramid.cell[2, 0]],
                 [ir111_pyramid.cell[0, 1], ir111_pyramid.cell[0, 2], ir111_pyramid.cell[0, 0]]])
ir111_pyramid.set_cell(cell)
ir111_pyramid.set_pbc([True, False, True])
tip_atom = ir111_pyramid[[atom.index for atom in ir111_pyramid if atom.tag == 1]]
tip_atom = tip_atom[0]
tip_atom_pos = tip_atom.position
cell_center = 0.5*np.sum(ir111_pyramid.cell, axis=0)
tip_translation = cell_center - tip_atom_pos
tip_translation[1] = 0.0
ir111_pyramid.translate(tip_translation)
ir111_pyramid.wrap()

fix_constraint = FixAtoms(mask=[atom.tag > ir_pyramid_depth+1 for atom in ir111_pyramid])
ir111_pyramid.set_constraint(fix_constraint)

#view(ir111_pyramid)
#sys.exit()

# Initialize the PYCP2k calculator object                                                                                                                                                                           
cp2k_initializer = CP2k_init(project_name, ir111_pyramid)
cp2k_calc = cp2k_initializer.init_calc_potential(V=1.0, E_per_V=efield)

# Run the calculation
#cp2k_calc.write_input_file()
cp2k_calc.run()
