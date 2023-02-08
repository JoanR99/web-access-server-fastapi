from bs4 import BeautifulSoup, Tag
from test_result import TestResult


def filter_submit_option(tag):
    return (tag.name == "button" and tag["type"] == "submit") or (
        tag.name == "input" and (tag["type"] == "submit" or tag["type"] == "image")
    )


def t_h_25(html_doc: BeautifulSoup):
    head = html_doc.find("head")

    if not head:
        return TestResult(test_name="H25", element_count=1, error_count=1)

    title = head.find("title")

    if not title or isinstance(title, Tag) and not title.string:
        return TestResult(test_name="H25", element_count=1, error_count=1)
    else:
        return None


def t_h_32(html_doc: BeautifulSoup):
    forms = html_doc.find_all("form")
    element_count = len(forms)
    error_count = 0

    if element_count > 0:
        for form in forms:
            valid_form = form.find_all(filter_submit_option)

            if len(valid_form) == 0:
                error_count = error_count + 1

        if error_count > 0:
            return TestResult(
                test_name="H32", element_count=element_count, error_count=error_count
            )

        return None
