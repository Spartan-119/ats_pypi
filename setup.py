import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="simple_ats",
    version="0.1.0",
    author="Abin Varghese",
    author_email="abinvarghese90@gmail.com",
    description="A simple package for parsing resumes and job descriptions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Spartan-119/ats_pypi",
    packages=setuptools.find_packages(),
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