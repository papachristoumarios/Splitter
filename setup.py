import setuptools
from setuptools import setup, find_packages

setup(
    name='splitter',
    version='1.0',
    description='Splitter',
    author='Alessandro Epasto and Bryan Perozzi. ',
    author_email='',
    url='https://github.com/benedekrozemberczki/Splitter',
    packages=['splitter'],
    package_dir={'splitter': 'splitter'},
    scripts=['splitter/train_splitter.py'])

