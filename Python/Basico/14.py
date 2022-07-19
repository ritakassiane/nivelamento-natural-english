from datetime import date

# Recebe uma string no formato ('ano, mes, dia') e retorna seus valores no formato [ano, mes, dia]
def formatDate(date):
    date = date.split(',')
    return [int(item) for item in date]


def deltaDays(first_date, last_date):
    last = formatDate(last_date)
    print(last)
    first = formatDate(first_date)
    print(first)
    result = date(last[0], last[1], last[2]) - date(first[0], first[1], first[2]) # datetime.timedelta object
    # print(f'{result//653}')
    return result.days

print("# Calculando a diferença entre duas datas #")
print(" ")
last = input('Digite a data mais no futuro no formato "Ano, Mês, Dia": ')
first = input('Digite a primeira data formato "Ano, Mês, Dia": ')
print(deltaDays(first, last))
# print(deltaDays('2014, 7, 2', '2014, 7, 11'))

