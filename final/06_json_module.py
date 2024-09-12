import json

print("\n---JSON")
# JSON в Python обозначает JavaScript Object Notation,
# который является широко используемым форматом данных
# для обмена данными в Интернете

print("\n---Сериализация и десериализация")
# Упаковка объектов в байтовую последовательность называется сериализацией.
# А распаковка байтов в объекты языка программирования,
# приведение последовательности назад к типам и структурам, — десериализацией.

# Сериализация
# Объекты Python	->  JSON
# 1.	Dict	        Object
# 2.	list, tuple	    Array
# 3.	Str	            String
# 4.	int, float	    Number
# 5.	True            true
# 6.	False           false
# 7.	None	        null

# Десериализация
# 	JSON	   ->   Python
# 1.	Object	        Dict
# 2.	Array	        list
# 3.	String	        str
# 4.	Number          (int)	int
# 5.	true	        True
# 6.	false	        False
# 7.	null	        None


# объявляем переменные
t = "Main"
c = 211
data = [1, 2, 3, 4, 5]
status = None
res = True

mydict = {"t": t, "c": c, "data": data, "status": status, "res": res}
print(mydict, type(mydict))


print("\n---Функции Dumps Loads")
# Dumps позволяет создать JSON-строку из переданного в нее объекта.
# Loads — преобразовать строку назад в объекты языка

# сериализуем его в JSON-структуру, как строку
x = json.dumps(mydict)
print(x, type(x))
# print(x["title"]) # TypeError: string indices must be integers

# проводим десериализацию JSON-объекта
y = json.loads(x)
print(y, type(y))
print(y["t"]) # Main


print("\n---Функции Dump Load")
# Dump и load используют, чтобы сохранить результат в файл или воссоздать объект.
# Работают они схожим образом,
# но требуют передачи специального объекта для работы с файлом — filehandler

# создаем filehandler с помощью контекстного менеджера
with open("files/data.json", "w") as fh:
    json.dump([1, 2, 3, 4, 5], fh) # записываем структуру в файл

# открываем тот же файл, но уже на чтение
with open("files/data.json", "r") as fh:
    res = json.load(fh) # загружаем структуру из файла

print(res)

print("\n---Работа с пользовательскими классами")
# Пользовательские классы не относятся к JSON-сериализуемым.
# Это значит, что просто применить к ним функции
# dumps, loads или dump и load не получится

class Test:
    def __init__(self, title, num):
        self.title = title
        self.body = num

t = Test("car", 455)
print(t.__dict__)


print("\n---Простой вариант сериализации, параметр default")
# используем анонимную функцию (лямбду), которая
# в качестве сериализуемых данных указывает полученный __dict__ объекта
x = json.dumps(t, default=lambda x: x.__dict__)
print(x, type(x))


print("\n---Добавляем название родительского класса объекта")


def to_json(obj):
    if isinstance(obj, Test):
        result = obj.__dict__
        result["className"] = obj.__class__.__name__
        return result


t2 = Test("house", 134)
x = json.dumps(t2, default=to_json)
print(x, type(x))

print("\n---Используем специальный класс json.JSONEncoder")

class TestEncoder(json.JSONEncoder):
    def default(self, o):
        return {"TITLE": o.title, "BODY": o.body, "CLASSNAME": o.__class__.__name__}

x = json.dumps(t, cls=TestEncoder)
print(x, type(x))

y = json.loads(x)
print(y, type(y))


print("\n---Применим паттерн «Адаптер»")
# Идея в том, чтобы написать класс,
# который приводит к JSON пользовательские объекты и восстанавливает их


class Figure:
    def __init__(self, title, form, color):
        self.title = title
        self.form = form
        self.color = color
 
    def __str__(self):
        return f"Figure: {self.title}, {repr(self.form)}, {repr(self.color)}"
 
class Form:
    def __init__(self, name):
        self.name = name
 
    def __repr__(self):
        return f"<Form: {self.name}>"
 
class Color:
    def __init__(self, name):
        self.name = name
 
    def __repr__(self):
        return f"<Color: {self.name}>"


class JSONDataAdapter:
    @staticmethod
    def to_json(o):
        if isinstance(o, Figure):
            return json.dumps({
              "title": o.title,
              "form": o.form.name,
              "color": o.color.name,
            })
 
    @staticmethod
    def from_json(o):
        o = json.loads(o)
 
        try:
            form = Form(o["form"])
            color = Color(o["color"])
            figure = Figure(o["title"], form, color)
            return figure
        except AttributeError:
            print("Неверная структура")


# создадим несколько цветов
black = Color("Black")
yellow = Color("Yellow")
green = Color("Green")

# несколько форм
rountt = Form("Rounded")
square = Form("Squared")

# объекты фигур
figure_one = Figure("Black Square", form=square, color=black)
figure_two = Figure("Yellow Circle", form=rountt, color=yellow)

print("Отображение объектов:")
print(figure_one)
print(figure_two)
print()

# преобразуем данные в JSON
jone = JSONDataAdapter.to_json(figure_one)
jtwo = JSONDataAdapter.to_json(figure_two)

print("Отображение JSON:")
print(jone)
print(jtwo)
print()

# восстановим объекты
restored_one = JSONDataAdapter.from_json(jone)
restored_two = JSONDataAdapter.from_json(jtwo)

print("Отображение восстановленных объектов:")
print(restored_one)
print(restored_two)

