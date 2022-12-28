import re


def filter(data, value: str) -> list:
    return list(_ for _ in data if value in _)


def unique(data) -> list:
    unique_data = set(data)
    return list(unique_data)


def sort(data, asc) -> list:
    if asc == 'desc':
        return list(data.sort())
    else:
        return list(data.sort(reverse=True))


def limit(data, value: int):
    return data[0:value]


def map(data, value: int) -> list:
    return list(_.split(" ")[int(value)] for _ in data)


def regex(data, value: str) -> list:
    return re.findall(data, value)

