import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="datetime_functions",
    version="0.0.3",
    author="Bee Group",
    description="Simple functions to treat datetimes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages()
)