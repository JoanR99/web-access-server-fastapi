from bs4 import BeautifulSoup
import pytest
import techniques


@pytest.mark.parametrize(
    "html_code",
    ["<html><head></head></html>", "<html><head><title></title></head></html>"],
    ids=["Without title", "With title empty"],
)
def test_h_25_failures(html_code: str) -> None:
    soup = BeautifulSoup(html_code, "html5lib")
    result = techniques.t_h_25(soup)

    assert result is not None
    assert result.test_name == "H25"
    assert result.element_count == 1
    assert result.error_count == 1


def test_h_25_success() -> None:
    html_code = "<html><head><title>title</title></head></html>"
    soup = BeautifulSoup(html_code, "html5lib")
    result = techniques.t_h_25(soup)

    assert result is None


@pytest.mark.parametrize(
    "html_code",
    [
        "<html><body></body></html>",
        "<html><body><form><input type='submit' /></form></body></html>",
        "<html><body><form><input type='image' /></form></body></html>",
        "<html><body><form><button type='submit' /></form></body></html>",
    ],
    ids=["Without form", "With submit input", "With image input", "with submit button"],
)
def test_h_32_success(html_code: str) -> None:
    soup = BeautifulSoup(html_code, "html5lib")
    result = techniques.t_h_32(soup)

    assert result is None


def test_h_32_failure() -> None:
    html_code = "<html><body><form></form></body></html>"
    soup = BeautifulSoup(html_code, "html5lib")
    result = techniques.t_h_32(soup)

    assert result is not None
    assert result.test_name == "H32"
    assert result.element_count == 1
    assert result.error_count == 1


@pytest.mark.parametrize(
    "html_code",
    [
        "<html><body></body></html>",
        "<html><body><img alt='alt'/></body></html>",
        "<html><body><form><input type='image' alt='alt' /></form></body></html>",
    ],
    ids=["Without image", "With alt", "With input image alt"],
)
def test_h_36_37_success(html_code: str) -> None:
    soup = BeautifulSoup(html_code, "html5lib")
    result = techniques.t_h_36_37(soup)

    assert result is None


@pytest.mark.parametrize(
    "html_code",
    [
        "<html><body><img /></body></html>",
        "<html><body><form><input type='image'/></form></body></html>",
    ],
    ids=["Without image alt", "With input image alt"],
)
def test_h_36_37_failure(html_code: str) -> None:
    soup = BeautifulSoup(html_code, "html5lib")
    result = techniques.t_h_36_37(soup)

    assert result is not None
    assert result.test_name == "H36_H37"
    assert result.element_count == 1
    assert result.error_count == 1


@pytest.mark.parametrize(
    "html_code",
    [
        "<html><body><form><input type='text' /></form></body></html>",
        "<html><body><form><input type='file'/></form></body></html>",
        "<html><body><form><input type='password'/></form></body></html>",
        "<html><body><form><input type='checkbox'/></form></body></html>",
        "<html><body><form><textarea></textarea></form></body></html>",
        "<html><body><form><select>x</select></form></body></html>",
        "<html><body><form><input type='text' id='x' /></form></body></html>",
        "<html><body><form><input type='file' id='x'/></form></body></html>",
        "<html><body><form><input type='password' id='x'/></form></body></html>",
        "<html><body><form><input type='checkbox' id='x'/></form></body></html>",
        "<html><body><form><textarea id='x'></textarea></form></body></html>",
        "<html><body><form><select id='x'>x</select></form></body></html>",
    ],
    ids=[
        "Text input without id",
        "file input without id",
        "password input without id",
        "checkbox input without id",
        "textarea without id",
        "select without id",
        "Text input without label",
        "file input without label",
        "password input without label",
        "checkbox input without label",
        "textarea without label",
        "select without label",
    ],
)
def test_h_44_failure(html_code: str) -> None:
    soup = BeautifulSoup(html_code, "html5lib")
    result = techniques.t_h_44(soup)

    assert result is not None
    assert result.test_name == "H44"
    assert result.element_count == 1
    assert result.error_count == 1


@pytest.mark.parametrize(
    "html_code",
    [
        "<html><body></body></html>",
        "<html><body><form><label for='x'>x</label><input type='text' id='x' /></form></body></html>",
        "<html><body><form><label for='x'>x</label><input type='file' id='x'/></form></body></html>",
        "<html><body><form><label for='x'>x</label><input type='password' id='x'/></form></body></html>",
        "<html><body><form><label for='x'>x</label><input type='checkbox' id='x'/></form></body></html>",
        "<html><body><form><label for='x'>x</label><textarea id='x'></textarea></form></body></html>",
        "<html><body><form><label for='x'>x</label><select id='x'>x</select></form></body></html>",
    ],
    ids=[
        "Without inputs",
        "Text input with label",
        "file input with label",
        "password input with label",
        "checkbox input with label",
        "textarea with label",
        "select with label",
    ],
)
def test_h_44_success(html_code: str) -> None:
    soup = BeautifulSoup(html_code, "html5lib")
    result = techniques.t_h_44(soup)

    assert result is None
