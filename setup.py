import sys
import os.path

from setuptools import find_packages
from setuptools import setup

# TODO: find_packages returns an empty array, what is missing?
print (find_packages())
setup(name="pybyte2ast",
    version='0.1.0-alpha.1',
    packages=['pybyte2ast'],
    scripts=[],
    description="Convert CPython bytecode to an Abstract Syntax Tree (AST)",
    long_description='Convert CPython bytecode to an Abstract Syntax Tree (AST)',
    author="G. Watts (IRIS-HEP)",
    author_email="gwatts@uw.edu",
    maintainer="Gordon Watts (IRIS-HEP)",
    maintainer_email="gwatts@uw.edu",
    url="http://iris-hep.org",
    download_url="http://iris-hep.org",
    license="TBD",
    test_suite="tests",
    install_requires=[],
    setup_requires=["pytest-runner"],
    tests_require=["pytest>=3.9"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development",
        "Topic :: Utilities",
    ],
    platforms="Any",
)
