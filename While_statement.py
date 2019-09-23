
answers_for_user = {"Как дела": "Хорошо!", "Что делаешь": "Программирую",
                    "Программист или кодерок": "Кодерок"}

def questionnaire():
    while True:
        try:
            user_input = input('How are thing with you? ')
            if user_input == 'Хорошо':
                print('Ну и славно')
                break
            elif user_input in answers_for_user:
                print(answers_for_user[user_input])
            else:
                print(f'This is not what asked about: {user_input}')
        except(KeyboardInterrupt):
            print("Пока!")
            break


print(questionnaire())