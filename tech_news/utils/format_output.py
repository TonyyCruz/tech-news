# Recebe uma lista de dict e devolve uma lista de tuplas
def format_response_to_list_of_tuple(dict_list):
    return [(news["title"], news["url"]) for news in dict_list]
