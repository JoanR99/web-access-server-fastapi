from bs4 import BeautifulSoup
import techniques


def test_h_25():
    html_code = "<html><head></head></html>"
    soup = BeautifulSoup(html_code, "html5lib")
    result = techniques.t_h_25(soup)

    assert result is not None
    assert result.test_name == "H25"
    assert result.element_count == 1
    assert result.error_count == 1

    html_code2 = "<html><head><title></title></head></html>"
    soup2 = BeautifulSoup(html_code2, "html5lib")
    result2 = techniques.t_h_25(soup2)

    assert result2 is not None
    assert result2.test_name == "H25"
    assert result2.element_count == 1
    assert result2.error_count == 1

    html_code3 = "<html><head><title>title</title></head></html>"
    soup3 = BeautifulSoup(html_code3, "html5lib")
    result3 = techniques.t_h_25(soup3)

    assert result3 is None


def test_h_32():
    html_code = "<html><body></body></html>"
    soup = BeautifulSoup(html_code, "html5lib")
    result = techniques.t_h_32(soup)

    assert result is None

    html_code2 = "<html><body><form></form></body></html>"
    soup2 = BeautifulSoup(html_code2, "html5lib")
    result2 = techniques.t_h_32(soup2)

    assert result2 is not None
    assert result2.test_name == "H32"
    assert result2.element_count == 1
    assert result2.error_count == 1

    html_code3 = "<html><body><form><input type='submit' /></form></body></html>"
    soup3 = BeautifulSoup(html_code3, "html5lib")
    result3 = techniques.t_h_32(soup3)

    assert result3 is None

    html_code4 = "<html><body><form><input type='image' /></form></body></html>"
    soup4 = BeautifulSoup(html_code4, "html5lib")
    result4 = techniques.t_h_32(soup4)

    assert result4 is None

    html_code5 = "<html><body><form><button type='submit' /></form></body></html>"
    soup5 = BeautifulSoup(html_code5, "html5lib")
    result5 = techniques.t_h_32(soup5)

    assert result5 is None


def test_h_36_37():
    html_code = "<html><body></body></html>"
    soup = BeautifulSoup(html_code, "html5lib")
    result = techniques.t_h_36_37(soup)

    assert result is None

    html_code2 = "<html><body><img /></body></html>"
    soup2 = BeautifulSoup(html_code2, "html5lib")
    result2 = techniques.t_h_36_37(soup2)

    assert result2 is not None
    assert result2.test_name == "H36_H37"
    assert result2.element_count == 1
    assert result2.error_count == 1

    html_code3 = "<html><body><form><input type='image'/></form></body></html>"
    soup3 = BeautifulSoup(html_code3, "html5lib")
    result3 = techniques.t_h_36_37(soup3)

    assert result3 is not None
    assert result3.test_name == "H36_H37"
    assert result3.element_count == 1
    assert result3.error_count == 1

    html_code4 = "<html><body><img alt='alt'/></body></html>"
    soup4 = BeautifulSoup(html_code4, "html5lib")
    result4 = techniques.t_h_36_37(soup4)

    assert result4 is None

    html_code5 = (
        "<html><body><form><input type='image' alt='alt' /></form></body></html>"
    )
    soup5 = BeautifulSoup(html_code5, "html5lib")
    result5 = techniques.t_h_36_37(soup5)

    assert result5 is None
