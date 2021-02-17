from setuptools import setup, find_packages
from pip._internal.exceptions import InstallationError


def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]


try:
    install_requires = parse_requirements("requirements.txt")
except InstallationError:
    install_requires = []

try:
    long_description = open("README.md").read()
except IOError:
    long_description = ""

setup(
    name="dep-dl",
    version="0.0.1",
    description="A module that installs dependencies that are requested.",
    license="MIT",
    author="Arjix",
    packages=find_packages(),
    install_requires=install_requires,
    long_description=long_description
)
