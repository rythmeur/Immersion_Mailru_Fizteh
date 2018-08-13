# coding=utf-8
'''
На этой неделе мы с вами реализуем собственный key-value storage. Вашей задачей будет написать скрипт, который принимает в качестве аргументов ключи и значения и выводит информацию из хранилища (в нашем случае — из файла).
Запись значения по ключу
> storage.py --key key_name --val value
Получение значения по ключу
> storage.py --key key_name
Ответом в данном случае будет вывод с помощью print соответствующего значения
> value
или
> value_1, value_2
если значений по этому ключу было записано несколько. Метрики сохраняйте в порядке их добавления. Обратите внимание на пробел после запятой.
Если значений по ключу не было найдено, выводите пустую строку или None.
Для работы с аргументами командной строки используйте модуль argparse. Вашей задачей будет считать аргументы, переданные вашей программе, и записать соответствующую пару ключ-значение в файл хранилища или вывести значения, если был передан только ключ. Хранить данные вы можете в формате JSON с помощью стандартного модуля json. Проверьте добавление нескольких ключей и разных значений.
Файл следует создавать с помощью модуля tempfile.
'''

import os
import tempfile #Generate temporary files and directories
import argparse
import json
from pprint import pprint

def insertion (key, value):                                            #функция вставляет новые ключ-значение в словарь файла. Если файла еще нет - создаем, если есть - записываем ключ-значение, если ключ уже есть-добавляем значение к ключу
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data') #получаю путь временного файла
    #print (storage_path)
    f_content = {}
    if not os.path.exists(storage_path):                            #
        with open(storage_path, 'w') as f:                          # создаем файл
            f_content = {key:[value]}
            #f.write("f_content")
    else:
        with open(storage_path, 'r+') as f:
            #print("have to insert key-value")
            f_content = json.load(f)                                # полностью считываем содержание файла в словарь JSON
            #print (type(f_content), f_content )
            if key in f_content:
                f_content[key].append(value)                        # если ключ уже есть - добавляем еще одно значение в лист к этому ключу
            else:
                f_content[key] = [value]                            # если ключа нет - добавляем в словарь новую пару ключ-значение
    with open(storage_path, 'w') as f:
        json.dump(f_content, f)

def search (key):                                                   # если на вход программе подается только ключ (python storage.py --key 43), ищем - есть ли он, и выдаем значение по нему
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    #print (storage_path)
    f_content = {}
    if not os.path.exists(storage_path):
        #print("no file but have key")
        return [""]                                                 # если даже файла нет, то и искать нечего, возращаем пустую строку
    else:
        with open(storage_path, 'r') as f:
            #print("read value from key")
            f_content = json.load(f)                                # считали содержимое файла
            #print (type(f_content), f_content )
            if key in f_content:
                return f_content[key]                               # поискали в нем ключ, по ключу выдали значение
            else:
                return [""]                                         # если ничего не нашли - пустая строка


parser = argparse.ArgumentParser()
parser.add_argument("--key", type=str, help="the key")              # если такая команда (python storage.py --key 43 --val 33), то в args.key попадает то что после --key и т.д., тип - строка
parser.add_argument("--val", type=str, help="the value")

args = parser.parse_args()
key_name =args.key
value =args.val
#print(key_name, value)

if args.key and args.val:
    #print("super, ve have a pair")
    insertion(key_name,value)
elif args.key:
    #print("we have key, start searching")
    result = search(key_name)
    print (', '.join([str(elem) for elem in result]))

else:
    print("")


'''
Решение
Поздравляем с первой полноценной программой на Python в рамках нашего курса! Она была заметно сложнее предыдущих и помогла вам разобраться сразу с несколькими моментами. Хорошим подходом было бы разбить свою программу на функции — обратите внимание, все команды вынесены в отдельные функции, а get_data мы переиспользуем в нескольких местах. Ключевым моментом в разработке любого приложения является выбор подходящей структуры данных. В этом примере логичным вариантом было использовать словарь, потому что он по сути и является key-value хранилищем, а значения просто хранить в списке.
Также в этом задании мы использовали модуль argparse для считывания аргументов командной строки и json для хранения данных в файле. Самым простым подходом было просто перечитывать при каждом обращении файл, преобразуя его в словарь, добавляя значения при необходимости. Модуль os помогает нам в проверке существования файла хранилища при первом запуске программы. В Python богатая стандартная библиотека, очень важно представлять себе, какие модули помогут нам в решении наших задач, и уметь быстро разбираться в документации к новым функциям.
Обратите внимание, в примере мы для простоты используем глобальную переменную, однако в реальном приложении вы, скорее всего, написали бы для решения похожей задачи свой класс и инкапсулировали бы в нём информацию о хранилище и его методы. В следующей неделе мы разберем объектно-ориентированный подход и его плюсы.

import argparse
import json
import os
import tempfile


storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')


def clear():
    os.remove(storage_path)


def get_data():
    if not os.path.exists(storage_path):
        return {}

    with open(storage_path, 'r') as f:
        raw_data = f.read()
        if raw_data:
            return json.loads(raw_data)

        return {}


def put(key, value):
    data = get_data()
    if key in data:
        data[key].append(value)
    else:
        data[key] = [value]

    with open(storage_path, 'w') as f:
        f.write(json.dumps(data))


def get(key):
    data = get_data()
    return data.get(key)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--key', help='Key')
    parser.add_argument('--val', help='Value')
    parser.add_argument('--clear', action='store_true', help='Clear')

    args = parser.parse_args()

    if args.clear:
        clear()
    elif args.key and args.val:
        put(args.key, args.val)
    elif args.key:
        print(get(args.key))
    else:
        print('Wrong command')

'''