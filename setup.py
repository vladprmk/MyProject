from setuptools import setup, find_packages

setup(
    name="MyProject",
    version="0.1.0",
    description="A simple command-line To-Do task manager",
    author="prmkvlad",
    packages=find_packages(),
    install_requires=[
        "pytest>=7.0.0",
        "flake8>=6.0.0",
        "black>=23.0.0",
        "coverage",
        "pytest-cov"
    ],
    python_requires=">=3.6",
)
