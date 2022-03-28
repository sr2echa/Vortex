from setuptools import setup, find_packages

def requirements():
    with open('requirements.txt') as f:
        return f.read().splitlines()

setup(
    name="vortex",
    description="A Python CLI Starter Template",
    version="0.1",
    author="Sreecharan S. <sreecharansiva@gmail.com>",
    packages=find_packages(),
    install_requires=requirements(),
    entry_points={
        "console_scripts": [
            "vortex = vortex.cli:cli"
        ]
    },
)