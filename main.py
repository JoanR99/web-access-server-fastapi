# pylint: disable=no-name-in-module
# pylint: disable=no-self-argument

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from evaluate_code import evaluate_html_code
from results_classes import Results
import requests
from fastapi.middleware.cors import CORSMiddleware
import re
from validate_url import regex


class Code(BaseModel):
    code: str


class URL(BaseModel):
    url: str


app = FastAPI()

origins = [
    "https://web-access-client.vercel.app",
    "https://web-access-client-romerojoan1999-gmailcom.vercel.app",
    "https://web-access-client-git-main-romerojoan1999-gmailcom.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/api/evaluation/code")
def evaluate_code(code: Code) -> Results:
    results = evaluate_html_code(code.code)
    return results


@app.post("/api/evaluation/url")
def evaluate_url(page_url: URL) -> Results:
    if not re.match(regex, page_url.url):
        raise HTTPException(status_code=400, detail="invalid url")
    try:
        response = requests.get(page_url.url, timeout=1)
        results = evaluate_html_code(response.text)
        return results
    except requests.exceptions.RequestException:
        raise HTTPException(status_code=500, detail="something went wrong")
