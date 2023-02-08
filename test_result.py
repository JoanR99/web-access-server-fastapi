# pylint: disable=no-name-in-module
# pylint: disable=no-self-argument

from pydantic import BaseModel


class TestResult(BaseModel):
    test_name: str
    element_count: int
    error_count: int
