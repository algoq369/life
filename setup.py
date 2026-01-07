"""
Life: Conceptual Intelligence System

Building genuine intelligence through concepts, relationships,
and human-like reasoning—not neural networks or gradient descent.
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README for long description
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="life-intelligence",
    version="0.1.0",
    author="Algoq",
    author_email="",
    description="Conceptual intelligence system with metacognition and ideological reasoning",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/algoq369/life",
    project_urls={
        "Bug Tracker": "https://github.com/algoq369/life/issues",
        "Documentation": "https://github.com/algoq369/life",
        "Source Code": "https://github.com/algoq369/life",
    },
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    install_requires=[
        "networkx>=3.0",
        "matplotlib>=3.5.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-cov>=3.0",
            "black>=22.0",
            "flake8>=4.0",
            "mypy>=0.950",
        ],
    },
    entry_points={
        "console_scripts": [
            "life-demo=life.examples.demo:main",
        ],
    },
)
