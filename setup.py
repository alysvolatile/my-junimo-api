"""Sets up the package"""

#!/usr/bin/env python
    # -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages

with open('README.md') as f:
    README = f.read()

with open('LICENSE.md') as f:
    LICENSE = f.read()

setup(
    name='myJunimoHelper',
    version='1.0.0',
    description='Django Auth back end for myJunimoHelper',
    long_description=README,
    author='<author>',
    author_email='<email>',
    url='https://github.com/WDI-SEA/django-auth-boilerplate',
    license=LICENSE,
    packages=find_packages(exclude=('tests', 'docs'))
)
