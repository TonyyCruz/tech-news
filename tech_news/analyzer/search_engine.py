from tech_news.database import search_news
import re
import datetime


# Recebe uma lista de dict e devolve uma lista de tuplas
def extract_title_and_link(dict_list):
    return [(news["title"], news["url"]) for news in dict_list]


# Requisito 6
def search_by_title(title):
    query = {"title": re.compile(title, re.IGNORECASE)}
    news_searched = search_news(query)
    response = extract_title_and_link(news_searched)

    return response


# Requisito 7
def search_by_date(date):
    print(date)
    try:
        date_formated = (
            datetime
            .datetime
            .strptime(date, "%Y-%m-%d")
            .strftime("%d/%m/%Y")
        )

        query = {"timestamp": date_formated}
        news_searched = search_news(query)
        return extract_title_and_link(news_searched)
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
