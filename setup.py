#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup


DESCRIPTION = (
    "A simple model for keeping notes."
)


def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except:
        return DESCRIPTION


setup(
    name="notes",
    version="0.3.0",
    description=DESCRIPTION,
    long_description=read("README.rst"),
    author="Colin Powell",
    author_email="colin@onecardinal.com",
    license="BSD",
    url="http://github.com/powellc/django-notes/",
    packages=['notes'],
    install_requires=[
        'django>=1.7'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Internet :: WWW/HTTP',
    ],
    zip_safe=False,
)
