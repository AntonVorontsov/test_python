def odds_from_odds(list_of_lists):
    n = list(map(odds, odds(list_of_lists)))
    return n

def odds(list):
    new_list = []
    for i, elem in enumerate(list):
        if i % 2 == 0:
            new_list.append(elem)
    return new_list

def keep_odd(some_list):
    del some_list[1::2]

def keep_odds_from_odds(list_of_lists):
    keep_odd(list_of_lists)
    for one_list in list_of_lists:
        keep_odd(one_list)
