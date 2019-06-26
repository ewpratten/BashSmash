from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='bashsmash',
    version='1.2',
    packages=['bashsmash'],
    description='A python3 tool for obfuscating bash shell code',
    url='https://github.com/Ewpratten/BashSmash',
    author='Evan Pratten',
    author_email='ewpratten@gmail.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
    ),
    entry_points={
        'console_scripts': [
            'bashsmash = bashsmash.__main__:main'
        ]
    })
