import datetime

def find_age():
    birth_year = int(input('What is your birth year?'))
    current_year = datetime.datetime.now().year
    print(current_year - birth_year)

find_age()

