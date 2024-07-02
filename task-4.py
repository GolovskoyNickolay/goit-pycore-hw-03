from datetime import datetime, date, timedelta


def get_upcoming_birthdays(users: list) -> list:
    today = date.today()
    list_of_birthdays = []
    for user in users:
        user_b_day = datetime.strptime(user['birthday'], '%Y.%m.%d').date().replace(today.year)
        # add current year to user birthday and check if it exists within next week
        if today - timedelta(days=1) < user_b_day < today + timedelta(days=7):
            if user_b_day.weekday() == 5:
                user_b_day = user_b_day + timedelta(days=2)
            elif user_b_day.weekday() == 6:
                user_b_day = user_b_day + timedelta(days=1)
            list_of_birthdays.append({'name': user['name'], 'congratulation_date': user_b_day.strftime('%Y.%m.%d')})
    return list_of_birthdays


users = [
    {"name": "John Doe", "birthday": "1985.07.06"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
