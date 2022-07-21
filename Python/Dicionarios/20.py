def unic_values(list_):
    unic_values = set(value for dict_ in list_ for value in dict_.values())
    return unic_values

print(f'Unic values: {unic_values([{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}])}')