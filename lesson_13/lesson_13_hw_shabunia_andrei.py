import json
print('Задача_1: Массив из слов и чисел, записать в файл сначала слова с сортировкой по len, а потом цифры')


def sorting_values(values):
    lst_dig = []  # список с цифровыми значениями
    lst_alp = []  # список с буквенными значениями
    for elem in values:
        if str(elem).isdigit():
            lst_dig.append(elem)
        elif elem.isalpha():
            lst_alp.append(elem)
    lst_alp = sorted(lst_alp, key=len)  # сортировка по длине слов
    lst_dig = sorted(lst_dig)  # сортировка по возрастанию чисел
    return lst_alp, lst_dig


lst = ('HELLO', 67, 'word', 'hi', 4, 20, 'python', 3)   # передаваемый массив из чисел и строк
lst_list = list(sorting_values(lst))
f = open('words_and_numbers.txt', 'w')
f.write(str(lst_list[0]))  # добавление списка слов
f.write(str(lst_list[1]))  # добавление списка цифр
print(f'* Ответ в файле: words_and_numbers.txt')

print('Задача_2: Пользователь вводит название и стоимость покупок до ввода "стоп", записать в JSON')
values_name = []  # список наименований
values_price = []  # список стоимостей
while True:
    int_data = input('Введите через пробел название и стоимость покупки (завершить покупки: "стоп"): ').split()
    if int_data[0] == 'стоп':
        break
    elif int_data[0].isdigit() or int_data[1].isalpha():  # проверка на корректность ввода: 1 - слово, 2 - число.
        print('Ошибка! Введите сначала слово, затем число')
        continue
    else:
        values_name.append(int_data[0])
        values_price.append(int_data[1])
shopping_list = {'название': values_name, 'стоимость': values_price}
with open('shopping_list.json', 'w', encoding='UTF-8') as file:
    json.dump(shopping_list, file, ensure_ascii=False)
print(f'* Ответ в файле: shopping_list.json')

print('Задача_3: Прочитать файл из предыдущего задания и вывести стоимость всех покупок за день')
with open('shopping_list.json', 'r', encoding='UTF-8') as file:
    data_values = json.load(file)
count = 0  # счетчик стоимости покупок
for i in data_values['стоимость']:  # итерация по списку по ключу "стоимость"
    count += int(i)
print(f'Стоимость всех покупок: {count}')
