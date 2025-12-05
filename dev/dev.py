import pandas as pd
import streamlit as st
import os
from loguru import logger

CSV_FILE_PATH = os.path.join("dev","quotes_db.csv")

def write_db(df:pd.DataFrame):
    df.to_csv(CSV_FILE_PATH, index=True, index_label='id')
    
def read_bd():
    return pd.read_csv(CSV_FILE_PATH, index_col='id')

def initialize_db():
    if os.path.exists(CSV_FILE_PATH):
        logger.info('DB exist')
    else :
        logger.warning(f'DB not found: {CSV_FILE_PATH}')
        df = pd.DataFrame(columns=['id', 'text'])
        df = df.set_index('id')
        write_db(df)
        logger.info('New db created')


initialize_db()