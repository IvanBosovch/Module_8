from datetime import datetime, date
from collections import defaultdict

users = [{"name": "Bill Gates", "birthday": datetime(1955, 10, 4).date()},
         {"name": "Ivcan df", "birthday": datetime(1955, 10, 2).date()},
         {"name": "Bdfdf", "birthday": datetime(1955, 10, 2).date()}]
def get_birthdays_per_week(users:list):
    today = date.today()
    dict_birthday = defaultdict(list)

    if not users:
        return dict_birthday
    
    for i in users:
        value_day = i.get('birthday').replace(year=today.year)
        value_name = i.get('name')
        dif_date = value_day - today

        if dif_date.days < 0:
            value_day = i.get('birthday').replace(year=today.year + 1)
            dif_date = value_day - today

        if 0 < dif_date.days <= 6:
            if 4 < value_day.weekday() <= 6:
                dict_birthday['Monday'].append(value_name)
            else:
                day = datetime.strftime(value_day, '%A')
                dict_birthday[day].append(value_name)

    return dict_birthday

print(get_birthdays_per_week(users))