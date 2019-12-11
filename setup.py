
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="intcode",
    version="1.0.0",
    author="Marco Lussetti",
    author_email="contact@marcolussetti.com",
    description="Packaged library of the intcode computer from Advent of Code 2019",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/marcolussetti/intcode",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
) 
