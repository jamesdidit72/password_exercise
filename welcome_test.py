def strength_checker():
    print('strength checker')
    pass
output_strength = strength_checker()

# def password_generator():
#     print('password generator')
#     pass
#
#
# def exit_function():
#     print('Exiting...')
#     exit()
#     pass
#
#
# def welcome():
#     word_exit = 'exit'
#     print('Welcome to the Password Hub')
#     try:
#         first_name = str(input('Please enter your first name: '))
#         last_name = str(input('Please enter your last name: '))
#     except TypeError as error_message:
#         print('Sorry, please enter a string: ' + str(error_message))
#     date_of_birth = input('Please enter your date of birth as DD/MM/YYYY: ')  # look this up
#     personal_details = [first_name, last_name, date_of_birth]
#     running = True
#     print(f'Hello {first_name}, enter the corresponding value for what you would like todo:')
#     while running:
#         user_action = input('Check password strength (1), generate a password (2) or type "exit" to exit.')
#         if user_action == '1':
#             return stength_checker()
#         elif user_action == '2':
#             return password_generator()
#         elif word_exit in user_action.lower():
#             return exit_function()
#         else:
#             print('Invalid input, try again')
#             continue
#     pass

def password_generator():
    print('password generator')
    pass


def exit_function():
    print('Exiting...')
    exit()
    pass


def welcome():
    print('Welcome to the Password Hub')

    first_name = str(input('Please enter your first name: '))
    last_name = input('Please enter your last name: ')

    date_of_birth = input('Please enter your date of birth as DD/MM/YYYY: ')  # look this up
    personal_details = [first_name, last_name, date_of_birth]


def menu(first_name):
    word_exit = 'exit'
    running = True
    print(f'Hello {first_name}, enter the corresponding value for what you would like todo:')
    while running:
        user_action = input('Check password strength (1), generate a password (2) or type "exit" to exit.')
        if user_action == '1':
            return strength_checker()
        elif user_action == '2':
            return password_generator()

        elif word_exit in user_action.lower():
            return exit_function()
        else:
            print('Invalid input, try again')
            continue
    pass