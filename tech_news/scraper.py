import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url, wait=1):
    time.sleep(wait)
    try:
        page_html = requests.get(url, timeout=3)
        if page_html.status_code == 200:
            return page_html.text
        else:
            return None
    except requests.Timeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(text=html_content)
    page_tags = selector.css("a.cs-overlay-link::attr(href)").getall()
    return page_tags


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
