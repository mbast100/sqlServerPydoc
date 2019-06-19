# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 07:27:19 2019

@author: bastama
"""

from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name = "sqlServerPydoc",
      version = "0.1", 
      description = "A SQL server Utility package"
      ,url = "http://github.com/mbast100/sqlServerPydoc",
      author = "Mark bastawros",
      long_description = long_description,
      author_email = "mbast.amin97@gmail.com",
      license = "MIT",
      packages = ['sqlServerPydoc'],
      zip_safe = False)