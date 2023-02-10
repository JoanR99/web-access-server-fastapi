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
    r = requests.get(url.url)
    results = evaluate_html_code(r.text)
    return results
