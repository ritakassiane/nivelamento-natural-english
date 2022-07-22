from datetime import datetime

def string_to_datetime(string):
    return datetime.strptime(string, '%b %d %Y %I:%M%p')

print(string_to_datetime('Jan 1 2014 2:43PM'))