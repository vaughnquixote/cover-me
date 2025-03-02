import argparse
import openai
import os
from pathlib import Path
import PyPDF2

# Set your OpenAI API key (you can also use an environment variable)
openai.api_key = os.getenv("OPENAI_API_KEY")

def extract_text_from_pdf(pdf_path):
    """Extracts text from a PDF file."""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
    return text

def read_file(file_path):
    """Reads text from a file."""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def generate_cover_letter(client, resume_text, job_description):
    """Uses OpenAI API to generate a cover letter based on the resume and job description."""
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

    # Extract resume text
    resume_path = Path(args.resume)
    if resume_path.suffix.lower() == ".pdf":
        resume_text = extract_text_from_pdf(resume_path)
    elif resume_path.suffix.lower() == ".txt":
        resume_text = read_file(resume_path)
    else:
        print("Unsupported resume format. Use PDF or TXT.")
        return

    # Read job description
    job_description = read_file(args.job_description)
    client = openai.OpenAI()
    # Generate cover letter
    cover_letter = generate_cover_letter(client, resume_text, job_description)

    # Write output
    with open(args.output, "w", encoding="utf-8") as file:
        file.write(cover_letter)

    print(f"Cover letter saved to {args.output}")

if __name__ == "__main__":
    main()
