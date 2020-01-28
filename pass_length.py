
def find_pass_length():
    user_name = input('Please enter a username --> ')
    password = input('Please enter a password --> ')
    pass_length = len(password)

    print(f'{user_name}, your password is {"*" * pass_length} is {pass_length} letters long.')

find_pass_length()