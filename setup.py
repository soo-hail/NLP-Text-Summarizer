# The purpose of "setup.py" is to make our project a Python-Module, that others can easily install and use it with commands  like "pip install ______".
from setuptools import setup
from setuptools import find_packages
from typing import List

# Add Description to the Model published in PyPi.
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

def get_requirements()->List[str]:
    # Returns List of requirements.
    HYPHON_E_DOT = '-e .'
    
    requirements = []
    with open('requirements.txt') as f:
        requirements = f.readlines()
        
        # Remove whitespace and newline characters
        requirements = [row.replace('\n', '').strip() for row in requirements]
        
        # Remove '-e .' and any empty strings
        requirements = [req for req in requirements if req and req != HYPHON_E_DOT]
            
    return requirements

# Define Meta-data, Dependencies.
setup(
    name = 'NLP-Text-summarizer',
    version = '0.0.0',
    author = 'Mohammed Sohail',
    author_email = 'mohammed01705@gmail.com',
    description = 'A Python Module for Text Summarization',
    long_description = long_description,
    url = 'https://github.com/soo-hail/NLP-Text-Summarizer.git',
    package_dir = {'': 'src'}, # Tells where Python should look for our packages. There we are telling instead of looking at root-dir(''), look inside src for packages. 
    packages = find_packages(), # packages: Tells which packages to include in project, find_packages(): include all the folders that has '__init__.py' 
    install_requires = get_requirements()
)
 