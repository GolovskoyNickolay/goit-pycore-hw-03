import datetime


def get_days_from_today(date: str) -> int:
    try:
        splitted_date = date.split('-')
        input_year = int(splitted_date[0])
        input_month = int(splitted_date[1])
        input_day = int(splitted_date[2])
    except Exception:
        print('Invalid date format, correct format is YYYY-MM-DD')
    else:
        input_date = datetime.date(input_year, input_month, input_day)
        today = datetime.date.today()
        result = today - input_date
        return result.days


print(get_days_from_today('2023-07-02'))
