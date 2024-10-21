from setuptools import setup, find_packages

setup(
    name="probabilistic.py",
    version="0.2.0",
    author="R Kataria",
    description="A package for probabilistic function execution.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/r-kataria/probabilistic.py",
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
)
