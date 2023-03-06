def count_words(string):
    string = string.lower()
    dictOfWords = dict()
    word = ""
    for el in string:
        if el.isalpha():
            word = word + el
        elif word != "":
            if dictOfWords.get(word) == None:
                dictOfWords[word] = 1
            else:
                dictOfWords[word] = dictOfWords[word] + 1
            word = ""

    if word != "":
        if dictOfWords.get(word) == None:
            dictOfWords[word] = 1
        else:
            dictOfWords[word] = dictOfWords[word] + 1

    return dictOfWords

print(count_words("A man, a plan, a canal -- Panama"))
print(count_words("Doo bee doo bee doo"))