# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='wonderguard',
    version='0.1',
    description='Competitive pokemon analysis tool',
    long_description=readme,
    author='Martin Quesada Zaragoza',
    author_email='devilukelele@gmain.com',
    url='https://github.com/martnquesada/wonderguard',
    license=license,
    packages=find_packages(exclude=('tests'))
)

