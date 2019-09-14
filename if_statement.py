age = int(input("Введите ваш возраст: "))


def occupation(age):
    if age <= 3:
        return "You are just a child, be nice"
    if 3 < age <= 6:
        return "Now you are in a kindergarten"
    if 7 <= age <= 17:
        return "You are in a secondary school"
    if 17 <= age < 21:
        return "dont drink to much, because you are in a university"
    else:
        return "Only work left"


print(f"Your age: {age}")
print(occupation(age))
