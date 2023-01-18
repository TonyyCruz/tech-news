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
    selector = Selector(text=html_content)
    next_page_url = selector.css("a.next::attr(href)").get()
    return next_page_url


# Requisito 4
def format_text(text_paragraph):
    selector = Selector(text=text_paragraph)
    paragraph_data = selector.css("p *::text").getall()
    paragraph_text = "".join(paragraph_data).replace("\xa0", "")
    if paragraph_text.endswith(" "):
        return paragraph_text[:-1]
    return paragraph_text


def scrape_news(html_content):
    selector = Selector(text=html_content)

    first_paragraph = selector.css("div.entry-content p").get()
    summary = format_text(first_paragraph)

    response = {
      "url": selector.css("link[rel='canonical']::attr(href)").get(),
      "title": selector.css("h1.entry-title::text").get().replace("\xa0", ""),
      "timestamp": selector.css("li.meta-date::text").get(),
      "writer": selector.css("span.author a::text").get(),
      "comments_count": len(selector.css("ol.comment-list li").getall()),
      "summary": summary,
      "tags": selector.css("section.post-tags li a::text").getall(),
      "category": selector.css("div.entry-details span.label::text").get(),
    }
    # print("RESPONSE ==>>", response)

    return response


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
