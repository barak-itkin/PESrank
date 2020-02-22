import setuptools


setuptools.setup(
    name="PESrank",
    version="1.0",
    author="Liron David and Avishai Wool",
    description='Python implementation for "Context Aware Password Guessability via Multi-Dimensional Rank Estimation"',
    url="https://github.com/lirondavid/PESrank",
    packages=setuptools.find_namespace_packages(include=('PESrank.*',)),
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
)