from dotenv import load_dotenv
load_dotenv() ##loading all the environment variables

import PyPDF2 as pdf
import os 
import streamlit as st
import google.generativeai as genai
import json


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#Function for load Gemini Pro Model and provide us to information as Response

def get_gemini_response(input):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(input)
    return response.text

## input pdf to text
def input_pdf_text(uploaded_file):
    if uploaded_file is not None and uploaded_file.type == "application/pdf":
        reader = pdf.PdfReader(uploaded_file)
        text = ""
        for page in reader.pages:  # Iterate over pages directly
            text += str(page.extract_text())
        return text
    else:
        return None  # Handle invalid file type or errors

#Prompt Template

input_prompt="""
Hey Act Like a skilled or very experience ATS(Application Tracking System)
with a deep understanding of tech field,software engineering,data science ,data analyst
and big data engineer. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide 
best assistance for improving thr resumes. Assign the percentage Matching based 
on Jd and
the missing keywords with high accuracy
resume:{text}
description:{jd}

I want the response in one single string having the structure
{{"JD Match":"%",\n
"MissingKeywords:[]",\n
"Profile Summary":""}}
"""
        
## streamlit app
st.title("Smart ATS")
st.text("Improve Your Resume ATS")
jd=st.text_area("Paste the Job Description")
uploaded_file=st.file_uploader("Upload Your Resume",type="pdf",help="Please uplaod the pdf")

submit = st.button("Submit")
if submit:
    if uploaded_file is not None:
        text=input_pdf_text(uploaded_file)
        response=get_gemini_response(input_prompt)
        st.subheader(response)