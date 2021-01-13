# -*- coding: utf-8 -*-
"""
Created on Wed Dec 10 10:16:15 2014

@author: juha
"""

import re
import numpy as np


def get_output_from_file(filename):
    with open(filename, 'r') as output_file:
        output = output_file.read()
    return output


def get_energy_from_output(output):
    energy = re.findall(r"ENERGY\|.*:\s*([-+]?\d*\.\d+|\d+)", output)
    if len(energy) != 0:
        return float(energy[-1])
    else:
        raise Exception("'ENERGY' entry was not found in the CP2K output file!")


def get_charges_from_output(output):
    output_lines = output.splitlines()
    mulliken_section_begin = -1
    mulliken_section_end = -1
    charges = []
    
    for line_index, line in enumerate(output_lines):
        if "Mulliken Population Analysis" in line:
            mulliken_section_begin = line_index
        elif "# Total charge" in line:
            mulliken_section_end = line_index
    
    if (mulliken_section_begin >= 0) and (mulliken_section_end > mulliken_section_begin):
        charges_begin = mulliken_section_begin + 3
        charges_end = mulliken_section_end
        for line in output_lines[charges_begin:charges_end]:
            splitted_line = line.split()
            charges.append(splitted_line[4])
        return charges
    else:
        raise Exception("'MULLIKEN POPULATION ANALYSIS' entry was not found in the CP2K output file!")


def get_forces_from_output(output):
    output_lines = output.splitlines()
    force_section_begin = -1
    force_section_end = -1
    forces = []
    
    for line_index, line in enumerate(output_lines):
        if "SUM OF ATOMIC FORCES" in line:
            force_section_end = line_index
        elif "ATOMIC FORCES" in line:
            force_section_begin = line_index
    
    if (force_section_begin >= 0) and (force_section_end > force_section_begin):
        forces_begin = force_section_begin + 3
        forces_end = force_section_end
        for line in output_lines[forces_begin:forces_end]:
            splitted_line = line.split()
            forces.append((splitted_line[3], splitted_line[4], splitted_line[5]))
        return np.array(forces)
    else:
        raise Exception("'ATOMIC FORCES' entry was not found in the CP2K output file!")
