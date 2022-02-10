# whatever try
'''
# at the moment not used
import numpy as np

fix_list = np.loadtxt('fixed_indices.txt')
'''
def set_system_specific_params(DFT, SCF, SUBSYS):
    DFT.Basis_set_file_name = "BASIS_MOLOPT"
    DFT.Potential_file_name = "GTH_POTENTIALS"
    
    KIND = SUBSYS.KIND_add("H")  # Section_parameters can be provided as argument.
    KIND.Basis_set = "DZVP-MOLOPT-SR-GTH"
    KIND.Potential = "GTH-PBE-q1"
    #KIND.Lebedev_grid = 80
    #KIND.Radial_grid  = 200
    KIND = SUBSYS.KIND_add("C")  # Section_parameters can be provided as argument.
    KIND.Basis_set = "DZVP-MOLOPT-SR-GTH"
    KIND.Potential = "GTH-PBE-q4"
    #KIND.Lebedev_grid = 80
    #KIND.Radial_grid  = 200
    KIND = SUBSYS.KIND_add("O")  # Section_parameters can be provided as argument.
    KIND.Basis_set = "DZVP-MOLOPT-SR-GTH"
    KIND.Potential = "GTH-PBE-q6"
    #KIND.Lebedev_grid = 80
    #KIND.Radial_grid  = 200
    KIND = SUBSYS.KIND_add("Cu")  # Section_parameters can be provided as argument.
    KIND.Basis_set = "DZVP-MOLOPT-SR-GTH"
    KIND.Potential = "GTH-PBE-q11"
    #KIND.Lebedev_grid = 80
    #KIND.Radial_grid  = 200
    KIND = SUBSYS.KIND_add("Br")  # Section_parameters can be provided as argument.
    KIND.Basis_set = "DZVP-MOLOPT-SR-GTH"
    KIND.Potential = "GTH-PBE-q7"
    #KIND.Lebedev_grid = 80
    #KIND.Radial_grid  = 200
    KIND = SUBSYS.KIND_add("Cl")  # Section_parameters can be provided as argument.
    KIND.Basis_set = "DZVP-MOLOPT-SR-GTH"
    KIND.Potential = "GTH-PBE-q7"
    #KIND.Lebedev_grid = 80
    #KIND.Radial_grid  = 200

