def input_value_list(count_values):
    list_data = []
    for i in range(count_values):
        list_data += [float(input('Введіть значення '+ str(i+1) + ' змінної: '))]
    return list_data