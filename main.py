# pylint: disable=no-name-in-module
# pylint: disable=no-self-argument

from fastapi import FastAPI
from pydantic import BaseModel
from evaluate_code import evaluate_html_code
from results_classes import Results
import requests


class Code(BaseModel):
    code: str


class URL(BaseModel):
    url: str


app = FastAPI()


@app.post("/api/evaluation/code")
def evaluate_code(code: Code) -> Results:
    results = evaluate_html_code(code.code)
    return results


@app.post("/api/evaluation/url")
def evaluate_url(url: URL) -> Results:
    response = requests.get(url.url, timeout=1)
    results = evaluate_html_code(response.text)
    return results
