# backend/main.py
from fastapi import FastAPI
import os
import uvicorn
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

@app.get('/')
def read_root():
    return {"Hello": "World", "status": "API is running"}

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