"""
Setup script for ailuntz package
"""

from setuptools import setup, find_packages
import os

# Read the long description from README
here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(os.path.dirname(here), "redeme.md")

long_description = ""
if os.path.exists(readme_path):
    with open(readme_path, "r", encoding="utf-8") as f:
        long_description = f.read()

setup(
    name="ailuntz",
    version="1.0.0",
    author="Ailuntz",
    author_email="ailuntz@example.com",
    description="A colorful and elegant personal CV CLI tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://ailuntz.com",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "ailuntz=ailuntz.cli:main",
        ],
    },
    keywords="cli cv resume personal portfolio terminal",
    project_urls={
        "Source": "https://github.com/ailuntz/cli",
        "Bug Reports": "https://github.com/ailuntz/cli/issues",
    },
)
