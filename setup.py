import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dobby_hardware",
    version="0.0.1",
    author="Zeeshan Khan",
    author_email="zkhan1093@gmail.com",
    description="package for pi harware",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zkhan93/dobby-hardware",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Dependent",
    ],
)
