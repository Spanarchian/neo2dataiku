from setuptools import setup, find_packages

setup(
    name='neo2dataiku',
    version='0.0.1',
    description='  A package to utilise neo4j in the Data Science Studio by Dataiku',
    url='https://github.com/Spanarchian/neo2dataiku',
    author='Colin Moore-Hill(Spanarchian)',
    license='MIT',
    packages=find_packages(exclude=('tests')),
)
