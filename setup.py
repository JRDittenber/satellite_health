from setuptools import setup, find_packages
import os


def read_requirements():
    with open(os.path.join(os.path.dirname(__file__), 'requirements.txt')) as f:
        return [line.strip() for line in f.readlines() if not line.startswith('#')]


setup(
    name='satellite-data-analysis',
    version='0.1.0',
    description='A deployable data science project for satellite data analysis',
    author='J. Dittenber',
    author_email='jeff.dittenber@hotmail.com',
    url='https://github.com/JRDittenber/satellite_health',
    packages=find_packages(),
    install_requires=read_requirements(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
    ],
)
