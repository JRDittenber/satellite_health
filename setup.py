from setuptools import setup, find_packages
from typing import List
import os



HYPHEN_e = '-e .'

def get_requirements(file_path:str)-> List[str]:
    """This function will return the requirements 
    """
    
    requirements = []    
    with open(file_path) as file_obj:
        requirements= file_obj.readlines() 
        requirements = [req.replace("\n",  "") for req in requirements]
        
        if HYPHEN_e in requirements: 
            requirements.remove(HYPHEN_e)
        
        
    return requirements




setup(
    name='satellite-data-analysis',
    version='0.1.0',
    description='A deployable data science project for satellite data analysis',
    author='J. Dittenber',
    author_email='jeff.dittenber@hotmail.com',
    url='https://github.com/JRDittenber/satellite_health',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
    ],
)
