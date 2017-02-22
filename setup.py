#!/usr/bin/env python

from setuptools import setup

__version__ = '0.4.0'

setup(
    name='dorset',
    version=__version__,
    description='Package for implementing Dorset remote agent API',
    long_description=open('README.rst').read(),
    author='Cash Costello',
    author_email='cash.costello@gmail.com',
    url='https://github.com/DorsetProject/dorset-python',
    license='Apache Software License',
    packages=['dorset'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP'
    ],
    install_requires=['enum34;python_version<"3.4"']
)
