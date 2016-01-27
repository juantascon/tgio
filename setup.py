#! /usr/bin/env python3

import sys
from setuptools import setup

setup(
    name="tgio",
    description="io shell commands over telegram (echo, read, etc)",
    version="0.0.1",
    author="Juan Diego Tascon",
    author_email="juantascon.tgio@horlux.org",
    
    url="https://github.com/juantascon/tgio",
    license="GPL3",
    keywords=["telegram", "io", "shell", "tools", "utils", "echo", "read"],
    scripts=["tgio"],
    data_files=[("share/tgio", ["README.md", "LICENSE", "tgio.cfg.example"])]
)
