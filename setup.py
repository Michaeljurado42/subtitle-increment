import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "Readme.md").read_text()

# This call to setup() does all the work
setup(
    name="subtitle-increment",
    version="1.0.1",
    description="Increments srt files forwards or backwards in time",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Michaeljurado24/subtitle-increment.git",
    author="Michael Jurado",
    author_email="michaeljurado42@gmail.com",
    license="CC0 1.0 Universal",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["subtitle_increment"],
    include_package_data=True,
    install_requires=[],
)
