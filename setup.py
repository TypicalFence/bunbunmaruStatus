# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try:
    long_description = open("README.rst").read()
except IOError:
    long_description = ""

setup(
    name="bunbunmarustatus",
    version="1.5.1",
    description="A pip package",
    license="GPL3",
    author="Alex Fence",
    packages=find_packages(),
    install_requires=["python-mpd2", "pulsectl", "ini-parser"],
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
    ],
    scripts=["bin/bunbunmarustatus"]
)
