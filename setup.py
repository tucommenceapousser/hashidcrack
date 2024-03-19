from setuptools import setup, find_packages

setup(
    name='trknhashcrack',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'questionary',
        'termcolor',
        'colorama'
    ],
    entry_points={
        'console_scripts': [
            'md5=md5:main'
        ]
    }
)