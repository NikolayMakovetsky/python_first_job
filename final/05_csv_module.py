import csv


print("\n---Построчное чтение csv файла c записью в список")
with open('files/people.csv') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)

print("\n---Выбор типа разделителя")
with open('files/people2.csv') as csv_file:
    reader = csv.reader(csv_file, delimiter=';')
    for row in reader:
        print(row)


print("\n---Построчное чтение csv файла с формированием словаря")
with open('files/people.csv') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        print(row)


with open('files/people2.csv') as csv_file:
    reader = csv.DictReader(csv_file, delimiter=';')
    for row in reader:
        name = row['name']
        age = row['age']
        print(name, 'is', age, 'years old.')


print("\n---Запись в csv файл (С ЗАГОЛОВКОМ)")
with open('files/names.csv', 'w') as csv_file:
    header = ['first', 'last']
    writer = csv.DictWriter(csv_file, fieldnames=header, lineterminator="\r")
    
    writer.writeheader()
    writer.writerow({'first': 'Jack', 'last': 'Hill'})
    writer.writerow({'first': 'James', 'last': 'Mitch'}) # словарь


print("\n---Запись в csv файл (БЕЗ ЗАГОЛОВКА)")
with open('files/names.csv', 'a', encoding="cp1251") as csv_file:
    writer = csv.writer(csv_file, delimiter = ",", lineterminator="\r")
    # Обратите внимание, что при записи использовался, lineterminator="\r".
    # Это разделитель между строками таблицы, по умолчанию он "\r\n".
    writer.writerow(['@Harry', '@Potter'])
    writer.writerow(['@Jermiona', '@Granger']) # список строк
    writer.writerow(['@@__Женя', '@@__Козлов']) # encoding="cp1251"


with open('files/names.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)
    

with open('files/names.csv') as csv_file:
    reader = csv.DictReader(csv_file)
    i = 0
    for col in reader:
        i += 1
        print(f"{i}. {col['first'] = }, {col['last'] = }")