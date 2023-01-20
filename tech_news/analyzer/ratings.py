from collections import Counter
from tech_news.database import find_news
from tech_news.utils.format_data import format_response_to_list_of_tuple
from tech_news.utils.sort_data import sort_list_of_dict


# Requisito 10
def top_5_news():
    news_list = find_news()
    sorted_news = sort_list_of_dict(news_list, "comments_count", "title")

    if len(sorted_news) >= 5:
        top_five_news = [sorted_news[index] for index in range(5)]
        return format_response_to_list_of_tuple(top_five_news)
    return format_response_to_list_of_tuple(sorted_news)


# Requisito 11
def top_5_categories():
    news_list = find_news()
    categories_list = [news["category"] for news in news_list]
    categories_list.sort()
    categories_counted = Counter(categories_list)
    sorted_categories = sorted(
        categories_counted.items(),
        key=lambda x: x[1],
        reverse=True
    )
    response = [categories for categories, _times_found in sorted_categories]

    return response
