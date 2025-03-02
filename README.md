# **CoverMe: AI-Powered Cover Letter Generator**  

**CoverMe** is a command-line tool that generates **tailored, professional cover letters** using OpenAI’s GPT model. Simply provide a resume and a job description, and CoverMe will craft a compelling cover letter for you.  

---

## **Installation**  

###  **1. Clone the Repository**  
```sh
git clone https://github.com/yourusername/coverme.git
cd coverme
```

### **2. Install Dependencies**

```
pip install -r requirements.txt
```

### **3. Install CoverMe as a CLI Tool**

```
pip install .
```

## **Usage**  

To generate a cover letter, run:

```
coverme path/to/resume.pdf path/to/job_description.txt path/to/output_cover_letter.txt
```

his will generate a customized cover letter and save it to `output_cover_letter.txt.`

## Setup OpenAI API Key

Set the following environment variable, either in .zshrc, a .env file or in your current session as follows:
```
export OPENAI_API_KEY="your-api-key-here"
```

