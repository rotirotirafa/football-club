def to_camel(string: str) -> str:
    string_split = string.split("_")
    return string_split[0] + "".join(word.capitalize() for word in string_split[1:])


def to_snake_case(string: str) -> str:
    return ''.join(['_' + i.lower() if i.isupper() else i for i in string]).lstrip('_')

