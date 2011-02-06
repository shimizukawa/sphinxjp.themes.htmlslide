# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os, sys

version = '0.0.1'
long_description = \
        open(os.path.join("src","README.txt")).read()

classifiers = [
    "Development Status :: 4 - Beta",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python",
    "Topic :: Software Development",
    "Topic :: Software Development :: Documentation",
    "Topic :: Text Processing :: Markup",
]

setup(
     name='sphinxjp.themes.htmlslide',
     version=version,
     description='A sphinx theme for generate HTML Slide presentation.',
     long_description=long_description,
     classifiers=classifiers,
     keywords=['sphinx', 'reStructuredText', 'presentation'],
     author='Takayuki SHIMIZUKAWA',
     author_email='shimizukawa at gmail dot com',
     url='http://bitbucket.org/shimizukawa/sphinxjp.themes.htmlslide',
     license='MIT',
     packages=find_packages('src'),
     package_dir={'': 'src'},
     package_data = {'': ['buildout.cfg']},
     include_package_data=True,
     install_requires=[
        'setuptools',
        'docutils',
        'sphinx',
        'sphinxjp.themecore',
     ],
     entry_points="""
        [sphinx_themes]
        path = sphinxjp.themes.htmlslide:template_path
     """,
     zip_safe=False,
)

