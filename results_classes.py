# pylint: disable=no-name-in-module
# pylint: disable=no-self-argument

from pydantic import BaseModel
from typing import List


class TestResultBase:
    def __init__(self, test_name: str, element_count: int, error_count: int):
        self.test_name = test_name
        self.element_count = element_count
        self.error_count = error_count


class TestResult(BaseModel):
    test_name: str
    element_count: int
    error_count: int


class Results(BaseModel):
    elements_evaluated_count: int
    errors_found_count: int
    results_details: List[TestResult]
