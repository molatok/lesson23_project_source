def filter(data, value: str):
    return list((_ for _ in data if value in _))


def unique(data):
    unique_data = list(set(data))
    return unique_data


def sort(data, asc):
    if asc == 'desc':
        return data.sort()
    else:
        return data.sort(reverse=True)


def limit(data, value: int):
    return data[0:value]


def map(data, value: int):
    return (_.split(" ")[int(value)] for _ in data)


a = ("мясо", "хлуб", "колбаса", "хлrб")
print(map(a, 2))