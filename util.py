def enumerate_names(name: str, data: list):
    if len(data) == 1:
        yield (name, data[0])
    else:
        for index, datum in enumerate(data, start=1):
            yield (f'{name} {index}', datum)
