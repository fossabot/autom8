import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Autom8",
    version="0.0.1",
    author="David Katz",
    author_email="author@example.com",
    description="A basic framework for Python Busines Process Automation (RPA)",
    long_description=" ",
    long_description_content_type="",
    url="https://github.com/dkatz23238/autom8",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 2.7.14",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Windows",
    ),
)
