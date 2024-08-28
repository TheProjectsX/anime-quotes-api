#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open("requirements.txt") as f:
    requirements = [req.strip() for req in f.readlines()]


setup(
    name="Anime Character Quotes API",
    version="1.0.0",
    url="https://github.com/TheProjectsX/anime-quotes-api",
    description="Get Anime Character Quotes Easily!",
    author="TheProjectsX",
    author_email="",
    license="MIT",
    packages=["chatgpt_free", "chatgpt_free.servers"],
    package_dir={"chatgpt_free": "chatgpt_free"},
    install_requires=requirements,
    # Include additional files
    include_package_data=True,
    # Additional classifiers
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
