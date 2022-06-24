def capitalize(text):
    if text == '':
        return ''
    first_char = text[0].upper()
    rest_substring = text[1:]
    return f'{first_char}{rest_substring}'

print(capitalize('antonio'))

def get_by_index(elements, index, default):
    return elements[index] if index <= len(elements) else default

print(get_by_index(['zero', 'one'], 1, 'value'))

print(get_by_index(['zero', 'one'], 0, 'value'))