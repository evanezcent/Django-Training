def transform(values, method):
    arr = []

    for item in values:
        arr.append(method(item))

    return arr