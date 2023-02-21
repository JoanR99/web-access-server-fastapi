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


@pytest.mark.parametrize(
    "html_code",
    ["<html><body></body></html>", "<html lang=''><body></body></html>"],
    ids=["Without lang", "With empty lang"],
)
def test_h_57_failures(html_code: str) -> None:
    soup = BeautifulSoup(html_code, "html5lib")
    result = techniques.t_h_57(soup)

    assert result is not None
    assert result.test_name == "H57"
    assert result.element_count == 1
    assert result.error_count == 1


def test_h_57_success() -> None:
    html_code = "<html lang='en'><body></body></html>"
    soup = BeautifulSoup(html_code, "html5lib")
    result = techniques.t_h_57(soup)

    assert result is None


@pytest.mark.parametrize(
    "html_code",
    [
        "<html><body></body></html>",
        "<html><body><table><tr><th scope='row'></th></tr></table></body></html>",
        "<html><body><table><tr><th scope='col'></th></tr></table></body></html>",
        "<html><body><table><tr><th scope='rowgroup'></th></tr></table></body></html>",
        "<html><body><table><tr><th scope='colgroup'></th></tr></table></body></html>",
    ],
    ids=[
        "Without table",
        "th with scope row",
        "th with scope col",
        "th with scope rowgroup",
        "th with scope colgroup",
    ],
)
def test_h_63_success(html_code: str) -> None:
    soup = BeautifulSoup(html_code, "html5lib")
    result = techniques.t_h_63(soup)

    assert result is None


def test_h_63_failure() -> None:
    html_code = "<table><tr><th></th></tr></table>"
    soup = BeautifulSoup(html_code, "html5lib")
    result = techniques.t_h_63(soup)

    assert result is not None
    assert result.test_name == "H63"
    assert result.element_count == 1
    assert result.error_count == 1


@pytest.mark.parametrize(
    "html_code",
    [
        "<html><body></body></html>",
        "<html><body><iframe title='title' /></body></html>",
    ],
    ids=[
        "Without iframe",
        "iframe with title",
    ],
)
def test_h_64_success(html_code: str) -> None:
    soup = BeautifulSoup(html_code, "html5lib")
    result = techniques.t_h_64(soup)

    assert result is None


@pytest.mark.parametrize(
    "html_code",
    [
        "<html><body><iframe /></body></html>",
        "<html><body><iframe title='' /></body></html>",
    ],
    ids=[
        "iframe without title",
        "iframe with empty title",
    ],
)
def test_h_64_failure(html_code: str) -> None:
    soup = BeautifulSoup(html_code, "html5lib")
    result = techniques.t_h_64(soup)

    assert result is not None
    assert result.test_name == "H64"
    assert result.element_count == 1
    assert result.error_count == 1


@pytest.mark.parametrize(
    "html_code",
    [
        "<html><body></body></html>",
        "<html><body><p id='x'>x</p><p id='y'>y</p></body></html>",
    ],
    ids=[
        "Without ids",
        "Without repeated ids",
    ],
)
def test_h_93_success(html_code: str) -> None:
    soup = BeautifulSoup(html_code, "html5lib")
    result = techniques.t_h_93(soup)

    assert result is None


def test_h_93_failure() -> None:
    html_code = (
        "<html><body><p id='x'>x</p><p id='x'>x</p><p id='y'>y</p></body></html>"
    )
    soup = BeautifulSoup(html_code, "html5lib")
    result = techniques.t_h_93(soup)

    assert result is not None
    assert result.test_name == "H93"
    assert result.element_count == 3
    assert result.error_count == 1


@pytest.mark.parametrize(
    "html_code",
    [
        "<html><body></body></html>",
        "<html><body><video><track kind='captions' /></video></body></html>",
    ],
    ids=[
        "Without video",
        "video with captions",
    ],
)
def test_h_95_success(html_code: str) -> None:
    soup = BeautifulSoup(html_code, "html5lib")
    result = techniques.t_h_95(soup)

    assert result is None


def test_h_95_failure() -> None:
    html_code = "<html><body><video></video></body></html>"
    soup = BeautifulSoup(html_code, "html5lib")
    result = techniques.t_h_95(soup)

    assert result is not None
    assert result.test_name == "H95"
    assert result.element_count == 1
    assert result.error_count == 1


@pytest.mark.parametrize(
    "html_code",
    [
        "<html><body></body></html>",
        "<html><body><video><track kind='descriptions' /></video></body></html>",
    ],
    ids=[
        "Without video",
        "video with descriptions",
    ],
)
def test_h_96_success(html_code: str) -> None:
    soup = BeautifulSoup(html_code, "html5lib")
    result = techniques.t_h_96(soup)

    assert result is None


def test_h_96_failure() -> None:
    html_code = "<html><body><video></video></body></html>"
    soup = BeautifulSoup(html_code, "html5lib")
    result = techniques.t_h_96(soup)

    assert result is not None
    assert result.test_name == "H96"
    assert result.element_count == 1
    assert result.error_count == 1
