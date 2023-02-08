from bs4 import BeautifulSoup, Tag
from test_result import TestResult


def t_h_25(html_doc: BeautifulSoup):
    head = html_doc.find("head")

    if not head:
        return TestResult(test_name="H25", element_count=1, error_count=1)

    title = head.find("title")

    if not title or isinstance(title, Tag) and not title.string:
        return TestResult(test_name="H25", element_count=1, error_count=1)
    else:
        return None
