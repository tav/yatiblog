#! /usr/bin/env python

# Public Domain (-) 2004-2014 The Yatiblog Authors.
# See the Yatiblog UNLICENSE file for details.

from setuptools import setup

# ------------------------------------------------------------------------------
# Run Setup
# ------------------------------------------------------------------------------

setup(
    name="yatiblog",
    author="tav",
    author_email="tav@espians.com",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: Public Domain",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Documentation",
        "Topic :: Text Processing",
        "Topic :: Utilities"
        ],
    description="Static site generator for blogs and source code documentation",
    entry_points=dict(console_scripts=[
        "yatiblog = yatiblog.main:main"
        ]),
    install_requires=[
        "docutils>=0.7",
        "Genshi>=0.6",
        "Pygments>=1.4",
        "PyYAML>=3.09",
        "simplejson>=2.1.6",
        "tavutil>=1.0"
        ],
    keywords=["blog", "documentation"],
    license="Public Domain",
    long_description=open('README.rst').read(),
    packages=["yatiblog"],
    url="https://github.com/tav/yatiblog",
    version="1.0.2",
    zip_safe=True
    )
