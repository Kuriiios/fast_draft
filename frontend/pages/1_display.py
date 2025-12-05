#frontend/pages/0_insert.py
import streamlit as st
import requests
import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

API_ROOT_URL = f"http://{os.getenv('API_BASE_URL')}:{os.getenv('FAST_API_PORT', 8080)}"
API_URL = API_ROOT_URL + "/read/"

st.title('Read all dict')

if st.toggle('Load data'):

    st.info('read from api')

    try:
        response = requests.get(API_URL)

        if response.status_code == 200:
            result = response.json()

            df = pd.DataFrame(result)
            st.dataframe(df, width='stretch')

            st.success(f"Quote sucessfully send !")
            st.balloons()
        else :
            st.error(f"Erreur de l'api with code {response.status_code}")
    except requests.exceptions.ConnectionError:
        st.warning(f'Failed to send to api at url:{API_URL}')