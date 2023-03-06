def is_palindrome(string):
    check = '.,:?-<>\'"();! '
    string = str(string).lower()
    i, j = 0, len(string)-1
    while j>i:
        while string[i] in check:
            i += 1
        while string[j] in check:
            j -= 1
        if string[i] != string[j]:
            return False
        i, j = i+1, j-1
    return True

print( is_palindrome("A man, a plan, a canal -- Panama"))
print( is_palindrome("Madam, I'm Adam!"))
print( is_palindrome(333))
print( is_palindrome(None))
print(is_palindrome("Abracadabra"))
print()
