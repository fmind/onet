"""Setup file of the project."""

import setuptools  # type: ignore


META = dict(
    name="onet",
    version="0.1.0",
    description="TODO: Write a description",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/fmind/onet",
    author="Médéric Hurier (fmind)",
    author_email="fmind@fmind.me",
    license="LGPL-3.0",
    packages=["onet"],
    keywords="machine-learning neural-network",
    classifiers=["Development Status :: 4 - Beta"],
    entry_points={"console_scripts": ["onet=onet.__main__:main"]},
    python_requires=">=3.8",
    install_requires=[],
)

if __name__ == "__main__":
    setuptools.setup(**META)
