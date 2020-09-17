import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="back-clima-agora-lucas-goss", # Replace with your own username
    version="0.0.1",
    author="Lucas Goss Del Vecchio",
    author_email="delvecchio1001@gmail.com",
    description="Back-end",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ineph/back-clima-agora",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.6',
)