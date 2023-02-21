from bs4 import BeautifulSoup, Tag
from results_classes import TestResultBase


def filter_submit_option(tag):
    return (
        tag.name == "button" and tag.has_attr("type") and tag["type"] == "submit"
    ) or (
        tag.name == "input"
        and tag.has_attr("type")
        and (tag["type"] == "submit" or tag["type"] == "image")
    )


def filter_images(tag):
    return (tag.name == "img") or (
        tag.name == "input" and tag.has_attr("type") and tag["type"] == "image"
    )


def filter_inputs(tag):
    return (
        (
            tag.name == "input"
            and tag.has_attr("type")
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


def filter_has_id(tag):
    return tag.has_attr("id")


def filter_tracks_with_captions(tag):
    return (
        tag.name == "track"
        and tag.has_attr("kind")
        and tag["kind"].strip() == "captions"
    )


def filter_tracks_with_descriptions(tag):
    return (
        tag.name == "track"
        and tag.has_attr("kind")
        and tag["kind"].strip() == "descriptions"
    )


def t_h_25(html_doc: BeautifulSoup):
    head = html_doc.find("head")

    if not head:
        return TestResultBase(test_name="H25", element_count=1, error_count=1)

    title = head.find("title")

    if not title or isinstance(title, Tag) and not title.string:
        return TestResultBase(test_name="H25", element_count=1, error_count=1)
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
            return TestResultBase(
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
            return TestResultBase(
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

            labels = html_doc.find_all("label")

            if len(labels) == 0:
                error_count = error_count + 1
                continue

            has_match = False

            for label in labels:
                if label.has_attr("for") and label["for"] == input_tag["id"]:
                    has_match = True
                    break

            if not has_match:
                error_count = error_count + 1

        if error_count > 0:
            return TestResultBase(
                test_name="H44", element_count=element_count, error_count=error_count
            )

    return None


def t_h_57(html_doc: BeautifulSoup):
    html = html_doc.find("html")

    if isinstance(html, Tag) and (
        not html.has_attr("lang") or html.attrs["lang"].strip() == ""
    ):
        return TestResultBase(test_name="H57", element_count=1, error_count=1)

    return None


def t_h_63(html_doc: BeautifulSoup):
    ths = html_doc.find_all("th")
    element_count = len(ths)
    error_count = 0

    if element_count > 0:
        for th in ths:
            if not th.has_attr("scope") or th["scope"].strip() not in [
                "row",
                "col",
                "rowgroup",
                "colgroup",
            ]:
                error_count = error_count + 1

        if error_count > 0:
            return TestResultBase(
                test_name="H63", element_count=element_count, error_count=error_count
            )

    return None


def t_h_64(html_doc: BeautifulSoup):
    iframes = html_doc.find_all("iframe")
    element_count = len(iframes)
    error_count = 0

    if element_count > 0:
        for iframe in iframes:
            if not iframe.has_attr("title") or iframe["title"].strip() == "":
                error_count = error_count + 1

        if error_count > 0:
            return TestResultBase(
                test_name="H64", element_count=element_count, error_count=error_count
            )

    return None


def t_h_93(html_doc: BeautifulSoup):
    tags_with_id = html_doc.find_all(filter_has_id)
    element_count = len(tags_with_id)
    error_count = 0

    if element_count > 0:
        ids = set()
        for tag in tags_with_id:
            ids.add(tag["id"])

        error_count = element_count - len(ids)

        if error_count > 0:
            return TestResultBase(
                test_name="H93", element_count=element_count, error_count=error_count
            )

    return None


def t_h_95(html_doc: BeautifulSoup):
    videos = html_doc.find_all("video")
    element_count = len(videos)
    error_count = 0

    if element_count > 0:
        tracks_with_captions = html_doc.find_all(filter_tracks_with_captions)

        error_count = element_count - len(tracks_with_captions)

        if error_count > 0:
            return TestResultBase(
                test_name="H95", element_count=element_count, error_count=error_count
            )

    return None


def t_h_96(html_doc: BeautifulSoup):
    videos = html_doc.find_all("video")
    element_count = len(videos)
    error_count = 0

    if element_count > 0:
        tracks_with_descriptions = html_doc.find_all(filter_tracks_with_descriptions)

        error_count = element_count - len(tracks_with_descriptions)

        if error_count > 0:
            return TestResultBase(
                test_name="H96", element_count=element_count, error_count=error_count
            )

    return None
