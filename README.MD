AI Resume Analyzer 🧑‍💼
The AI Resume Analyzer is a powerful tool built with Python and Streamlit that leverages Google's Gemini API to help job seekers tailor their resumes to specific job descriptions.

This application performs a detailed "gap analysis" by comparing the contents of an uploaded resume against a pasted job description. It then generates a comprehensive report that includes a match score, highlights strengths, identifies skill gaps, and provides actionable suggestions for both resume improvement and new projects to build relevant experience.

Features
📄 File Upload: Supports resume uploads in both PDF (.pdf) and Word (.docx) formats.

🤖 AI-Powered Analysis: Uses the Gemini API to conduct an in-depth comparison between the resume and job description.

📊 Structured Reporting: Generates a clean, easy-to-read report with key sections:

Overall Match Score (%)

Strengths Aligned with the Role

Identified Gaps and Areas for Improvement

Specific Resume Improvement Suggestions

Custom Project Ideas to Fill Skill Gaps

🌐 Web Interface: Simple and intuitive user interface built with Streamlit.

Tech Stack
Backend: Python

AI Model: Google Gemini API

Web Framework: Streamlit

File Handling:

PyMuPDF for PDF extraction

python-docx for Word document extraction

Environment Management: python-dotenv

🚀 Setup and Installation
Follow these steps to get the application running on your local machine.

1. Prerequisites
Python 3.9 or higher

A Google Gemini API Key

2. Clone the Repository
First, clone this repository to your local machine (or simply download the app.py file).

Bash

git clone <your-repository-url>
cd <your-repository-name>
3. Create a Virtual Environment
It is highly recommended to use a virtual environment to manage project dependencies.

Bash

# For Mac/Linux
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
.\venv\Scripts\activate
4. Install Dependencies
Install all the required Python libraries using the following command:

Bash

pip install streamlit google-generativeai python-dotenv PyMuPDF python-docx
5. Configure Environment Variables
You must provide your Gemini API key for the application to work.

Create a file named .env in the root directory of your project.

Add your API key to this file as shown below:

GEMINI_API_KEY="YOUR_API_KEY_HERE"
6. Run the Application
Once the setup is complete, you can run the Streamlit app with this command:

Bash

streamlit run app.py
Your web browser should automatically open to the application's interface.

How to Use
Upload Your Resume: Click the "Browse files" button to upload your resume in .pdf or .docx format.

Paste Job Description: Copy the full text of the job description you are targeting and paste it into the text area.

Analyze: Click the "Analyze My Resume" button and wait for the AI to generate your detailed report.
