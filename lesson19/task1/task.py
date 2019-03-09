# не добавляйте кода вне функции
def update_dictionary(d, key, value):
    assert isinstance(d, dict)
    if d.keys().__contains__(key):
        d.pop(value)
    else:
        if d.keys().__contains__(key * 2):
            d[key * 2] += value
        else:
            d[key * 2] = value

# не добавляйте кода вне функции