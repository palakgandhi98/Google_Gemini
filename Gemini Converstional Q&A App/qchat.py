from dotenv import load_dotenv
load_dotenv() ##loading all the environment variables

import os 
import streamlit as st
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
#Function  to  load Gemini Pro Model and get Response

model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])



def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response

##initilizing our streamlit app

st.set_page_config(page_title="Q & A Demo")
st.header("Gemini LLM Application")

#Initilize session state for the chat history if it doesn't exit
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []
    
input = st.text_input("Input:", key="input")
submit = st.button("Ask Me Question")

## When Submit Button is clicked

if submit and input:
    response=get_gemini_response(input)
    ## add user query and response to session chat history
    st.session_state['chat_history'].append(("You",input))
    st.subheader("The Response Is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot",chunk.text))

st.subheader("The Chat History Is")

for role,text in st.session_state['chat_history']:
    st.write(f"{role}:{text}")
    