# Модуль os в Python — это библиотека функций для работы с операционной системой.

# Модуль os даёт возможность не только получать полезные сведения о платформе,
# но и работать с содержимым диска, создавая новые директории и файлы,
# переименовывая и полностью удаляя их.

import os

print("\n---Получение информации об ОС")
print(os.name) # nt


print("\n---Конфигурация компьютера")
# ...название системного диска, адрес домашней директории,
# имя системы и массу другой информации
print(os.environ)


print("\n---Доступ к различным переменным среды")
print(os.getenv("TMP"))
print(os.getenv("USERNAME"))
print(os.getenv("PGUSER"))


print("\n---Сведения о текущей директории")
print(os.getcwd())


print("\n---Изменение рабочей директории")
# Если указанного пути на самом деле не существует,
# программа будет завершена в аварийном режиме из-за выброшенного исключения.
os.chdir(r"C:\DISK_D")


print("\n---Проверка существования пути")
print(os.path.exists("C:\DISK_D"))      # True
print(os.path.exists("D:/test.txt"))    # False


print("\n---Является ли объект файлом")
print(os.path.isfile(r"C:\DISK_D\_6_python-for-first-job\final\files\names.csv")) # True
print(os.path.isfile(r"C:\DISK_D\_6_python-for-first-job\final\files")) # False


print("\n---Является ли объект директорией")
print(os.path.isdir(r"C:\DISK_D\_6_python-for-first-job\final\files\names.csv")) # False
print(os.path.isdir(r"C:\DISK_D\_6_python-for-first-job\final\files")) # True


print("\n---Создание директории")
# os.mkdir(r"C:\DISK_D\_6_python-for-first-job\final\files\test_folder")


print("\n---Генерация цепочки папок")
# folder\first\second\third
# os.makedirs(r"C:\DISK_D\_6_python-for-first-job\final\files\folder\first\second\third")


print("\n---Удаление файлов и директорий")
# os.remove(r"D:\test.txt")
# os.rmdir(r"D:\folder")
# os.removedirs(r"D:\folder\first\second\third")


print("\n---Запуск на исполнение")
# os.startfile(r"C:\DISK_D\_6_python-for-first-job\final\files\names.csv")


print("\n---Получение имени файла С РАСШИРЕНИЕМ")
# Иногда для взаимодействия с документом необходимо получить его полное имя,
# включающее разрешение, но не абсолютный путь к нему на диске.
print(os.path.basename(r"C:\DISK_D\_6_python-for-first-job\final\files\names.csv"))
# names.csv


print("\n---Получение пути к файлу БЕЗ НАЗВАНИЯ САМОГО ОБЪЕКТА")
print(os.path.dirname(r"C:\DISK_D\_6_python-for-first-job\final\files\names.csv"))


print("\n---Вычисление размера")
print(os.path.getsize(r"C:\DISK_D\_6_python-for-first-job\final\files\names.csv"))


print("\n---Переименование")
# os.rename(r"D:\folder", r"D:\catalog")
# os.renames(r"D:\folder\first\second", r"D:\catalog\one\two")


print("\n---Содержимое директорий")
# Проверить наличие в каталоге определенных объектов позволяет функция listdir.
# С её помощью можно получить информацию о файлах и папках в виде списка
print(os.listdir(r"C:\DISK_D\_6_python-for-first-job\final\files"))
# ['data.json', 'names.csv', 'people.csv', 'people2.csv']

for root, directories, files in os.walk(r"C:\DISK_D\_6_python-for-first-job\final"):
    print("ROOT: ", root)
    for directory in directories:
        print("DIRECTORY: ", directory)
    for file in files:
        print("FILE: ", file)


print("\n---Статистика о файлах и директориях")
print(os.stat(r"C:\DISK_D\_6_python-for-first-job\final\files"))


print("\n---Разъединение пути к файлу и имени файла в различные строки")
print(os.path.split(r"C:\DISK_D\_6_python-for-first-job\final\files\names.csv"))

print("\n---Соединение пути к файлу с его названием")

print(os.path.join(r'C:\\DISK_D\\_6_python-for-first-job\\final\\files', 'names.csv'))