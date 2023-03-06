def coincidence(list = [], range = ()):
    return [el for el in list if (type(el) == int or type(el) == float or type(el) == complex)  and (el <= range[-1] and el >= range[0] or el <= range[0] and el >= range[-1])]

print(coincidence([1, 2, 3, 4, 5], range(3, 6)))
print(coincidence())
print(coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4)))
