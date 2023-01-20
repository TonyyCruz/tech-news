from parsel import Selector


# Recebe uma lista de dict e devolve uma lista de tuplas
def format_response_to_list_of_tuple(dict_list):
    return [(news["title"], news["url"]) for news in dict_list]


def format_paragraph(text_paragraph):
    selector = Selector(text=text_paragraph)
    paragraph_data = selector.css("p *::text").getall()
    paragraph_text = "".join(paragraph_data).replace("\xa0", "")
    if paragraph_text.endswith(" "):
        return paragraph_text[:-1]
    return paragraph_text
