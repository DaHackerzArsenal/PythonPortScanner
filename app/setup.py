from setuptools import setup

setup(
    name='Python Port Scanner',
    version='0.1',
    description='Scan a given range of possible open ports',
    author='victorkolis',
    url='',
    license='MIT',
    packages=['program'],
    entry_points={'console_scripts': ['prog = program.program', ], },
)
