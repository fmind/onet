"""Setup file."""

import setuptools


META = dict(
    name="onet",
    version="0.1.0",
    description="Train and predict procedures of DNN for binary image classification.",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/fmind/onet",
    author="Médéric Hurier (fmind)",
    author_email="fmind@fmind.me",
    license="LGPL-3.0",
    packages=["onet"],
    keywords="tensorflow keras image-classification",
    classifiers=["Development Status :: 4 - Beta"],
    entry_points={"console_scripts": ["onet=onet.__main__:main"]},
    python_requires=">=3.7",
    install_requires=[
        "pillow>=7.2.0,<8.0.0",
        "tensorflow>=2.3,<3.0",
    ],
    extras_require={
        'dev': [
            'pytest',
            'twine',
        ]
    }
)

if __name__ == "__main__":
    setuptools.setup(**META)
