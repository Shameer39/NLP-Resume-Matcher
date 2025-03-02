
import streamlit as st
import google.generativeai as genai
import PyPDF2

# Configure API Key directly
genai.configure(api_key="AIzaSyCz8ckIc6Cm9HodDRSQSQtm0SeZrOx_1LA")

st.header("Profile Analysis & Job Match Score 💯")
st.subheader("Created by Shaik Shameer")
input_text = st.text_area(label="Job Description", key="Input JD")
upload_file = st.file_uploader(label="Upload your Resume", type="pdf")
if upload_file is not None:
    st.write("Choose from below option")

submit1 = st.button(label="Summary of Resume")
submit2 = st.button(label="Job Matching Score")

prompt1 = '''You are an experienced Technical Human Resource Manager, your task is to review the provided resume against the job description. Please share your professional evaluation on whether the candidate's profile aligns with the role. Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.'''

prompt2 = '''You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality, your task is to evaluate the resume against the provided job description. Give me the percentage of match if the resume matches the job description. First the output should come as percentage and then keywords missing and last final thoughts.'''

def input_pdf_setup(upload_file):
    pdf_reader = PyPDF2.PdfReader(upload_file)
    pdf_text = ""
    for page in pdf_reader.pages:
        text = page.extract_text()
        if text:
            pdf_text += text
    return pdf_text

def get_gemini_response(prompt, pdf_text, input_text):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([prompt, pdf_text, input_text])
    return response.text

if submit1:
    if upload_file is not None:
        pdf_text = input_pdf_setup(upload_file)
        response = get_gemini_response(prompt1, pdf_text, input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.warning("Please upload the resume")

elif submit2:
    if upload_file is not None:
        pdf_text = input_pdf_setup(upload_file)
        response = get_gemini_response(prompt2, pdf_text, input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.warning("Please upload the resume")
