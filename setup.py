from setuptools import find_packages, setup

with open("app/README.md", "r") as f:
    long_description = f.read()

setup(
    name="NeoCrypto",
    version="0.0.1-alpha",
    description="post quantum asymetric cryptography package",
    package_dir={"": "app"},
    packages=find_packages(where="app"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/neomn/NeoCrypto",
    author="Neo",
    author_email="neomn110@gmail.com",
    license="GLP-3.0",
    classifiers=[
        "License :: OSI Approved :: GLP License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    install_requires=[""],
    extras_require={
        "dev": ["pytest>=7.0", "twine>=4.0.2"],
    },
    python_requires=">=3.10",
)
