import datetime

print("\n---Применение")
# Получение текущих системных даты и времени
# Вычисления разницы между датами и другие арифметические операции
# Сравнение значений времени
# Форматированный вывод информации о дате и времени
# MINYEAR == 1
# MAXYEAR == 9999 соответственно.
# Это минимальное и максимально возможное значение года, используемые в библиотеке.


print("\n---Отличие datetime от time")
# Модуль time в отличие от datetime не позволяет производить
# арифметические операции со временем


print("\n---Классы библиотеки datetime")
# КЛАСС         ОПИСАНИЕ

# date	        представляет собой дату,
#               полностью исключая данные о времени,
#               на основе Григорианского календаря

# time	        включает данные о времени,
#               полностью игнорируя сведения о дате

# datetime	    содержит информацию о времени и дате,
#               основываясь на данных из Григорианского календаря

# timedelta	    описывает определенный период во времени,
#               который находится между двумя различными моментами

# tzinfo	    представляет различные сведения о часовом поясе

# timezone	    описывает время, руководствуясь стандартом UTC


print("\n---date")
a = datetime.date(2001, 10, 28)
print(a, type(a))

a = datetime.date.today()
print(a, type(a))

a = datetime.date(2012, 7, 21)
print(f"{a.year = }; {a.month = }; {a.day = }")


print("\n---time")
# Недостающие данные о времени автоматически заполняются нулями,
# в то время как введенные числа добавляются в объект от большего к меньшему
a = datetime.time(12, 18, 35, 5867)
print(a, type(a))

a = datetime.time(23, 5, 30)
b = datetime.time(7, 26)
c = datetime.time(21)
print(a, type(a))
print(b, type(b))
print(c, type(c))

a = datetime.time(16, 3, 49, 23578)
print(f"{a.hour = }; {a.minute = }; {a.second = }; {a.microsecond = }")


print("\n---datetime")
# Создавать объекты можно с разным набором параметров,
# указывая только нужные сведения.
# Отсутствующие данные по умолчанию будут заполнены нулями
c = datetime.datetime(2017, 7, 18, 4, 52, 33, 51204)
print(c, type(c))

a = datetime.datetime(2007, 2, 13)
b = datetime.datetime(2013, 10, 25, 12, 8, 47)
print(a, type(a))
print(b, type(b))

# Получить текущий момент времени можно при помощи двух разных методов
a = datetime.datetime.today()
b = datetime.datetime.now()
print(a, type(a))
print(b, type(b))

a = datetime.datetime(2015, 3, 27, 8, 12, 24, 34574)
print(f"{a.year = }")
print(f"{a.month = }")
print(f"{a.day = }")
print(f"{a.hour = }")
print(f"{a.minute = }")
print(f"{a.second = }")
print(f"{a.microsecond = }")


print("\n---Форматирование вывода")

# Формат	Значение
# %a	    название дня недели в сокращенном виде
# %A	    название дня недели в полном виде
# %w	    номер дня недели в виде целого числа
# %d	    номер дня месяца в виде целого числа
# %b	    название месяца в сокращенном виде
# %B	    название месяца в полном виде
# %m	    номер месяца в числовом представлении
# %y	    номер года без столетия
# %Y	    номер года в полном представлении
# %H	    количество часов в 24-часовом формате
# %I	    количество часов в 12-часовом формате
# %p	    до полудня или после полудня в 12-часовом формате
# %M	    количество минут в виде целого числа
# %S	    количество секунд в виде целого числа
# %f	    количество микросекунд в виде целого числа
# %z	    часовой пояс в формате UTC
# %Z	    название часового пояса
# %j	    номер дня в году
# %U	    номер недели в году, если считать с воскресенья
# %w	    номер недели в году, если считать с понедельника
# %c	    местное представление даты и времени
# %x	    местное представление даты
# %X	    местное представление времени
# %%	    символ процента

a = datetime.datetime.today().strftime("%d.%m.%Y")
b = datetime.datetime.today().strftime("%H:%M:%S")
print(a, type(a))
print(b, type(b))


print("\n---Формирование datetime при помощи date и time")
a = datetime.date(2015, 3, 19)
b = datetime.time(2, 10, 43)
c = datetime.datetime.combine(a, b)
print(c, type(c))


print("\n---Операции")

# Операция	Значение
# a + b	    суммирует значения дат a и b
# a – b	    находит разницу между датами a и b
# a * i	    умножает численное представление свойств даты a на некую константу i
# a // i	делит численное представление свойств даты a на некую константу i,
#           остаток отбрасывается
# +a	    возвращает объект timedelta с полностью идентичным значением a
# –a	    возвращает объект timedelta с полностью противоположным значением a
# a > b	    возвращает true, если a больше b
# a < b	    возвращает true, если a меньше b
# abs(a)	возвращает объект timedelta с положительным значением всех свойств a
# str(a)	возвращает строковое представление объекта a в формате,
#           заданном по умолчанию
# repr(a)	возвращает строковое представление объекта a в формате
#           с отрицательными значениями

a = datetime.datetime.now()
b = datetime.datetime(2023, 6, 29)
c = a - b
print(c, type(c))
print(f"{c.days = }")
# print(f"{c.minutes = }") # 'datetime.timedelta' object has no attribute 'minutes'
print(f"{c.seconds = }")
print(f"{c.microseconds = }")


print("\n---timedelta")
# Класс timedelta предназначен для удобного выполнения
# различных манипуляций над датами и временем
a = datetime.datetime(2006, 12, 5)
b = datetime.timedelta(hours=2, minutes=5, seconds=17)
c = a + b
print(a, type(a))
print(b, type(b))
print(c, type(c))


print("\n---tzinfo и timezone")
# Классы tzinfo и timezone применяются для работы с информацией,
# которая содержит сведения о часовых поясах

# Создать объект, принадлежащий типу tzinfo невозможно,
# поскольку этот класс является абстрактным.
# Однако можно воспользоваться наследованием,
# создав собственный класс на основе tzinfo.
# При этом следует помнить,
# что для работы с такими объектами придется реализовать несколько абстрактных методов,
# к числу которых относятся:
#   - utcoffset (смещение по местному времени с UTC)
#   - dst (настройка перехода на летнее время)
#   - tzname (имя часового пояса в виде строки)

from datetime import tzinfo, timedelta, datetime, timezone

class UTC0530(tzinfo):
    def __init__(self, offset=19800, name=None):
        self.offset = timedelta(seconds=offset)
        self.name = name or self.__class__.__name__

    def utcoffset(self, dt):
        return self.offset

    def tzname(self, dt):
        return self.name

    def dst(self, dt):
        return timedelta(0)

a = datetime.now(timezone.utc)
print(a)
b = datetime.now(UTC0530())
print(b)

print(b.utcoffset())
print(b.tzname())
print(b.dst())

print("\n---timezone using pytz module")
from datetime import datetime
import pytz

datetime_in_GB = datetime.now(pytz.timezone('GB'))
print(datetime_in_GB, type(datetime_in_GB))

all_timezones = pytz.all_timezones
print(all_timezones)

