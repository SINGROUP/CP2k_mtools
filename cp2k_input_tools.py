# -*- coding: utf-8 -*-
import sys
import numpy as np

from ase import Atoms
from ase.constraints import FixAtoms


def set_cell_pbc(SUBSYS, atoms):
   pbc = atoms.get_pbc()
   periodic_str = ''
   if pbc[0]:
      periodic_str = periodic_str+'X'
   if pbc[1]:
      periodic_str = periodic_str+'Y'
   if pbc[2]:
      periodic_str = periodic_str+'Z'
   if len(periodic_str) == 0:
      periodic_str = "NONE"
   SUBSYS.CELL.Periodic = periodic_str


def set_poisson_solver(DFT, atoms):
   pbc = atoms.get_pbc()
   periodic_str = ''
   if pbc[0]:
      periodic_str = periodic_str+'X'
   if pbc[1]:
      periodic_str = periodic_str+'Y'
   if pbc[2]:
      periodic_str = periodic_str+'Z'
   if len(periodic_str) == 0:
      periodic_str = "NONE"
   
   if pbc[0] and pbc[1] and pbc[2]:
      solver = "PERIODIC"
   elif pbc[0] and pbc[2]:
      solver = "WAVELET"
   elif not(pbc[0]) and not(pbc[1]) and not(pbc[2]):
      solver = "WAVELET"
   else:
      sys.exit('No poisson solver in CP2k for these periodic boundary conditions!\n')

   DFT.POISSON.Periodic = periodic_str
   DFT.POISSON.Poisson_solver = solver


def set_fixed_atoms(MOTION, fixed_indices):
   constraint_list = ''
   for index in fixed_indices:
      constraint_list = constraint_list+repr(index+1)+' '
      
   FIXED_ATOMS = MOTION.CONSTRAINT.FIXED_ATOMS_add()
   FIXED_ATOMS.Components_to_fix = 'XYZ'
   FIXED_ATOMS.List = constraint_list


def set_fixed_atoms_ASE(MOTION, atoms):
        """Creates the constraints corresponding to ASE's FixAtoms class.

        args:
            subsys: The MOTION section of pycp2k calculators input.
            atoms: ASE Atoms
                Atoms from which the FixAtom contraint is extracted.
        """
        CONSTRAINT = MOTION.CONSTRAINT
        constraints = atoms.constraints
        n_constraints = 0
        if type(constraints) is not list:
            constraints = [constraints]
        for constraint in constraints:
            # FixAtoms -> CONSTRAINT.FIXED_ATOMS
            n_constraints += 1
            if isinstance(constraint, FixAtoms):
                if len(constraint.index) == len(atoms) and all(i <= 1 for i in constraint.index):
                    indices = np.where(constraint.index)[0]
                else:
                    indices = constraint.index
                # CP2K indexing starts at 1
                indices = [x+1 for x in indices]
                fixed_atoms = CONSTRAINT.FIXED_ATOMS_add()
                fixed_atoms.Components_to_fix = "XYZ"
                fixed_atoms.List = " ".join(map(str, indices))
        if n_constraints == 0:
            print_warning("No 'FixAtoms' constraints found.")
