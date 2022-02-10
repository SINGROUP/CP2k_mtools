# whatever try:
import numpy as np
'''
# at the moment not used
fix_list = np.loadtxt('fixed_indices.txt')
'''
hartree_per_bohr_to_pN = 82387.2245447

def set_common_params_diagonalize(GLOBAL, FORCE_EVAL, DFT, SCF, VDW):
    FORCE_EVAL.Method = "Quickstep"
    FORCE_EVAL.PRINT.FORCES.Section_parameters = "ON"
    DFT.PRINT.MULLIKEN.Section_parameters = "ON"
    # old stuff bellow
    DFT.MGRID.Ngrids = 4
    DFT.MGRID.Cutoff = 1200
    DFT.MGRID.Rel_cutoff = 60
    DFT.XC.XC_FUNCTIONAL.Section_parameters = "PBE"
    DFT.POISSON.Periodic = "XZ" #beware here, no periodicity in /y/#
    DFT.POISSON.Poisson_solver = "WAVELET" # probably taken care by CP2K_mtoos
    # new - to be HQ partially HQ (ussing GPW instead of GAPW):
    #DFT.QS.Method = "GAPW"
    #DFT.QS.Force_paw = "ON"
    #DFT.QS.Eps_default = 1.0E-14
    #DFT.MGRID.Ngrids = 5
    #DFT.MGRID.Cutoff = 1200
    #DFT.MGRID.Rel_cutoff = 60
    # DFT.XC.XC_GRID.Xc_deriv = "PW"
    # Old stuff bellow
    DFT.QS.Method = "GPW"
    DFT.QS.Eps_default = 1.0E-14
    DFT.QS.Map_consistent = ".TRUE."
    DFT.QS.Extrapolation = "USE_PREV_P"
    DFT.QS.Extrapolation_order = 4
    DFT.KPOINTS.Full_grid = ".TRUE."
    DFT.KPOINTS.Scheme = "MONKHORST-PACK 2 2 1"
    VDW.Potential_type = "PAIR_POTENTIAL"
    vdw1 = VDW.PAIR_POTENTIAL_add()
    vdw1.Type                  = "DFTD3(BJ)"
    vdw1.Calculate_c9_term     = ".TRUE."
    vdw1.Reference_c9_term     = ".TRUE."
    vdw1.Long_range_correction = ".TRUE."
    vdw1.Parameter_file_name   = "dftd3.dat"
    vdw1.Reference_functional  = "PBE"
    SCF.Scf_guess = "RESTART"
    #SCF.Scf_guess = "ATOMIC"
    SCF.Added_mos = 100
    SCF.Eps_scf = 1.0E-7
    SCF.Max_scf = 550
    # new - to be HQ:
    #SCF.OUTER_SCF.Section_parameters = "ON"
    #SCF.OUTER_SCF.Eps_scf = 1.0E-7
    #SCF.OUTER_SCF.Max_scf = 2
    # endy	
    SCF.DIAGONALIZATION.Section_parameters = "ON"
    # new - to be HQ:
    #SCF.MIXING.Section_parameters = "ON"
    #SCF.MIXING.Method = "BROYDEN_MIXING"
    #SCF.MIXING.Alpha = 0.2
    #SCF.MIXING.Nbroyden = 8
    #SCF.MIXING.N_simple_mix = 10
    # Old stuff bellow
    SCF.DIAGONALIZATION.Algorithm = "STANDARD"
    SCF.MIXING.Section_parameters = True
    SCF.MIXING.Method = "BROYDEN_MIXING"
    SCF.MIXING.Alpha    = 0.1
    SCF.MIXING.Beta     = 1.5
    SCF.MIXING.Nbroyden = 8
    SCF.PRINT.RESTART.Add_last = "SYMBOLIC"
    SCF.PRINT.RESTART.Backup_copies = 0

def set_geo_opt_params(MOTION,DFT):
    MOTION.GEO_OPT.Type = "MINIMIZATION"
    MOTION.GEO_OPT.Optimizer = "BFGS"
    MOTION.GEO_OPT.Max_iter = 240
    MOTION.GEO_OPT.Max_force = 0.2/hartree_per_bohr_to_pN
    MOTION.GEO_OPT.Rms_force = 0.05/hartree_per_bohr_to_pN    
    '''
    # at the moment not used
    CONSTRAINT = MOTION.CONSTRAINT
    fix1 = CONSTRAINT.FIXED_ATOMS_add() 
    fix1.Components_to_fix = "XYZ"
    fix1.List = ' '.join(map(str,fix_list))
    '''
    DFT.QS.Extrapolation = "USE_GUESS"
    #DFT.QS.Extrapolation_order = 3

def set_smearing_params(SCF):
    SCF.SMEAR.Section_parameters = "ON"
    SCF.SMEAR.Method = "FERMI_DIRAC"
    SCF.SMEAR.Electronic_temperature = 1.0E+03
