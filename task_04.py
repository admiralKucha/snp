def sort_list(list):
    if list == []:
        return list
    listOfIndexes = [[0], [0]]
    min = list[0]
    max = list[0]
    l = len(list)
    for i in range (0, l):
        if list[i] < min:
            min, listOfIndexes[0] = list[i], [i]
        elif list[i] == min:
            listOfIndexes[0].append(i)
        if list[i] > max:
            max, listOfIndexes[1] = list[i], [i]
        elif list[i] == max:
            listOfIndexes[1].append(i)
    if min != max:
        for i in listOfIndexes[0]:
            list[i] = max
        for i in listOfIndexes[1]:
            list[i] = min
    return list + [min]

print( sort_list([]) )
print( sort_list([2, 4, 6, 8]) )
print( sort_list([1]) )
print( sort_list([1, 2, 1, 3]) )
