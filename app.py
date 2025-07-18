import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import fitz 
from docx import Document

load_dotenv() # loading environment variables from .env file for GEMINI API

try: # configure the Gemini API with your key
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
except AttributeError:
    st.error("GEMINI_API_KEY not found. Please create a .env file with your key.")
    st.stop()
genai_model = genai.GenerativeModel('gemini-1.5-flash')

def get_text_from_file(uploaded_file): # function for the resume uploaded
    """ extracts text content from an uploaded file (.pdf and .docx)"""
    text = ""
    file_extension = os.path.splitext(uploaded_file.name)[1]
    
    uploaded_file.seek(0)
    
    if file_extension == '.pdf':
        try:
            with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
                for page in doc:
                    text += page.get_text()
        except Exception as e:
            st.error(f"Error reading PDF file: {e}")
            return None
    elif file_extension == '.docx':
        try:
            doc = Document(uploaded_file)
            for para in doc.paragraphs:
                text += para.text + "\n"
        except Exception as e:
            st.error(f"Error reading DOCX file: {e}")
            return None
    else:
        st.error(f"Unsupported file type: {file_extension}")
        return None
            
    return text

def get_analysis_report(resume_text, job_description_text):
    """ performs a gap analysis by sending the resume and job description to the Gemini API """
    # detailed prompt for AI model
    prompt = f"""
    - You are an expert career coach and resume analyst with deep expertise in tech and business hiring.
    - Your task is to perform a detailed gap analysis between the provided Resume and the Job Description.
    
    - Analyze both documents and generate a concise, actionable report in Markdown format. The report must include the following sections:

    - Overall Match Score
    Provide a percentage score representing how well the resume matches the job description and a brief one-sentence summary of the match.

    - Strengths Aligned with Role
    In a bulleted list, identify the key skills, experiences, and qualifications from the resume that are a strong match for the requirements in the job description.

    - Gaps and Areas for Improvement
    In a bulleted list, identify the key skills, technologies, or experiences required by the job description that are missing or underrepresented in the resume.

    - Resume Improvement Suggestions
    Provide a bulleted list of specific, actionable suggestions for improving the resume. For each suggestion, mention what to change or add to better reflect the job description's needs. For example: "Rephrase your bullet point on 'Project X' to highlight the use of Python and data analysis, as this is a key requirement."

    - Suggested Projects to Fill Gaps
    Based on the identified gaps, suggest 1-2 concrete project ideas that the candidate could build to gain the missing experience. The projects should be directly related to the job role.

    ---

    RESUME TEXT:
    {resume_text}

    ---

    JOB DESCRIPTION TEXT:
    {job_description_text}
    """
    
    try:
        response = genai_model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"an error occurred while contacting the Gemini API: {e}"


# user interface
st.set_page_config(page_title="AI Resume Analyzer", page_icon="🧑‍💼")
st.title("AI Resume Analyzer 🧑‍💼")
st.info("Upload your resume and paste a job description to get a detailed analysis and improvement suggestions.")

# component for input
resume_file = st.file_uploader("1. Upload Your Resume", type=['pdf', 'docx'], help="Please upload your resume in PDF or DOCX format.")
jd_text = st.text_area("2. Paste the Job Description", height=300, placeholder="Paste the full job description here...")

analyze_button = st.button("Detailed analyze My Resume", type="primary") # analyzer buttom

if analyze_button:    # processing and deisplaying the result
    # inputs validation
    if resume_file is None:
        st.warning("Please upload your resume.")
    elif not jd_text:
        st.warning("Please paste the job description.")
    else:
        # processing spinner
        with st.spinner("Analyzing... This may take a moment."):
            resume_text = get_text_from_file(resume_file)
            
            if resume_text:
                # call the analysis function
                analysis_report = get_analysis_report(resume_text, jd_text)
                
                # display the report
                st.write("---")
                st.header("Analysis Report")
                st.markdown(analysis_report)