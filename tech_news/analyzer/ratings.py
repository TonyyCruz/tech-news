from tech_news.database import find_news
from tech_news.utils.format_output import format_response_to_list_of_tuple


# Requisito 10
def top_5_news():
    news_list = find_news()
    sorted_news = sorted(
        news_list,
        key=lambda i: (i["comments_count"], i["title"]),
        reverse=True
    )

    if len(sorted_news) >= 5:
        top_five_news = [sorted_news[index] for index in range(5)]
        return format_response_to_list_of_tuple(top_five_news)
    return format_response_to_list_of_tuple(sorted_news)


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
