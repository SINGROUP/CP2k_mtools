# -*- coding: utf-8 -*-

import numpy as np

angstrom_to_bohr = 1.88972613288564
rydberg_to_au = 0.5
    

# Find number of grid points in each dimension so that the largest plane wave
# energy is at least as large as the cutoff (in Ry) and so that the number of
# points is suitable for FFT
def get_grid_size(cell_vectors, cutoff, use_extended_fft_lengths=False):
    if use_extended_fft_lengths:
        allowed_n = get_extended_fft_lengths_()
    else:
        allowed_n = get_fftsg_lengths_()
    
    cutoff_au = cutoff*rydberg_to_au
    
    n_grid = np.zeros(3, dtype=np.int)
    for dim in range(3):
        cell_vector_len = np.sqrt(cell_vectors[dim, :].dot(cell_vectors[dim, :]))*angstrom_to_bohr
        n_grid[dim] = 2*int(cell_vector_len*np.sqrt(0.5*cutoff_au)/np.pi)+1
        print('points in dim {}: {}'.format(dim, n_grid[dim]))
        for test_n in allowed_n:
            if test_n >= n_grid[dim]:
                n_grid[dim] = test_n
                print('points in dim {} (for FFT): {}'.format(dim, n_grid[dim]))
                break
    
    print('')
    return n_grid


def get_fftsg_lengths_():
    allowed_n = np.array([2, 4, 6, 8, 9, 12, 15, 16, 18, 20, 24, 25, 27, 30, 32, 36,
                40, 45, 48, 54, 60, 64, 72, 75, 80, 81, 90, 96, 100, 108,
                120, 125, 128, 135, 144, 150, 160, 162, 180, 192, 200, 216,
                225, 240, 243, 256, 270, 288, 300, 320, 324, 360, 375, 384,
                400, 405, 432, 450, 480, 486, 500, 512, 540, 576, 600, 625,
                640, 648, 675, 720, 729, 750, 768, 800, 810, 864, 900, 960,
                972, 1000, 1024])
    return allowed_n


def get_extended_fft_lengths_():
    maxn_twos = 13
    maxn_threes = 3
    maxn_fives = 2
    maxn_sevens = 1
    maxn_elevens = 1
    maxn = 10000
    
    allowed_n = []
    for n_twos in range(maxn_twos+1):
        power_of_two = 2**n_twos
        for n_threes in range(maxn_threes+1):
            for n_fives in range(maxn_fives+1):
                for n_sevens in range(maxn_sevens+1):
                    for n_elevens in range(maxn_elevens+1):
                        number = 11**n_elevens * 7**n_sevens * 5**n_fives * 3**n_threes * power_of_two
                        if number <= maxn:
                            allowed_n.append(number)
    
    allowed_n = np.array(allowed_n)
    allowed_n = np.sort(allowed_n)
    return allowed_n
