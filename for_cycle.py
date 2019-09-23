list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in list_of_numbers:
    print(i + 1)

string = input('Enter some word: ')
for i in string:
    print(i)

classes_in_school = [{'class': '5b', 'scores': [2, 5, 3, 3, 4, 4]},
                     {'class': '7a', 'scores': [3, 4, 5, 5, 5, 4]},
                     {'class': '6a', 'scores': [5, 5, 5, 4, 5, 4]},
                     {'class': '11b', 'scores': [3, 5, 4, 4, 4, 4]},
                     {'class': '9a', 'scores': [5, 5, 2, 2, 3, 4]},
                     {'class': '8b', 'scores': [2, 5, 3, 3, 4, 4]}]

total_score = 0
for score in classes_in_school:
    total_score += (sum(score['scores'])/len(score['scores']))/len(classes_in_school)
    print(sum(score['scores'])/len(score['scores']))

print('Average score for this school is: %.2f' % total_score)
