"""file to implement function skeletons and implementations"""

__author__ = "730567639"


def invert(invert_dict: dict[str, str]) -> dict[str, str]:
    new_invert_dict = {}
    count_dict: dict[str, int] = {}
    for key in invert_dict:
        value = invert_dict[key]
        if value in count_dict:
            count_dict[value] += 1
        else:
            count_dict[value] = 1
    for key in count_dict:
        if count_dict[key] >= 2:
            raise KeyError("encountered more than one of the same key")
    for key in invert_dict:
        value = invert_dict[key]
        new_invert_dict[value] = key
    return new_invert_dict


def count(count_list: list[str]) -> dict[str, int]:
    count_dict = {}
    i: int = 0
    while i < len(count_list):
        item = count_list[i]
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
        i += 1
    return count_dict


def favorite_color(colors: dict[str, str]) -> str:
    new_color: list[str] = []
    for i in colors:
        new_color.append(colors[i])
    new_color_dict: dict[str, int] = count(new_color)
    color_count_index: int = 0
    favorite_color: str = ""
    for i in new_color_dict:
        if new_color_dict[i] > color_count_index:
            color_count_index = new_color_dict[i]
            favorite_color = i
    return favorite_color


def bin_len(strings_list: list[str]) -> dict[int, set[str]]:
    bins_dict = {}
    for string in strings_list:
        string_length = len(string)
        if string_length in bins_dict:
            bins_dict[string_length].add(string)
        else:
            bins_dict[string_length] = {string}
    return bins_dict


print(bin_len(["the", "quick", "fox"]))
