from tech_news.database import search_news
import re


# Requisito 6
def search_by_title(title):
    query = {"title": re.compile(title, re.IGNORECASE)}
    news_searched = search_news(query)
    response = [(news["title"], news["url"]) for news in news_searched]
    return response


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
