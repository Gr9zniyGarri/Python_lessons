def comparsion(str1: str, str2: str) -> str:
    if not isinstance(str1, str):
        return 0
    elif not isinstance(str2, str):
        return 0
    if str1 == str2:
        return 1
    elif str1 != str2 and str1 > str2:
        return 2
    elif str1 != str2 and str2 == 'learn':
        return 3


print(comparsion(1, 'learn'))
print(comparsion(True, 'learn'))
print(comparsion('кек', 'кек'))
print(comparsion('lear', 'learn'))
print(comparsion('python', 'learn'))
