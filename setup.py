#!/usr/bin/env python
# -*- coding: utf-8 -*

import os
from glob import glob

from setuptools import find_packages, setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))
VERSION = "0.0.0"
# User README.md as long description
with open("README.md", encoding="utf-8") as f:
    README = f.read()

# https://stackoverflow.com/questions/46784964/create-package-with-cython-so-users-can-install-it-without-having-cython-already
try:
    from Cython.Distutils.extension import Extension
    from Cython.Distutils import build_ext
except ImportError:
    from setuptools import Extension
    USING_CYTHON = False
else:
    USING_CYTHON = True

ext = 'pyx' if USING_CYTHON else 'c'
sources = glob(f'nmf/*.{ext}')
extensions = [
    Extension(source.split('.')[0].replace(os.path.sep, '.'),
              sources=[source],
    )
    for source in sources
]
cmdclass = {'build_ext': build_ext} if USING_CYTHON else {}


setup(
    name="nmf",
    version=VERSION,
    description="NMF with missing values",
    long_description=README,
    long_description_content_type="text/markdown",
    # Credentials
    author="Igor Gotlibovych",
    author_email="igor.gotlibovych@gmail.com",
    url="https://github.com/ig248/nmf-contrib",
    license="BSD",
    # Package
    packages=find_packages(exclude=("tests",)),
    entry_points={"console_scripts": []},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "scikit-learn",
    ],
    classifiers=[
    ],
    ext_modules=extensions,
    cmdclass=cmdclass
)
