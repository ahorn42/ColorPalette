"""
ColorPalette python modules.

Colin Page <cwpage@umich.edu>
"""

from setuptools import setup

setup(
    name='ColorPalette',
    version='0.1.0',
    packages=['ColorPalette'],
    include_package_data=True,
    install_requires=[
        'Pillow==11.0.0',
        'matplotlib==3.9.3',
        'scipy==1.14.1',
        'pandas==2.2.3',
        'click==6.7'
    ],
    entry_points={
        'console_scripts': [
            'colorpalette = ColorPalette.__main__:main',
        ]
    },
)

