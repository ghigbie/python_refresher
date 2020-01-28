
def find_pass_length():
    user_name = input('Please enter a username --> ')
    password = input('Please enter a password --> ')

    print(f'{user_name}, your password is {"*" * len(password)} is {len(password)} letters long.')

find_pass_length()