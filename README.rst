================
CP2k tools
================
Description
-----------

This Python package is intended to help running multiple CP2k calculations for the same system or multiple similar systems. In particular, it is used by ``KPFM_simulation_tools`` package to run geometry optimizations for multiple tip-sample distances and bias voltages. The parameters are separated in two Python modules called ``cp2k_common_params`` and ``cp2k_system_params``, the first of which contains computational parameters common to a wide range of calculations and the second contains parameters for a specific system, like the used basis sets. The atomic geometry is expected to be defined as an Atoms object of Atomic Simulation Environment (ASE). pycp2k is used to write the CP2k input file and run the calculation.

Requirements
------------

- Python 3.X (originally 2.7)
- Atomic Simulation Environment (ASE), `https://wiki.fysik.dtu.dk/ase/ <https://wiki.fysik.dtu.dk/ase/>`_
- pycp2k, `https://github.com/SINGROUP/pycp2k <https://github.com/SINGROUP/pycp2k>`_

Installation
------------

Put this directory containing the Python modules to your ``PYTHONPATH`` environment variable. Create file ``cp2k_common_params.py`` based on the file templates in ``parameter_file_templates`` folder and place it to a directory that fits the scope in which you want to use those parameters (for example the root directory of a set of simulations). There are actually 2 sets of parameters the original one - used for NaCl systems - and more recent one called ``style_metallic`` - used for systems of organics on metallic substrates and CO-metallic tips - which has to be renamed to the original form, before usage. Make sure that directory is also in your ``PYTHONPATH``.

Usage
-----

cp2k_init:
^^^^^^^^^^
``cp2k_init`` is the main module containing ``CP2k_init`` class that defines CP2k initializer objects. Import that class to your Python script where you define and run your CP2k calculation. The initializer object is created using command

``cp2k_initializer = CP2k_init(project_name, atoms)``

where ``project_name`` is used in the output files created by the calculation and ``atoms`` is an ASE Atoms object defining the geometry of your model. The initializer object creates a ``CP2K`` object of pycp2k and sets the parameters from ``cp2k_common_params`` and ``cp2k_system_params`` to it, loads the atomic coordinates, cell vectors and boundary conditions based on the given Atoms object and tries to guess a Poisson solver that would work for the given boundary conditions. You should have the ``cp2k_common_params`` in your ``PYTHONPATH`` and ``cp2k_system_params`` files in the directory where you run the calculation (or both in the ``PYTHONPATH`` or in the working directory). See the ``parameter_file_templates`` folder for templates for these files. After that, you should call the correct initialize method based on the type of calculation you want to run. For example,

``cp2k_calc = cp2k_initializer.init_geometry_optimization()``

sets parameters needed for a geometry optimization and returns an object of type ``CP2K`` defined in pycp2k package. There are multiple initialize methods defined in ``cp2k_init`` but you can also define your own if you cannot find a suitable one. To run the actual calculation, use command

``cp2k_calc.run()``

See the documentation of pycp2k for more information. See also ``examples`` folder for a usage examples.

cp2k_grid_size:
^^^^^^^^^^^^^^^
Contains ``get_grid_size`` function that returns the number of grid points along each cell vector in the finest grid used by CP2k. The number of points in the finest grid depends on the cell vectors and the plane wave cutoff, and it must be compatible for the FFT method that CP2k uses. You should use ``use_extended_fft_lengths=False`` unless you have allowed extended FFT lengths in the CP2k input file.

cp2k_output_tools:
^^^^^^^^^^^^^^^^^^
Contains some functions for obtaining data, such as total energy and forces on atoms, from the CP2k output file.

Author
------
Juha Ritala (2016)
`jritala@gmail.com <mailto:jritala@gmail.com>`_

Ondrej Krejci (2022)
`ondrej.krejci@aalto.fi <mailto:ondrej.krejci@aalto.fi>`_
