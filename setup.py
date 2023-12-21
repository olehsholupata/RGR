# setup.py
from setuptools import setup, find_packages

setup(
    name='music_analysis',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'matplotlib',
        'seaborn',
        # add any other dependencies
    ],
    test_suite='tests',
)

