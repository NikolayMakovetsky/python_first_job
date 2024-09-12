"""
Работа с разными форматами:
- работа со временем и датами
- работа с Decimal
- работа с регулярными выражениями
- работа с файлами (например csv)
- Работа с вводом/выводом
- Работа с uuid
- Работа с os
- Работа с кодировками
"""
import csv
import datetime
import decimal
import json
import os
import re
import time
import uuid

# Даты
print("\n---Даты")
today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)
current_time = datetime.datetime.now()
current_timestamp = current_time.timestamp()

print(f"{today = }")
print(f"{yesterday = }")
print(f"{tomorrow = }")
print(f"{current_time = }")
print(f"{current_timestamp = }")

in_str = current_time.strftime('%d:%m:%y %H:%M:%S')
in_datetime = datetime.datetime.strptime(in_str, '%d:%m:%y %H:%M:%S')

print(f"{in_str = }")
print(f"{in_datetime = }")

timestamp = time.time()
from_timestamp = datetime.datetime.fromtimestamp(timestamp)

print(f"{timestamp = }")
print(f"{from_timestamp = }")

# работа с Decimal
print("\n---работа с Decimal")
context = decimal.getcontext()
print(f"{context = }")
context.rounding = decimal.ROUND_DOWN
print(f"{context = }")

a = decimal.Decimal('0.3')
b = decimal.Decimal(0.3)
c = b.quantize(decimal.Decimal('.0001'), rounding=decimal.ROUND_UP)

print(f"{a = }")
print(f"{b = }")
print(f"{c = }")

# работа с регулярными выражениями
print("\n---работа с регулярными выражениями")
# Функция compile() модуля re компилирует шаблон регулярного выражения pattern
# в объект регулярного выражения,
# который может быть использован для поиска совпадений
# с использованием методов Match.match(), Match.search() и других способов
pattern = re.compile(r'^@(\w+)$')
nicknames = ['@qweqwe', '@@qweqwe', 'qweqwe', 'qwe@qwe']
valid_nicknames = [i for i in nicknames if re.match(pattern, i)]

print(f"{pattern = }")
print(f"{nicknames = }")
print(f"{valid_nicknames = }")



# Работа с файлами
print("\n---Работа с файлами")
# some_dict = {'qwe': 123}
# file_name = 'files/new.json'
file_name = 'files/new.csv'
with open(file_name, 'w') as file:
    # json.dump(some_dict, fp=file, indent=4, ensure_ascii=False)
    fieldnames = ['nicknames', 'length']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for nickname in valid_nicknames:
        writer.writerow({'nicknames': nickname, 'length': len(nickname)})

with open(file_name, 'r') as file:
    # json_obj = json.load(file)
    reader = csv.DictReader(file)
    for row in reader:
        print(row['nicknames'], row['length'])


# Ввод/вывод
# test = input('test:').split()
test = 'test'.split()
for i in range(3):
    print(*test, sep='(╯ ° □ °) ╯ ┻━┻', end='\n' + '\t' * i,)


# Работа с uuid
print("\n---Работа с uuid")
# UUID = Universally Unique Identifiers
# Значения UUID полезны для генерации идентификаторов для документов,
# хостов, клиентов приложений и других ситуаций,
# когда необходимо уникальное значение

# uuid.uuid1() может нарушить конфиденциальность,
# поскольку создает идентификатор, содержащий сетевой адрес компьютера
uid = uuid.uuid1()
print(uid)

# uuid.uuid4() создает случайный UUID
uid = uuid.uuid4()
print(uid)

# Работа с os
print("\n---Работа с os")
path = os.path.join(__file__, 'qweqwe')
print(path)
print(os.getenv('ENV_NAME'))

os.system('echo 123')
# Command to execute
# Using Windows OS command
cmd = 'date'
 
# Using os.system() method
os.system(cmd)

# Кодировки
a = 'qweqwe'.encode('utf-16')
b = a.decode('utf-16')

# В Python используются следующие кодировки:
# ASCII     — латинские буквы, цифры и простые символы
# CP1251    — кириллическая кодировка (русский и другие языки)
# KOI-8     — кодировка для русского языка
# UTF-8     — Юникод-кодировка для всех языков (длина символа — 8 бит)
# UTF-16    — Юникод-кодировка для всех языков (длина символа — 16 бит)