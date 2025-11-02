import http.client
import re
import sys
import urllib.request
from urllib.error import URLError

REGEXP_LINK_PATTERN = r"""<a href=".*?">.*?</a>"""


def get_links_s(html_body: str) -> list[str]:
    return re.findall(REGEXP_LINK_PATTERN, html_body)


def count_links_s(html_body: str) -> int:
    return len(get_links_s(html_body))


def get_html_content(url: str) -> str:
    try:
        response = urllib.request.urlopen(url)
        if isinstance(response, http.client.HTTPResponse):
            return str(response.read())
        raise ValueError("Unknown response type.")
    except ValueError | URLError:
        raise


if len(sys.argv) < 2:
    raise Exception("Nie przekazano żadnych argumentów.")

url = sys.argv[1]

try:
    html_content = get_html_content(url)
    link_count = count_links_s(html_content)

    print(f"Strona zawiera {link_count} linków.")
except:
    print("Nie udało się odczytać zawartości strony.")
