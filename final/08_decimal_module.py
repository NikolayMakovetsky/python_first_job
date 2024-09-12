from decimal import Decimal, ROUND_HALF_EVEN

# При работе с числами с плавающей точкой (то есть float)
# порой мы сталкиваемся с тем, что в результате вычислений
# получаем неверный результат

print("\n---При работе с float можно получить неверный результат")

num = 0.1 + 0.1 + 0.1
print(num) # 0.30000000000000004

print("\n---Класс Decimal")

num = Decimal("0.1")
num = num + num + num
print(num) # 0.3

# В операциях с Decimal можно использовать целые числа
print(num + 3) # 3.3

# С помощью доп нулей мы указываем кол-во знаком после запятой
number = Decimal("0.10")
number = 3 * number
print(number) # 0.30


print("\n---Округление чисел - метод quantize()")
# Используемая строка "1.00" указывает,
# что округление будет идти до двух знаков в дробной части

number = Decimal("0.444")
number = number.quantize(Decimal("1.00"))
print(number)                                   # 0.44
 
number = Decimal("0.555678")
print(number.quantize(Decimal("1.00")))         # 0.56
 
number = Decimal("0.999")
print(number.quantize(Decimal("1.00")))         # 1.00

number = Decimal("10.025")      # 2 - ближайшее четное число
print(number.quantize(Decimal("1.00"), ROUND_HALF_EVEN))       # 10.02
 
number = Decimal("10.035")      # 4 - ближайшее четное число
print(number.quantize(Decimal("1.00"), ROUND_HALF_EVEN))       # 10.04

# ROUND_HALF_UP:    округляет число в сторону повышения,
#                   если после него идет число 5 или выше
# ROUND_HALF_DOWN:  округляет число в сторону повышения,
#                   если после него идет число больше 5
# ROUND_05UP:       округляет 0 до единицы,
#                   если после него идет число 5 и выше
# ROUND_CEILING:    округляет число в большую сторону
#                   вне зависимости от того, какое число идет после него
# ROUND_FLOOR:      не округляет число вне зависимости от того,
#                   какое число идет после него