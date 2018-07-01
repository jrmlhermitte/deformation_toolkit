#!/usr/bin/env python
import setuptools
from distutils.core import setup, Extension
import versioneer
import os
import sys
import importlib

import numpy as np


setup(
    name='deformation_toolkit',
    author='Julien Lhermitte',
    description="Deformation toolkit",
    packages=setuptools.find_packages(exclude=['doc']),
    include_dirs=[np.get_include()],
    install_requires=['six', 'numpy'],  # essential deps only
    url='http://github.com/jrmlhermitte/deformation_toolkit',
    keywords='Xray Deformation',
    license='BSD',
    classifiers=['Development Status :: 3 - Alpha',
                 "License :: OSI Approved :: BSD License",
                 "Programming Language :: Python :: 3.6",
                 "Programming Language :: Python :: 3.5",
                 "Topic :: Scientific/Engineering :: Physics",
                 "Topic :: Scientific/Engineering :: Chemistry",
                 "Topic :: Software Development :: Libraries",
                 "Intended Audience :: Science/Research",
                 "Intended Audience :: Developers",
                 ],
    )
