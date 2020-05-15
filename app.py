# This is my birthday app
# The goal of this app is to send myself a text message in the morning when one of my friends has a birthday
# I don't have a Facebook so this is the best way for me to remember minus a calendar warning
import datetime

today = datetime.datetime.now()
day = today.day
month = today.month

birthdays = {
    'p1': {
        'name': 'Craig Massoni',
        'birthday_month': 10,
        'birthday_day': 29},
    'p2': {
        'name': 'Chris Brooks',
        'birthday_month': 10,
        'birthday_day': 29},
    'p3': {
        'name': 'Pat Brooks',
        'birthday_month': 10,
        'birthday_day': 29},
    'p5': {
        'name': 'Nick Overlack',
        'birthday_month': 5,
        'birthday_day': 2},
    'p6': {
        'name': 'Bryan Smith',
        'birthday_month': 6,
        'birthday_day': 2},
    'p7': {
        'name': 'Jacob Fishman',
        'birthday_month': 8,
        'birthday_day': 11},
    'p8': {
        'name': 'Mom',
        'birthday_month': 6,
        'birthday_day': 4},
    'p9': {
        'name': 'Dad',
        'birthday_month': 8,
        'birthday_day': 31},
}

for name, birthday in birthdays.items():
    if birthday['birthday_month'] == month and birthday['birthday_day'] == day:
        print(f"It is {birthday['name']}'s birthday today!")
    else:
        break








