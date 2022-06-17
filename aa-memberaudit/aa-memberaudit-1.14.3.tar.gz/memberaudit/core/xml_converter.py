import unicodedata

import bs4

from eveuniverse.core import evexml

from allianceauth.services.hooks import get_extension_logger
from app_utils.logging import LoggerAddTag

from .. import __title__

logger = LoggerAddTag(get_extension_logger(__name__), __title__)

DEFAULT_FONT_SIZE = 13


def eve_xml_to_html(xml_doc: str, add_default_style: bool = False) -> str:
    """Converts Eve Online XML to HTML.

    Args:
    - xml_doc: XML document
    - add_default_style: When set true will add the default style to all unstyled fragments
    """
    xml_doc = unicodedata.normalize("NFKC", xml_doc)
    xml_doc = evexml.remove_loc_tag(xml_doc)
    soup = bs4.BeautifulSoup(xml_doc, "html.parser")
    _convert_font_tag(soup)
    _convert_a_tag(soup)
    if add_default_style:
        _add_default_style(soup)
    return str(soup)


def _convert_font_tag(soup):
    """Convert the font tags into HTML style."""
    for element in soup.find_all("font"):
        element.name = "span"
        styles = []
        if "size" in element.attrs:
            styles.append(f"font-size: {element['size']}px")
            del element["size"]
        if "color" in element.attrs:
            del element["color"]
        if styles:
            element["style"] = "; ".join(styles)


def _convert_a_tag(soup: bs4.BeautifulSoup):
    """Convert links into HTML."""
    for element in soup.find_all("a"):
        new_href = evexml.eve_link_to_url(element["href"])
        if new_href:
            element["href"] = new_href
            element["target"] = "_blank"
        else:
            element["href"] = "#"


def _add_default_style(soup: bs4.BeautifulSoup):
    """Add default style to all unstyled fragments."""
    for el in soup.children:
        if isinstance(el, bs4.NavigableString):
            new_tag = soup.new_tag("span")
            new_tag["style"] = f"font-size: {DEFAULT_FONT_SIZE}px"
            el.wrap(new_tag)
