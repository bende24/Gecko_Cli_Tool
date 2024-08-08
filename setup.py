from setuptools import find_packages, setup

from post_install import PostInstallCommand

setup(
    name="gko",
    version="0.1",
    packages=find_packages(),
    install_requires=["Click", "click-aliases"],
    entry_points={
        "console_scripts": ["gko = gko.cli:cli", "gkom = gko.gkom_cli:cli"],
    },
    cmdclass={"install": PostInstallCommand},
)
