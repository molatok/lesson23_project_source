import re


def filter(data, value: str):
    return list(_ for _ in data if value in _)


def unique(data):
    unique_data = set(data)
    return list(unique_data)


def sort(data, asc):
    if asc == 'desc':
        return list(data.sort())
    else:
        return list(data.sort(reverse=True))


def limit(data, value: int):
    return data[0:value]


def map(data, value: int):
    return list(_.split(" ")[int(value)] for _ in data)


def regex(data, value):
    return list(re.findall(f'{data}', value))


