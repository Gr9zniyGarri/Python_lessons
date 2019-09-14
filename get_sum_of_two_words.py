def get_summ(one, two, delimeter='&'):
    return one.capitalize() + delimeter + two.capitalize()
    
result = get_summ('learn', 'python')

print(result)
