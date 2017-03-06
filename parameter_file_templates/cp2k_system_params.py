# -*- coding: utf-8 -*-

def set_system_specific_params(DFT, SCF, SUBSYS):
    SCF.Added_mos = 100
    
    DFT.Potential_file_name = "GTH_POTENTIALS"
    DFT.Basis_set_file_name = "BASIS_MOLOPT"

    KIND = SUBSYS.KIND_add()
    KIND.Section_parameters = "Cu"
    KIND.Element = "Cu"
    KIND.Basis_set = "DZVP-MOLOPT-SR-GTH"
    KIND.Potential = "GTH-PBE-q11"

    KIND = SUBSYS.KIND_add()
    KIND.Section_parameters = "Na"
    KIND.Element = "Na"
    KIND.Basis_set = "DZVP-MOLOPT-SR-GTH"
    KIND.Potential = "GTH-PBE-q9"

    KIND = SUBSYS.KIND_add()
    KIND.Section_parameters = "Cl"
    KIND.Element = "Cl"
    KIND.Basis_set = "DZVP-MOLOPT-SR-GTH"
    KIND.Potential = "GTH-PBE-q7"
