# -*- coding: utf-8 -*-

hartree_per_bohr_to_pN = 82387.2245447

def set_common_params_ot(GLOBAL, FORCE_EVAL, DFT, SCF):
   GLOBAL.Preferred_diag_library = "ELPA"
   FORCE_EVAL.Method = "Quickstep"
   FORCE_EVAL.PRINT.FORCES.Section_parameters = "MEDIUM"
   DFT.QS.Method = "GPW"
   DFT.QS.Eps_default = 1.0E-14
   DFT.MGRID.Ngrids = 5
   DFT.MGRID.Cutoff = 1600
   DFT.MGRID.Rel_cutoff = 60
   DFT.XC.XC_FUNCTIONAL.Section_parameters = "PBE"
   SCF.Eps_scf = 1.0E-7
   SCF.Max_scf = 29
   SCF.OUTER_SCF.Section_parameters = "ON"
   SCF.OUTER_SCF.Eps_scf = 1.0E-7
   SCF.OUTER_SCF.Max_scf = 10
   SCF.OT.Section_parameters = "ON"
   SCF.OT.Preconditioner = "FULL_SINGLE"
   SCF.OT.Energy_gap = "0.2"
   SCF.OT.Linesearch = "3PNT"
   SCF.PRINT.RESTART.Add_last = "SYMBOLIC"
   SCF.PRINT.RESTART.Backup_copies = 0


def set_common_params_diagonalize(GLOBAL, FORCE_EVAL, DFT, SCF):
   GLOBAL.Preferred_diag_library = "ELPA"
   #GLOBAL.Extended_fft_lengths = "ON"
   #GLOBAL.Fftw_plan_type = "MEASURE"
   #GLOBAL.Fftw_wisdom_file_name = "~/fftw_wisdom/wisdom"
   FORCE_EVAL.Method = "Quickstep"
   FORCE_EVAL.PRINT.FORCES.Section_parameters = "MEDIUM"
   DFT.QS.Method = "GAPW"
   DFT.QS.Force_paw = "ON"
   DFT.QS.Eps_default = 1.0E-14
   DFT.MGRID.Ngrids = 5
   DFT.MGRID.Cutoff = 1200
   DFT.MGRID.Rel_cutoff = 60
   DFT.XC.XC_FUNCTIONAL.Section_parameters = "PBE"
   #DFT.XC.XC_GRID.Xc_smooth_rho = "NN50"
   DFT.XC.XC_GRID.Xc_deriv = "PW"
   SCF.Eps_scf = 1.0E-7
   SCF.Max_scf = 100
   SCF.OUTER_SCF.Section_parameters = "ON"
   SCF.OUTER_SCF.Eps_scf = 1.0E-7
   SCF.OUTER_SCF.Max_scf = 2
   SCF.MIXING.Section_parameters = "ON"
   SCF.MIXING.Method = "BROYDEN_MIXING"
   SCF.MIXING.Alpha = 0.2
   SCF.MIXING.Nbroyden = 8
   SCF.MIXING.N_simple_mix = 10
   SCF.PRINT.RESTART.Add_last = "SYMBOLIC"
   SCF.PRINT.RESTART.Backup_copies = 0


def set_geo_opt_params(MOTION, DFT):
    MOTION.GEO_OPT.Type = "MINIMIZATION"
    MOTION.GEO_OPT.Max_iter = 40
    MOTION.GEO_OPT.Max_force = 0.2/hartree_per_bohr_to_pN
    MOTION.GEO_OPT.Rms_force = 0.05/hartree_per_bohr_to_pN
    DFT.QS.Extrapolation = "PS"
    DFT.QS.Extrapolation_order = 3


def set_smearing_params(SCF):
   SCF.SMEAR.Section_parameters = "ON"
   SCF.SMEAR.Method = "FERMI_DIRAC"
   SCF.SMEAR.Electronic_temperature = 300
