"""
Базовый синтаксис
"""
import typing # типизация (int | float) ...


# основные типы и структуры
types = [
    ...,
    None,
    True, False, bool,
    1, int,
    1.1, float,
    ' ', " ", """ """, f'', r'', str,
    b'', bytes, # байтовые объекты
    [], list,
    (), tuple,
    {1, }, set,
    {}, dict
]


# основные операторы
_ = 1 + 2
_ = 1 - 2
_ = 1 * 2
_ = 1 ** 2
_ = 1 / 2
_ = 1 // 2
_ = 1 % 2
_ = None and 2      # None      truthy/falsy value
_ = 1 and 2         # 2         truthy/falsy value
_ = 1 or 2          # 1         truthy/falsy value
_ = True | True     # True      bit opetarion
_ = True | False    # True      bit opetarion
_ = False | True    # True      bit opetarion
_ = False | False   # False     bit opetarion

print(f"{bin(2) = }, {bin(1) = }, {2 | 1 = }")  # 2 | 1 = 3

_ = 1 > 2   | 1 >= 2   | 1 < 2   | 1 <= 2       # False
_ = 1 > (2  | 1) >= (2 | 1) < (2 | 1) <= 2      # False
_ = (1 > 2) | (1 >= 2) | (1 < 2) | (1 <= 2)     # True

_ = 2 > 5 < 3           # False
_ = 2 < 5 < 10 > 20     # False

_ = 2 == (2  | 5) == 5          # False (2 == 7 == 5)
_ = 2 == 2   | 5 == 5           # False
_ = (2 == 2) | (5 == 5)         # (True | True) = True


# цикл for
for _ in types:
    pass

for _ in types:
    break
else:
    pass


# Comprehensions
a = [i for i in types]
b = (i for i in types)
c = {i for i in types if isinstance(i, typing.Hashable)}
d = {str(i): i for i in types}
print(c)


# Присвоение, распаковка, срезы
e, *f, g = types
h = [*f]
_ = [1, 2, 3][:]
_ = {**{}}


# Утверждение assert
# assert 5 < 0, 'test' # AssertionError: test


# цикл while
a = [i for i in types]
while a:
    a.pop()

while a:
    break
else:
    pass


# Функции
def func(text: str, space: str, action: typing.Callable) -> None:
    if not text:
        return

    print(space + action(text))
    func(text[1:], space + ' ', action) # рекурсия
    print(space + action(text))


# lambda функции
func('*' * 5, '', lambda text: ' '.join(i for i in text))


# Декораторы
def decorator(multiplier: int):

    def dec(func: typing.Callable):
        # Области видимости функции
        global a, b, c, d
        nonlocal multiplier

        if multiplier % 2 == 0:
            multiplier += 1

        def wrap(*args, **kwargs): # f становится функцией wrap
            for _ in range(multiplier):

                # Генераторы
                yield func(*args, **kwargs)

        return wrap
    return dec

# @decorator(4)
# @decorator(5)
def f(num: int) -> int:
    return num

# # v1
# qwe = [*f(1)]
# print(qwe)

# # v2
f = decorator(7)(f) # получаем доступ к функции wrap (аналог @decorator(7))
qwe = [i for i in f(2)] # [*f(2)]
print(qwe)

# # v3
# f = decorator(3)(f)
# for i in f(3):
#     print(i, end=",")

# Условия
d = {str(i): i for i in types}

if i := d.get(''): # dict.get(key[, default])
    pass
elif not (q := d.get(1)):
    pass
else:
    ...


# match qwe:
#     case "1":
#         pass
#     case _:
#         pass


# Исключения и их обработка
try:
    1 / 0
except ZeroDivisionError as exc:
    pass
else:
    pass
finally:
    ...


# Классы
class A:

    class_attrs = None

    def __init__(self, *args, **kwargs):
        self.args, self.kwargs = args, kwargs
        self.__test_arg = None

    def main(self) -> None:
        print("main() of A class")

    def __str__(self):
        return f"{self.__class__}/ args:{self.args}, kwargs:{self.kwargs}, __test_arg:{self.__test_arg}"

    @property
    def test_arg(self) -> typing.Any:
        return self.__test_arg

    @test_arg.setter
    def test_arg(self, value: typing.Any):
        self.__test_arg = value


class B(A):

    def main(self) -> None:
        super().main()
        print("main() of B class")

    @classmethod
    def create(cls, *args, **kwargs) -> 'B':
        return cls(*args, **kwargs)

    @staticmethod
    def get_test() -> str:
        return 'test'

print("\n---Classes")

b1 = B(x = 3, y = 7)
b1.test_arg = 50
b1.main()

b2 = B.create(x = 31, y = 71)
b2.test_arg = 501

print(b1)
print(b2)

a = A('point', z = 1)
a.class_attrs = (7, 8, 9)
print(a.__dict__)

