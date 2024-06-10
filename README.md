# Simple Applicant Tracking System (simple_ats)

The Simple Applicant Tracking System (simple_ats) is a Python application designed to parse resumes and job descriptions, extract relevant information, and compute the similarity between them. This system can be useful for recruiters and job seekers to assess the suitability of a candidate for a particular job role.

## You can view the PyPI package and the latest version [here](https://pypi.org/project/simple-ats/).

### Features

- **Resume Parsing**: The system can extract the work experience and skills sections from a resume.
- **Text Cleaning**: The extracted text is cleaned by removing stopwords, punctuation, and performing lemmatization.
- **Job Description Cleaning**: The job description text is also cleaned using the same text cleaning techniques.
- **Similarity Computation**: The system computes the similarity score between the cleaned resume text (experience and skills) and the cleaned job description text using the SentenceTransformer model.

### Installation

To install the simple_ats package, follow these steps:

#### Windows

1. Open the Command Prompt (cmd.exe).
2. Navigate to the directory where you want to install the package using the `cd` command.
3. Run the following command to install the package:

```
pip install simple-ats
```
```
python
```

This will open the Python shell where you can write the Python commands

```
from simple_ats.ats import ATS
resume_content = """<copy-paste your resume text here>"""
jd_content = """<copy-paste the job description text here>"""

ats = ATS()

ats.load_resume(resume_content)
ats.load_job_description(jd_content)

experience = ats.extract_experience()
ats.clean_experience(experience)

skills = " ".join(ats.extract_skills())
ats.clean_skills(skills)

similarity_score = ats.compute_similarity()

print(f"The similarity score between the resume and job description is: {round(similarity_score.item() * 100, 2)}%")
```

#### Linux/macOS

1. Open the Terminal.
2. Navigate to the directory where you want to install the package using the `cd` command.
3. Run the following command to install the package:

```
pip3 install simple-ats
```
```
python
```

This will open the Python shell where you can write the Python commands

```
from simple_ats.ats import ATS
resume_content = """<copy-paste your resume text here>"""
jd_content = """<copy-paste the job description text here>"""

ats = ATS()

ats.load_resume(resume_content)
ats.load_job_description(jd_content)

experience = ats.extract_experience()
ats.clean_experience(experience)

skills = " ".join(ats.extract_skills())
ats.clean_skills(skills)

similarity_score = ats.compute_similarity()

print(f"The similarity score between the resume and job description is: {round(similarity_score.item() * 100, 2)}%")
```

### To run on Jupyter notebook or Google Colab

1. After installing the package, you can use it in your Python script by importing the necessary classes and functions.

```python
!pip install simple-ats
```
```python
from simple_ats import ATS
```

```python
# Load resume and job description content
resume_content = """<copy-paste your resume text here>"""
jd_content = """<copy-paste the job description text here>"""
```

```python
# add the resume content (copy-paste from your resume here)
ats.load_resume(resume_content)
```

```python
# add the job description content (copy-paste from the job description from the job board here)
ats.load_job_description(jd_content)
```

```python
# Create an instance of ATS
ats = ATS()
# Extract and clean experience
experience = ats.extract_experience()
ats.clean_experience(experience)

# Extract and clean skills
skills = " ".join(ats.extract_skills())
ats.clean_skills(skills)

# Compute and print the similarity score
similarity_score = ats.compute_similarity()
print(f"The similarity score between the resume and job description is: {round(similarity_score.item() * 100, 2)}%")
```

### Code Structure

- `TextCleaner` class: Responsible for cleaning text by removing stopwords, punctuation, and performing lemmatization.
- `ATS` class: The main class that handles resume and job description parsing, text cleaning, and similarity computation.
  - `load_resume()`: Loads the resume content from a string.
  - `load_job_description()`: Loads the job description content from a string.
  - `extract_skills()`: Extracts skills from the resume content.
  - `extract_experience()`: Extracts the work experience section from the resume content.
  - `clean_experience()`: Cleans the extracted experience text from the resume.
  - `clean_skills()`: Cleans the extracted skills text from the resume.
  - `clean_jd()`: Cleans the job description text.
  - `compute_similarity()`: Computes the similarity score between the cleaned resume and cleaned job description text using the SentenceTransformer model.

### Dependencies

The following Python libraries are required to run the simple_ats system:

- `re`: For regular expression operations.
- `spacy`: For natural language processing tasks.
- `sentence_transformers`: For computing sentence embeddings and similarity scores.
- `string`: For string operations.
- `nltk`: For natural language processing tasks, such as tokenization, stopword removal, and lemmatization.

These dependencies will be automatically installed when you install the `simple-ats` package.


In this example, the user runs the `simple-ats` package from the command line. The system prompts the user to enter the resume content and job description content. After processing the input, the system computes the similarity score and prints the result to the console.

### Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.