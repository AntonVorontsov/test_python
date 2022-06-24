l = "abc"

def number_of_unique_letters(string):
    letters = []
    for i in string.lower():
        if i.isalpha() == True:
            letters.append(i)
    return len(set(letters))

print(number_of_unique_letters(l))


# Решение учителя:
#
# def number_of_unique_letters(text):
#     return len({char.lower() for char in text if char.isalpha()})
