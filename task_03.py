def max_odd(array):
    flag = True
    res = None
    for el in array:
        try:
            el = int(el)
        except:
            continue
        if el%2 == 1:
            if flag:
                res = el
                flag = False
            elif res < el:
                res = el
    return res

print( max_odd([1, 2, 3, 4, 4]) )
print( max_odd([21.0, 2, 3, 4, 4]) )
print( max_odd(['ololo', 2, 3, 4, [1, 2], None]) )
print( max_odd(['ololo', 'fufufu']) )
print( max_odd([2, 2, 4]))
