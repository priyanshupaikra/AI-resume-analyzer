AI Resume Analyzer 🧑‍💼

A powerful tool built with Python, Streamlit, and the Google Gemini API to help job seekers tailor their resumes for specific job descriptions.
(Note: Replace the image path above with a screenshot of your application)
🚀 Features ✅ File Upload: Supports resume uploads in both PDF (.pdf) and Word (.docx) formats.
🤖 AI-Powered Analysis: Uses the Gemini API to conduct an in-depth comparison between a resume and a job description.
📊 Structured Reporting: Generates a clean, easy-to-read report with key sections like a match score, strengths, skill gaps, and improvement suggestions.
💡 Actionable Feedback: Provides custom project ideas to help users build experience for their target roles.
🌐 Simple Web Interface: Intuitive and easy-to-use UI built with Streamlit.
🛠️ Tech Stack Frontend / UI Backend AI Model File Handling Streamlit Python Google Gemini PyMuPDF, python-docx
Export to Sheets 📁 Project Structure ai-resume-analyzer/ │ ├── app.py # Main Streamlit application file ├── .env # For storing the API Key └── requirements.txt # Project dependencies ⚙️ How to Run Locally Clone the Repository
Bash
git clone https://github.com/yourusername/ai-resume-analyzer.git cd ai-resume-analyzer Create and Activate a Virtual Environment
Bash
For Mac/Linux

python3 -m venv venv source venv/bin/activate
For Windows

python -m venv venv .\venv\Scripts\activate Install Required Packages
Bash
pip install streamlit google-generativeai python-dotenv PyMuPDF python-docx Configure Environment Variables Create a file named .env in the root project folder and add your Google Gemini API key:
GEMINI_API_KEY="YOUR_API_KEY_HERE" Run the Streamlit App
Bash
streamlit run app.py Visit the URL provided in your terminal (usually http://localhost:8501) in your browser 🚀
🧠 Future Improvements [ ] Export the analysis report to PDF format.
[ ] Track analysis history for different job applications.
[ ] Add a feature to analyze a LinkedIn profile URL instead of a resume file.
[ ] Visualize skill matches and gaps with charts and graphs.
