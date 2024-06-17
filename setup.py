import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="patcha",
    version="0.0.1",
    author="Dion Timmer",
    author_email="diontimmer@live.nl",
    description="Simple class to patch module functions.",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    scripts=["patcha.py"],
)
