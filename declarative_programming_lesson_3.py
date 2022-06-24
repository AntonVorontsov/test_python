a = [[0, ""], [False, None]]

def non_empty_truths(list_of_lists):
    return [truths for truths in [[elem for elem in one_list if elem] for one_list in list_of_lists] if truths]

non_empty_truths(a)

print(non_empty_truths(a))
