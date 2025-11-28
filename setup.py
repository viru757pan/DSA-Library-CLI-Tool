from setuptools import setup, find_packages

setup(
    name="dsa-cli",
    version="1.0.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "dsa=dsa_cli.dsa_cli:main",
        ]
    },
)
