from setuptools import setup, find_packages

setup(
    name="file-structure-py",
    version="1.0.0",
    description="A Python utility for creating and generating file structures.",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "file-structure-py=file_structure_py.main:main",
        ],
    },
)
