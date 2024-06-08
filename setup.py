import setuptools
import os
import nltk

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Change to your package's name
package_name = "simple_ats" 

# Get the list of required NLTK data packages
nltk_data_packages = []
with open("nltk.txt", "r") as fp:
    nltk_data_packages = [line.strip() for line in fp]

# Download the NLTK data when package is installed
nltk.download(nltk_data_packages, download_dir=os.path.join(os.path.abspath(os.path.dirname(__file__)), package_name, 'package_data'))


setuptools.setup(
    name=package_name,
    version="3.0.0",
    author="Abin Varghese",
    author_email="abinvarghese90@gmail.com",
    description="A simple package to return a similarity score between a resume and a job description.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Spartan-119/ats_pypi",
    packages=setuptools.find_packages(),
    package_data={package_name: [os.path.join('package_data', '*')]},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
    install_requires=[
        'spacy',
        'sentence-transformers',
        'nltk',
    ],
    entry_points={
        'console_scripts': [
            'simple_ats=simple_ats.ats:main',
        ],
    },
)