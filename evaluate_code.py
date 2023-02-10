from bs4 import BeautifulSoup
import techniques
from results_classes import Results, TestResult


def evaluate_html_code(code: str | bytes) -> Results:
    soup = BeautifulSoup(code, "html5lib")
    elements_evaluated_count = 0
    errors_found_count = 0
    results_details = []

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
            results_details.append(
                TestResult(
                    test_name=result.test_name,
                    element_count=result.element_count,
                    error_count=result.error_count,
                )
            )
            elements_evaluated_count += result.element_count
            errors_found_count += result.error_count

    return Results(
        elements_evaluated_count=elements_evaluated_count,
        errors_found_count=errors_found_count,
        results_details=results_details,
    )
