#!/usr/bin/env python

from setuptools import setup,Extension

the_scripts = ['scripts/book_combiner', 'scripts/find_book',
               'scripts/isbn_lookup', 'scripts/pickle2json']

setup (name ='drcbooks',
       version = '0.1.0',
       url = 'http://davecoss.com',
       license = 'GPL v3',
       description = 'Book management software',
       author='David Coss',
       author_email='david@davecoss.com',
       packages = ['drcbooks'],
       scripts = the_scripts)

