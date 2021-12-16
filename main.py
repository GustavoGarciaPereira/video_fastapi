from typing import Optional
from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def main_root():
    return "<h1>gustavo</h1>"