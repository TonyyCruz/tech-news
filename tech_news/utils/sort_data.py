def sort_list_of_dict(dict_list, key_one, key_two=False):
    if key_two:
        return sorted(
            dict_list,
            key=lambda i: (i[key_one], i[key_two]),
            reverse=True
        )

    return sorted(
        dict_list,
        key=lambda i: i[key_one],
        reverse=True
    )
