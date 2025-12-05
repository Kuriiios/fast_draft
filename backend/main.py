# backend/main.py
from fastapi import FastAPI
import os
import pandas as pd
import uvicorn
from pydantic import BaseModel
from dotenv import load_dotenv
from modules.df_tools import write_db, read_bd, initialize_db
from typing import List

load_dotenv()

class QuoteRequest(BaseModel):
    text : str

class QuoteResponse(BaseModel):
    id : int
    text : str

initialize_db()

app = FastAPI()

@app.get('/')
def read_root():
    return {"Hello": "World", "status": "API is running"}

@app.post('/insert/', response_model=QuoteResponse)
def insert_quotes(quote:QuoteRequest):

    df = read_bd()
    if df.empty:
        new_id = 1
    elif df.index.max() <= 0:
        new_id = 1
    else :
        new_id = 1 + df.index.max()

    new_row = pd.DataFrame({"text":[quote.text]}, index =[new_id])

    df = pd.concat([df, new_row])
    write_db(df)

    return {'id': new_id, 'text':quote.text}

@app.get("/read/", response_model=List[QuoteResponse])
def read_all_quotes():
    df = read_bd()
    return df.reset_index().rename(columns={'id':'id','text':'text'}).to_dict('records')

@app.get('/fr')
def read_root():
    return {'Bonjour': "Monde", "status": "API est ok"}

if __name__ == "__main__":
    try:
        port = os.getenv("FAST_API_PORT")
        port = int(port)
        host = os.getenv("HOST")
    except ValueError:
        print('ERROR')
        port = 8080
        host = '127.0.0.1'

    uvicorn.run("main:app",
                host=host,
                port=port,
                reload=True,
                log_level="debug")