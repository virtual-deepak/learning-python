from io import StringIO

from src.html_pages import HtmlPagesConverter


def test_convert_second_page():
    fake_file = StringIO(
        """page one
PAGE_BREAK
page two
PAGE_BREAK
page three
    """
    )
    html_page_converter = HtmlPagesConverter(fake_file)
    html = html_page_converter.get_html_page(1)
    assert html == "page two<br />"
