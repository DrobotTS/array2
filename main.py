import importlib
import sys

from TK_1 import input_value_list #импорт функции с ТК_1
from TK_2 import min_and_max #импорт функции с ТК_2
from TK_3 import everage_elem #импорт функции с ТК_3
from TK_4 import multiplication_avarage #импорт функции с ТК_4




def main():
    sqrt = importlib.import_module('TK-5')  # созданние новой переменной с файла ТК-5
    count = int(input('Введіть кількість змінних: '))
    list_data = input_value_list(count)
    res_1 = list_data
    min_and_max1 = min_and_max(list_data)
    everage_elem1 = everage_elem(list_data)
    multiplication_avarage1 = multiplication_avarage(list_data)
    square_root1 = sqrt.square_root(list_data)
    print(f'Заданий список: {res_1}')
    print(f'Минімальне та максимальне значення: {min_and_max1}')
    print(f'Ділення на середне значення: {everage_elem1}')
    print(f'Множення на середне значення: {multiplication_avarage1}')
    print(f'Корень квадратний: {square_root1}')
    return 0

sys.exit(main()) if __name__ == '__main__' else print('error')