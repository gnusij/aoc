#!/usr/bin/python3
from pathlib import Path
from setuptools import setup

with open(Path(__file__).parent.joinpath('requirements.txt'), 'r') as f:
    required = f.read().splitlines()

setup(name='aoc',
    packages=['aoc'],
    package_dir={'':'src'},
    install_requires=required,
)