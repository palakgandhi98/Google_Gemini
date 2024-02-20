from dotenv import load_dotenv
load_dotenv() ##loading all the environment variables

import os 
import streamlit as st
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
#Function  to  load Gemini Pro Model and get Response

model = genai.GenerativeModel("gemini-pro")

def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

##initilizing our streamlit app

st.set_page_config(page_title="Q & A Demo")
st.header("Gemini Application")

input = st.text_input("Input:", key="input")
submit = st.button("Ask Me Question")

## When Submit Button is clicked

if submit:
    response=get_gemini_response(input)
    st.subheader("The Response Is")
    st.write(response)