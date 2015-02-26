#!/usr/bin/env python

from setuptools import setup

setup(
    name='commonUtils',
    version='0.0.1',
    description='common Utilities',
    url='https://github.com/XavierVal/commonUtils',
    zip_safe=False,
    classifiers=[
        'Development Status :: 1 - Development',
        'Framework :: Lettuce',
        'Intended Audience :: Developers',
        'Intended Audience :: Quality Assurance',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
        'Programming Language :: Python :: 2.7'
    ],
    install_requires=[
        'requests==1.2.3',
        'nose==1.3.4'
    ],
    py_modules=[
        'commonUtils.time_utils',
        #'commonUtils.parsing_utils'
    ],
    packages=[
        'commonUtils',
        'commonUtils.templates',
    ],
)
