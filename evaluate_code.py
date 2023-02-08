from bs4 import BeautifulSoup
import techniques
from test_result import TestResult


def evaluate_html_code(code: str) -> list[TestResult]:
    soup = BeautifulSoup(code, "html.parser")
    results: list[TestResult] = []
    first_results = [techniques.t_h_25(soup), techniques.t_h_32(soup)]
    for result in first_results:
        if result is not None:
            results.append(result)

    return results
