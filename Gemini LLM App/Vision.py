from dotenv import load_dotenv
load_dotenv() ##loading all the environment variables

import os 
import streamlit as st
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


#Function  to  load Gemini Pro Model and get Response
model = genai.GenerativeModel("gemini-pro-vision")

def get_gemini_response(input,image):
    if input !="":
        response = model.generate_content([input,image])
    else:
        response = model.generate_content(image)
    return response.text

##initilizing our streamlit app

st.set_page_config(page_title="Gemini Image Demo")
st.header("Gemini Application")
upload_file = st.file_uploader("Choose A Image...", type=["jpg","jpeg","png"])
image = ""
if upload_file is not None:
    image = Image.open(upload_file)
    st.image(image,caption="Uploaded Image is.",use_column_width=True)

input = st.text_input("Input Prompt:",key="input")
submit = st.button("Tell me about this image")

## When Submit Button is clicked

if submit:
    response=get_gemini_response(input,image)
    st.subheader("The Response Is")
    st.write(response)