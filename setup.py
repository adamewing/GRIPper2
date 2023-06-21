#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='gripper2',
    version='v0.1.0',
    author='Adam Ewing',
    author_email='adam.ewing@gmail.com',
    description=("detect gene retrocopy insertion polymorphisms from short-read paired-end WGS"),
    license='MIT',
    url='https://github.com/adamewing/GRIPper2',
    download_url='https://github.com/adamewing/GRIPper2/archive/refs/tags/v0.1.0.tar.gz',
    scripts=['gripper2'],
    packages=find_packages(),
    install_requires = [
        'pysam',
        'numpy',
        'scikit-bio',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],

)
