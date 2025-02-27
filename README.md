# NLP : Resume Matcher

This project uses Streamlit to build an interactive web application that analyzes resumes against job descriptions.
Upon uploading a PDF resume, the app leverages pdf2image to convert the PDF into images, and PIL (Pillow) is used to process the first page of the resume image, saving it as a byte stream. 
The os library helps manage file paths and system operations during this process. 
The image is then encoded into base64 using base64 and passed to Google Generative AI (Gemini) for analysis. 
Two primary functions are provided: a Resume Summary that highlights strengths and weaknesses, and a Job Match Score that calculates a percentage match and identifies missing keywords. 
The results are displayed on the Streamlit interface, offering valuable insights into job fitment.
