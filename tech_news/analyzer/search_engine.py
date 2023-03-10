from tech_news.database import search_news
from tech_news.utils.format_data import format_response_to_list_of_tuple
import re
import datetime


# Requisito 6
def search_by_title(title):
    query = {"title": re.compile(title, re.IGNORECASE)}
    news_searched = search_news(query)
    response = format_response_to_list_of_tuple(news_searched)

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
        return format_response_to_list_of_tuple(news_searched)
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    query = {"tags": re.compile(tag, re.IGNORECASE)}
    news_searched = search_news(query)
    response = format_response_to_list_of_tuple(news_searched)

    return response


# Requisito 9
def search_by_category(category):
    query = {"category": re.compile(category, re.IGNORECASE)}
    news_searched = search_news(query)
    response = format_response_to_list_of_tuple(news_searched)

    return response
