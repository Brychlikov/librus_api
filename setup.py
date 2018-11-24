import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="librus_api",
    version="0.1",
    author="Brych",
    author_email="author@example.com",
    description="Wrapper around librus API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Brychlikov/librus_api",
    packages=setuptools.find_packages(),
    install_requires=["requests"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)