import os
import markdown 
from flask import Flask, render_template, request
from dotenv import load_dotenv
import google.generativeai as genai
import fitz  
from docx import Document 

app = Flask(__name__)
load_dotenv()

try:
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    genai_model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    print(f"Error configuring Gemini API: {e}")
    genai_model = None

def get_text_from_file(uploaded_file):
    text = ""
    file_extension = os.path.splitext(uploaded_file.filename)[1]
    
    if file_extension == '.pdf':
        with fitz.open(stream=uploaded_file.stream.read(), filetype="pdf") as doc:
            for page in doc:
                text += page.get_text()
    elif file_extension == '.docx':
        doc = Document(uploaded_file.stream)
        for para in doc.paragraphs:
            text += para.text + "\n"
    return text

def get_analysis_report(resume_text, job_description_text):
    if not genai_model:
        return "Error: Gemini API is not configured."

    prompt = f"""
    You are an expert career coach and resume analyst...
    (The rest of the detailed prompt is the same as the Streamlit version)
    ...
    RESUME TEXT: {resume_text}
    JOB DESCRIPTION TEXT: {job_description_text}
    """
    try:
        response = genai_model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"An error occurred while contacting the Gemini API: {e}"

# flask routes
@app.route('/', methods=['GET', 'POST'])
def index():
    report_html = None
    if request.method == 'POST':

        if 'resume_file' not in request.files or not request.form.get('jd_text'):
            return render_template('index.html', report="Error: Please provide both a resume and a job description.")

        resume_file = request.files['resume_file']
        jd_text = request.form['jd_text']

        if resume_file.filename == '':
            return render_template('index.html', report="Error: Please select a resume file to upload.")

        # inputs
        resume_text = get_text_from_file(resume_file)
        if resume_text:
            analysis_report_md = get_analysis_report(resume_text, jd_text)
   
            report_html = markdown.markdown(analysis_report_md)
        else:
            report_html = "<p class='text-danger'>Error: Could not read text from the uploaded file.</p>"

    # GET request or after processing
    return render_template('index.html', report=report_html)

# running the app
if __name__ == '__main__':
    app.run(debug=True)
