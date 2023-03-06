def multiply_numbers(inputs=''):
    res = None
    i = 0
    inputs = str(inputs)
    l = len(inputs)
    while i < l:
        buf = inputs[i]
        i += 1
        if buf.isdigit():
            res = int(buf)
            break
    while i < l:
        buf = inputs[i]
        i += 1
        if buf.isdigit():
            res *= int(buf)
    return res

print(multiply_numbers())
print(multiply_numbers(None))
print(multiply_numbers('ss'))
print(multiply_numbers('1234'))
print(multiply_numbers('sssdd34'))
print(multiply_numbers(2.3))
print(multiply_numbers([5, 6, 4]))