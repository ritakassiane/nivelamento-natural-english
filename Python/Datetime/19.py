from datetime import date
from datetime import timedelta

# TODO: Adicionar parametro data
def last_data_of_day(day):
    today = date(2022, 7, 18)
    offset = (today.weekday() - day) % 7
    return today - timedelta(days=offset)


"""
0 -> Segunda
1 -> Terça
2 -> Quarta
.
.
.

"""

print(last_data_of_day(1))