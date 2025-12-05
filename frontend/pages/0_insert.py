#frontend/pages/0_insert.py
import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_ROOT_URL =  f"http://{os.getenv('API_BASE_URL')}:{os.getenv('FAST_API_PORT', '8080')}"
API_URL =  API_ROOT_URL + "/insert"

st.title('Form')

with st.form("insert form"):
    quote = st.text_area("quote text", height=120)
    submitted = st.form_submit_button('Add quote')
    if submitted:
        data = {"text": quote}
        st.info('send to api')

        try:
            response = requests.post(API_URL, json=data)
            if response.status_code == 200:
                print("KINDA WORKING")
                result = response.json()
                st.success(f"Quote sucessfully send !{result['id']}")
                st.balloons()
            else :
                st.error(f"Erreur de l'api with code {response.status_code}")
        except requests.exceptions.ConnectionError:
            st.warning(f'Failed to send {data} to api at url:{API_URL}')