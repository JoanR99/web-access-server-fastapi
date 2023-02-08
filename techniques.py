from bs4 import BeautifulSoup, Tag
from test_result import TestResult


def filter_submit_option(tag):
    return (tag.name == "button" and tag["type"] == "submit") or (
        tag.name == "input" and (tag["type"] == "submit" or tag["type"] == "image")
    )


def filter_images(tag):
    return (tag.name == "img") or (tag.name == "input" and tag["type"] == "image")


def filter_inputs(tag):
    return (
        (
            tag.name == "input"
            and (
                tag["type"] == "text"
                or tag["type"] == "file"
                or tag["type"] == "password"
                or tag["type"] == "checkbox"
            )
        )
        or tag.name == "select"
        or tag.name == "textarea"
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


def t_h_36_37(html_doc: BeautifulSoup):
    images = html_doc.find_all(filter_images)
    element_count = len(images)
    error_count = 0

    if element_count > 0:
        for image in images:
            if not image.has_attr("alt") or image["alt"].strip() == "":
                error_count = error_count + 1

        if error_count > 0:
            return TestResult(
                test_name="H36_H37",
                element_count=element_count,
                error_count=error_count,
            )

    return None


def t_h_44(html_doc: BeautifulSoup):
    inputs = html_doc.find_all(filter_inputs)
    element_count = len(inputs)
    error_count = 0

    if element_count > 0:
        for input_tag in inputs:
            if not input_tag.has_attr("id") or input_tag["id"].strip() == "":
                error_count = error_count + 1
                continue

            input_id = input_tag["id"]

            if input_id is None or input_id.strip() == "":
                error_count = error_count + 1
                continue

            labels = html_doc.find_all("label")

            if len(labels) == 0:
                error_count = error_count + 1
                continue

            has_match = False

            for label in labels:
                if label.has_attr("for") and label["for"] == input_id:
                    has_match = True
                    break

            if not has_match:
                error_count = error_count + 1

        if error_count > 0:
            return TestResult(
                test_name="H44", element_count=element_count, error_count=error_count
            )

    return None
