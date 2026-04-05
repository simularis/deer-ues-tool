from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="deer-ues-tool",
    version="0.1.0",
    author="Kelsey Yen, Nicholas Fette",
    maintainer="Solaris Technical LLC",
    description="A Python package for expediting unit energy savings calculations from DEER prototypes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/simularis/deer-ues-tool",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "pandas",
    ],
    package_data={
        "deer_ues_tool": [
            "commercial/*.sql",
            "residential/*.sql",
            "lookup/*.csv",
        ],
    },
    include_package_data=True,
)
