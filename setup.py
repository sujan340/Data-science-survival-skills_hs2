from setuptools import setup, find_packages

setup(
    name="math_quiz",  # The name of the package
    version="0.1",  # Initial version number
    packages=find_packages(),  # Automatically find and include all packages
    install_requires=[],  # List dependencies here or leave empty if none are needed
    entry_points={
        "console_scripts": [
            "math_quiz=math_quiz.math_quiz:math_quiz_game",  # Entry point for CLI command
        ],
    },
    author="Natraj Sujan Saya",  #  name
    author_email="sayanatrajsujan@gmail.com",  #  email
    description="A simple command-line math quiz game",  # Brief description of the package
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/sujan340/Data-science-survival-skills_hs2.git",  #  GitHub repository URL
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  
)
