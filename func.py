def filter(data, value: str):
    return list((_ for _ in data if value in _))


def unique(data):
    unique_data = []
    unique_data.append(_ for _ in data if _ not in unique_data)
    return list(unique_data)


def sort(data, asc):
    if asc == 'desc':
        return data.sort()
    else:
        return data.sort(reverse=True)


def limit(data, value: int):
    return data[0:value]


def map(data, value: int):
    return list(_.split(" ")[int(value)] for _ in data)

