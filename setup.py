from setuptools import setup, find_packages

setup(
    name="coverme",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "openai",
        "pypdf2"
    ],
    entry_points={
        "console_scripts": [
            "coverme=coverme.__main__:main",
        ],
    },
    author="Vaughn Franz",
    description="A CLI tool to generate cover letters using OpenAI.",
)
