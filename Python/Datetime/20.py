import calendar
from datetime import datetime 

c = calendar.Calendar(firstweekday=calendar.SUNDAY) 

def get_n_tuesday(n, month, year):
    monthcal = c.monthdatescalendar(year,month) # todos os dias do mês month desse ano year
    all_tuesday = [day for week in monthcal for day in week if day.weekday() == calendar.TUESDAY and day.month == month] 
    # print(all_tuesday[n])
    return all_tuesday[n]



def is_third_tuesday(day, n, month, year):
    date = datetime.strptime(day, '%b %d, %Y')
    print(f'data de entradda: {date.date()}')
    return date.date() == get_n_tuesday(n, month, year)

print(is_third_tuesday('Jun 7, 2022', 3, 7,2022))
print(is_third_tuesday('Jul 17, 2022', 3, 7,2022))
print(is_third_tuesday('Jul 26, 2022', 3, 7,2022))