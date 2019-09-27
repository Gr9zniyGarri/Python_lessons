
answers_for_user = {"Как дела": "Хорошо!", "Что делаешь": "Программирую",
                    "Программист или кодерок": "Кодерок"}

def questionnaire():
    while True:
        try:
            user_input = input('How are thing with you? ')
            default_answer = f'This is not what asked about: {user_input}'
            if user_input == 'Хорошо':
                print('\nНу и славно')
                break
            else: 
                print(answers_for_user.get(user_input, default_answer))
        except(KeyboardInterrupt):
            print("\nПока!")
            break

questionnaire()