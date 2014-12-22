#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="udacity-api",
    version="1.0.0",
    description="Library for interacting with Udacity account data and course progress",
    author="Ty-Lucas Kelley",
    author_email="tylucaskelley@gmail.com",
    license="MIT",
    url="https://github.com/tylucsakelley/udacity-api-python",
    download_url="https://github.com/tylucaskelley/udacity-api-python/tarball/v1.0.0",
    long_description=open("README.md").read(),
    classifiers=[
        "Programming Language :: Python",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        "Topic :: Internet :: WWW/HTTP"
    ],
    packages=[
        "udacity",
        "udacity.user",
        "udacity.catalog"
    ],
    install_requires=[
        "requests >= 2.5.0"
    ],
    keywords=[
        "education",
        "api",
        "udacity",
        "courses",
        "mooc"
    ],
    test_suite="tests"
)
