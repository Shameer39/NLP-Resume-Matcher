import streamlit as st #Streamlit
import google.generativeai as genai # genai
import os
import base64
from PIL import Image
import pdf2image
import io

# Setup the key form Api
genai.configure(api_key="Paste_your_api_key_here")

# Design the Front End
st.header("Profile Analysis & Job Match Score 💯")
st.subheader("created by Faraz Siddiqui")
input_text = st.text_area(label="Job Description", key = "Input JD")
upload_file = st.file_uploader(label = "Upload your Resume",
                               type = "pdf")
if upload_file is not None:
               st.write("Choose from below option")
               
# Buttons
submit1 = st.button(label = "Summary of Resume")
submit2 = st.button(label = "Job Matching Score")

# Prompts:
prompt1 = '''You are an experienced Technical Human Resource Manager,your task is to review the provided resume against the job description. Please share your professional evaluation on whether the candidate's profile aligns with the role. Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
'''
prompt2 = '''You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality, your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches the job description. First the output should come as percentage and then keywords missing and last final thoughts.
'''
# Gen Ai Model....
def get_gemini_response(input, pdf_content, prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([input, pdf_content[0], prompt])
    return response.text

# PDF File
def input_pdf_setup(upload_file):
    if upload_file is not None:
        # Convert pdf into Image
        images = pdf2image.convert_from_bytes(upload_file.read()) 
        
        first_page = images[0]
        # Convert them into Bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()
        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Lets put soul into the buttons
if submit1:
    if upload_file is not None:
        pdf_content=input_pdf_setup(upload_file)
        response=get_gemini_response(prompt1,pdf_content,
                                     input_text)
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please upload the resume")

elif submit2:
    if upload_file is not None:
        pdf_content=input_pdf_setup(upload_file)
        response=get_gemini_response(prompt2,pdf_content,input_text)
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please upload the resume")