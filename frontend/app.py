# frontend/app.py
import streamlit as st
import requests
import os

API_ROOT_URL = f"http://127.0.0.1:{os.getenv('FAST_API_PORT', '8000')}"

st.title("Demonstration API avec FastAPI et Steamlit")
st.subheader("Verification de l'API")

if st.toggle("Ping API (Route /)"):
    try:
        response = requests.get(API_ROOT_URL)
        if response.status_code == 200:
            st.success("Connection sucessfull")
            st.write(response)
            st.code(f'Statut HTTP:{response.status_code}')
            st.json(response.json())
    except requests.exceptions.ConnectionError:
        st.error(f"ERROR: Impossible to connect to the api at {API_ROOT_URL}")
        st.warning("Please make sure the Uvicorn server is running in the background")