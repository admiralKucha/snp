def combine_anagrams(words_array):
    res = []

    dict_word = dict()
    buf = words_array.pop(0)
    word = set(buf)
    res.append([buf])
    for el in words_array:
        dict_word[el] = set(list(el))
        if dict_word[el] == word:
            res[-1].append(el)
            dict_word.pop(el)

    keys = list(dict_word.keys())
    while keys != []:
        el = keys[0]
        word = dict_word[el]
        dict_word.pop(el)
        keys.remove(el)
        res.append([el])
        for el2 in dict_word:
            if dict_word[el2] == word:
                res[-1].append(el2)
                keys.remove(el2)


    return res


print(combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar","creams", "scream"]))