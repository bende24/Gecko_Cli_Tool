from setuptools import setup, find_packages

from post_install import PostInstallCommand

setup(
    name='gko',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'gko = gko.cli:cli',
            'gkom = gko.gkom_cli:cli'
        ],
    },
    cmdclass={
        'install': PostInstallCommand
    },
)
