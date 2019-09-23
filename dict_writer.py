import csv 

jobs_list = [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
    ]

with open ('lesson.csv', 'w', encoding = 'utf-8', newline = '') as f:
    fields = ['name', 'age', 'job']
    writer =csv.DictWriter(f, fields, delimiter = ';')
    for job in jobs_list:
        writer.writerow(job)
