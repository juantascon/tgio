#! /usr/bin/env python3

from setuptools import setup

__version__ = "0.0.2"

setup(
    name="tgio",
    version=__version__,
    description="io shell commands over telegram (echo, read, etc)",
    url="https://github.com/juantascon/tgio",
    author="Juan Diego Tascon",
    author_email="juantascon.tgio@horlux.org",
    license="GPL3",
    keywords=["telegram", "io", "shell", "tools", "utils", "echo", "read", "printf"],
    
    install_requires=[
        'pyxdg',
        'pytelegrambotapi'
    ],
    
    scripts=["tgio"],
    data_files=[("share/tgio", ["README.md", "LICENSE", "tgio.cfg.example"])]
)
