# pylint: disable=no-name-in-module
# pylint: disable=no-self-argument

from fastapi import FastAPI
from pydantic import BaseModel
from evaluate_code import evaluate_html_code
from test_result import TestResult
import requests


class Code(BaseModel):
    code: str


class URL(BaseModel):
    url: str


app = FastAPI()


@app.post("/evaluation/code")
def evaluate_code(code: Code) -> list[TestResult]:
    results = evaluate_html_code(code.code)
    return results


@app.post("/evaluation/url")
def evaluate_url(url: URL) -> list[TestResult]:
    r = requests.get(url.url)
    results = evaluate_html_code(r.text)
    return results
