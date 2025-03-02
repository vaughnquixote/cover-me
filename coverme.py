import argparse
import openai
import os
from pathlib import Path
import PyPDF2

# Set your OpenAI API key (you can also use an environment variable)
openai.api_key = os.getenv("OPENAI_API_KEY")

def extract_text_from_pdf(pdf_path):
    """Extracts text from a PDF file."""
    try:
        with open(pdf_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
        return text
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return ""

def read_file(file_path):
    """Reads text from a file."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return ""

def generate_cover_letter(resume_text, job_description):
    """Generates a cover letter using OpenAI API."""
    if not resume_text or not job_description:
        print("Error: Missing resume or job description text.")
        return ""

    client = openai.OpenAI()

    prompt = (
        f"Write a professional cover letter for the following job description:\n\n"
        f"{job_description}\n\n"
        f"Using this resume as a reference:\n\n"
        f"{resume_text}\n\n"
        f"Make the letter formal, engaging, and tailored to the job."
    )

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

def main():
    parser = argparse.ArgumentParser(description="Generate a cover letter using OpenAI.")
    parser.add_argument("resume", help="Path to the resume file (PDF or TXT).")
    parser.add_argument("job_description", help="Path to the job description text file.")
    parser.add_argument("output", help="Path to save the generated cover letter (TXT).")
    
    args = parser.parse_args()

    # Validate input files
    resume_path = Path(args.resume)
    job_desc_path = Path(args.job_description)

    if not resume_path.exists():
        print(f"Error: Resume file '{args.resume}' does not exist.")
        return

    if not job_desc_path.exists():
        print(f"Error: Job description file '{args.job_description}' does not exist.")
        return

    # Extract resume text
    resume_text = extract_text_from_pdf(resume_path) if resume_path.suffix.lower() == ".pdf" else read_file(resume_path)
    
    if not resume_text:
        print("Error: Unable to extract text from the resume.")
        return

    # Read job description
    job_description = read_file(args.job_description)
    
    # Generate cover letter
    cover_letter = generate_cover_letter(resume_text, job_description)

    if cover_letter:
        with open(args.output, "w", encoding="utf-8") as file:
            file.write(cover_letter)
        print(f"✅ Cover letter saved to {args.output}")
    else:
        print("❌ Error: Failed to generate cover letter.")

if __name__ == "__main__":
    main()
