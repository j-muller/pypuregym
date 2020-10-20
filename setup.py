from os.path import join, dirname

from setuptools import setup, find_packages


def read(filename):
    with open(join(dirname(__file__), filename)) as fileobj:
        return fileobj.read()


def get_version(package):
    return [
        line for line in read('{}/__init__.py'.format(package)).splitlines()
        if line.startswith('__version__ = ')][0].split("'")[1]


PROJECT_NAME = "pypuregym"
PACKAGE_NAME = "pypuregym"
VERSION = get_version(PACKAGE_NAME)


setup(
    name=PROJECT_NAME,
    version=VERSION,
    description="A library to interact with Pure Fitness/Pure Yoga APIs.",
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    author='Jeffrey Muller',
    author_email='hello@jeffrey.wtf',
    url='https://github.com/j-muller/pypuregym',
    packages=find_packages(exclude=['tests', 'tests.*']),
    extras_require={
        'test': [
            'pytest',
            'pytest-cov',
            'pylint',
            'xenon',
            'pydocstyle',
            'pycodestyle',
            'cobertura-clover-transform',
        ],
        'doc': [
            'sphinx<2', # Sphinx 2 needs Python>=3.5.2
        ],
        'dev': [
            'ipython',
            'pdbpp',
        ],
    },
    install_requires=[
        'requests >=2.23.0,<3.0.0',
        'python-dateutil >=2.8.1,<3.0.0',
        'docopt >=0.6.2,<1.0.0',
        'tabulate >=0.8.7,<1.0.0',
    ],
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    entry_points={
        'console_scripts': [
            'pypuregym = pypuregym.cli.cli:main',
        ],
    }
)
