from bs4 import BeautifulSoup
import techniques


def test_h_25():
    html_code = "<html><head></head></html>"
    soup = BeautifulSoup(html_code, "html5lib")
    result = techniques.t_h_25(soup)

    if result is not None:
        assert result.test_name == "H25"
        assert result.element_count == 1
        assert result.error_count == 1

    html_code2 = "<html><head><title></title></head></html>"
    soup2 = BeautifulSoup(html_code2, "html5lib")
    result2 = techniques.t_h_25(soup2)

    if result2 is not None:
        assert result2.test_name == "H25"
        assert result2.element_count == 1
        assert result2.error_count == 1

    html_code3 = "<html><head><title>title</title></head></html>"
    soup3 = BeautifulSoup(html_code3, "html5lib")
    result3 = techniques.t_h_25(soup3)

    if result3 is not None:
        assert result3.test_name == "H25"
        assert result3.element_count == 1
        assert result3.error_count == 0
