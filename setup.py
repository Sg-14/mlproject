from setuptools import find_packages,setup
from typing import List


def get_requirements(file_path:str)->List[str]:
    """
    This function will return a list of requrements
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements

setup(
    name = 'mlproject',
    version = '0.0.1',
    author = 'Shivank',
    author_email='shivank1407@gmail.com',
    packages = find_packages(),
    intsall_requires = get_requirements('requirements.txt')
)