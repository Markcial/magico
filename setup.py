#!/usr/bin/env python
import sys
import subprocess
from os import path
from setuptools import find_packages, setup
from magico import __VERSION__


MIN_PYTHON = (3, 4)
if sys.version_info < MIN_PYTHON:
    sys.exit("Python %s.%s or later is required.\n" % MIN_PYTHON)


setup(
    name='Magico',
    version='0.1',
    description='Bot(ijo) que he creado como regalo para mi querido compadre Pepe',
    author='Mark Garcia Sastre',
    author_email='markcial@gmail.com',
    url='https://github.com/markcial/magico',
    packages=find_packages(),
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Bot Helpers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    install_requires=[
        'requests',
        'python-dotenv',
        'paramiko',
        'slackclient',
        'py-expression-eval'
    ],
    entry_points={
        'console_scripts': [
            'magico=magico.bot:listen'
        ]
    }
)
