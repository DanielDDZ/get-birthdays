from datetime import datetime, timedelta, date


fist_day = {
    '1': datetime.now() - timedelta(days=2),
    '2': datetime.now() - timedelta(days=3),
    '3': datetime.now() - timedelta(days=4),
    '4': datetime.now() - timedelta(days=5),
    '5': datetime.now() - timedelta(days=6),
    '6': datetime.now(),
    '7': datetime.now() - timedelta(days=1),
}

last_day = {
    '1': datetime.now() + timedelta(days=4),
    '2': datetime.now() + timedelta(days=3),
    '3': datetime.now() + timedelta(days=2),
    '4': datetime.now() + timedelta(days=1),
    '5': datetime.now(),
    '6': datetime.now() + timedelta(days=6),
    '7': datetime.now() + timedelta(days=5),
}


def get_birthdays_per_week(users):
    week = {
        '1': 'Monday',
        '2': 'Tuesday',
        '3': 'Wednesday',
        '4': 'Thursday',
        '5': 'Friday',
        '6': 'Monday',
        '7': 'Monday',
    }

    congratulations_current_week = {
        'Monday': '',
        'Tuesday': '',
        'Wednesday': '',
        'Thursday': '',
        'Friday': '',
    }
    congratulations_next_week = congratulations_current_week.copy()

    today = str(datetime.isoweekday(datetime.now()))
    first_current_week = fist_day[today].date()
    last_current_week = last_day[today].date()
    first_next_week = last_current_week + timedelta(days=1)
    last_next_week = first_next_week + timedelta(days=6)
    current_year = datetime.now().year

    for user in users:
        if user['birthday'].year <= current_year:
            user['birthday'] = date(
                year=current_year, month=user['birthday'].month, day=user['birthday'].day)
            if user['birthday'].month in (first_current_week.month, last_next_week.month):
                if first_current_week <= user['birthday'] <= last_current_week:
                    congratulations_current_week[week[str(
                        date.isoweekday(user['birthday']))]] += user['name'] + ', '
                elif first_next_week <= user['birthday'] <= last_next_week:
                    congratulations_next_week[week[str(
                        date.isoweekday(user['birthday']))]] += user['name'] + ', '

    print('Current week:')
    print_result(congratulations_current_week)
    print('Next week:')
    print_result(congratulations_next_week)


def print_result(week):
    for key, value in week.items():
        if value != '':
            value = value[:-2]
            week[key] = value
            print(key + ':', value)


get_birthdays_per_week([{'name': 'Jim', 'birthday': date(year=2012, month=10, day=1)},
                        {'name': 'Kim', 'birthday': date(
                            year=1990, month=10, day=5)},
                        {'name': 'Diana', 'birthday': date(
                            year=1998, month=9, day=24)},
                        {'name': 'Daniel', 'birthday': date(
                            year=1995, month=10, day=2)},
                        {'name': 'Sam', 'birthday': date(
                            year=2000, month=10, day=8)},
                        {'name': 'Maria', 'birthday': date(
                            year=1996, month=10, day=7)},
                        {'name': 'Bill', 'birthday': date(
                            year=1999, month=9, day=27)},
                        {'name': 'Elina', 'birthday': date(
                            year=1997, month=9, day=24)},
                        {'name': 'Marina', 'birthday': date(
                            year=1995, month=9, day=25)},
                        {'name': 'Alex', 'birthday': date(year=2005, month=9, day=23)}])
