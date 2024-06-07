# Simple Applicant Tracking System (simple_ats)

The Simple Applicant Tracking System (simple_ats) is a Python application designed to parse resumes and job descriptions, extract relevant information, and compute the similarity between them. This system can be useful for recruiters and job seekers to assess the suitability of a candidate for a particular job role.

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
pip install simple_ats
```

#### Linux/macOS

1. Open the Terminal.
2. Navigate to the directory where you want to install the package using the `cd` command.
3. Run the following command to install the package:

```
pip3 install simple_ats
```

### Usage

1. After installing the package, you can use it in your Python script by importing the necessary classes and functions.

```python
from simple_ats import ATS

# Create an instance of ATS
ats = ATS()

# Load resume and job description content
resume_content = "..."
jd_content = "..."
ats.load_resume(resume_content)
ats.load_job_description(jd_content)

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

2. Alternatively, you can run the `main()` function from the command line:

```
python -m simple_ats
```

This will prompt you to enter the resume content and job description content. The system will process the input, extract relevant information, clean the text, and compute the similarity score, which will be printed to the console.

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

These dependencies will be automatically installed when you install the `simple_ats` package.

### Example

```
$ python -m simple_ats

Please enter the resume content: 
[Resume content goes here]

Please enter the job description content:
[Job description content goes here]

The similarity score between the resume and job description is: 75.23%
```

In this example, the user runs the `simple_ats` package from the command line. The system prompts the user to enter the resume content and job description content. After processing the input, the system computes the similarity score and prints the result to the console.[1]

### Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.