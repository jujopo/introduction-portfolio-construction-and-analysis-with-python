from setuptools import setup, find_packages

setup(
    name='portfolio_pkg',
    version='0.1.0',
    packages=find_packages(),
    description='Tools and scripts for portfolio construction analysis.',
    author='Juan Perez Osorio',
    author_email='juan.perezosorio@stonybrook.edu',
    url='https://github.com/jujopo/introduction-portfolio-construction-and-analysis-with-python',
    install_requires=[
        'numpy',
        'pandas',
        'matplotlib',
        'scipy'
    ],
)