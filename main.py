# pylint: disable=no-name-in-module
# pylint: disable=no-self-argument

from fastapi import FastAPI
from pydantic import BaseModel
from evaluate_code import evaluate_html_code
from test_result import TestResult


class Code(BaseModel):
    code: str


app = FastAPI()


@app.post("/evaluation/code")
def evaluate_code(code: Code) -> list[TestResult]:
    results = evaluate_html_code(code.code)
    return results
