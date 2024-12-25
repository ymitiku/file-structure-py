from setuptools import setup, find_packages

setup(
    name="file-structure-py",
    version="1.0.0",
    description="A Python utility for creating and generating file structures.",
    author="Mitiku Yohannes",
    author_email="se.mitiku.yohannes@gmail.com",
    url="https://github.com/ymitiku/file-structure-py",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "file-structure-py=file_structure_py.main:main",
        ],
    },
)
