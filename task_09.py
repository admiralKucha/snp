from functools import reduce
def sum(dict):
    res = 0
    for el in dict:
        res += dict[el]
    return res

def connect_dicts(dict1, dict2):
    flag = sum(dict1) > sum(dict2)
    for el in dict2:
        if el in dict1 and flag:
            pass
        else:
            dict1[el] = dict2[el]

    keys = list(dict1.keys())
    for el in keys:
        if dict1[el] < 10:
            dict1.pop(el)

    return  dict(sorted(list(dict1.items()), key=lambda x: x[1], reverse=False))



print(connect_dicts({ "a": 2, "b": 12 }, { "c": 11, "e": 5 }))
print(connect_dicts({ "a": 13, "b": 9, "d": 11 }, { "c": 12, "a": 15 }))
print(connect_dicts({ "a": 14, "b": 12 }, { "c": 11, "a": 15 }))