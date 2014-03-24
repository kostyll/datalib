# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

import re
from setuptools import setup
 
version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('datalib/main.py').read(),
    re.M
    ).group(1)
 
setup(
    name = 'datalib',
    packages = ['datalib'],
    entry_points = {
        "console_scripts": ['datalib = datalib.main:main']
        },
    version = version,
    description = "Python datalib.",
    # author = "Andriy Vasyltsiv",
    # author_email = "***",
    # url = None,
    )

__author__ = "Andriy Vasyltsiv"