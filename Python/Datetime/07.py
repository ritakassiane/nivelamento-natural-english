from datetime import date
from datetime import datetime

def date_to_datetime():
    return(datetime.combine(date.today(),datetime.min.time() ))

print(date_to_datetime())