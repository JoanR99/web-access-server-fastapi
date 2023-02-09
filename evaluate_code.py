from bs4 import BeautifulSoup
import techniques
from test_result import TestResult


def evaluate_html_code(code: str) -> list[TestResult]:
    soup = BeautifulSoup(code, "html.parser")
    results: list[TestResult] = []
    first_results = [
        techniques.t_h_25(soup),
        techniques.t_h_32(soup),
        techniques.t_h_36_37(soup),
        techniques.t_h_44(soup),
        techniques.t_h_57(soup),
        techniques.t_h_63(soup),
        techniques.t_h_64(soup),
        techniques.t_h_93(soup),
        techniques.t_h_95(soup),
        techniques.t_h_96(soup),
    ]
    for result in first_results:
        if result is not None:
            results.append(result)

    return results
