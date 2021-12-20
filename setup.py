# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in saiotx_home/__init__.py
from saiotx_home import __version__ as version

setup(
	name='saiotx_home',
	version=version,
	description='Saiotex_home',
	author='MiM',
	author_email='mismail@datavaluenet.net',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
