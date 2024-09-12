import re 

# ОСНОВНОЙ МАТЕРИАЛ: https://habr.com/ru/articles/349860/ 

print("\n---Основные функции")


print("\n---re.search(pattern, string)")
# Найти в строке string первую строчку, подходящую под шаблон pattern

match = re.search(r'\d\d\D\d\d', r'Телефон 123-12-12') 
print(match[0] if match else 'Not found') # -> 23-12 

match = re.search(r'\d\d\D\d\d', r'Телефон 1231212') 
print(match[0] if match else 'Not found') # -> Not found 

print("\n---re.fullmatch(pattern, string)")
# Проверить, подходит ли строка string под шаблон pattern

match = re.fullmatch(r'\d\d\D\d\d', r'12-12') 
print('YES' if match else 'NO') # -> YES 

match = re.fullmatch(r'\d\d\D\d\d', r'Т. 12-12') 
print('YES' if match else 'NO') # -> NO 

print("\n---re.split(pattern, string, maxsplit=0)")
# Аналог str.split(), только разделение происходит по подстрокам,
# подходящим под шаблон pattern
print(re.split(r'\W+', 'Где, скажите мне, мои очки??!')) 
# -> ['Где', 'скажите', 'мне', 'мои', 'очки', ''] 


print("\n---re.findall(pattern, string)")
# Найти в строке string все непересекающиеся шаблоны pattern
print(re.findall(r'\d\d\.\d\d\.\d{4}', 
                 r'Эта строка написана 19.01.2018, а могла бы и 01.09.2017')) 
# -> ['19.01.2018', '01.09.2017'] 

print("\n---re.finditer(pattern, string)")
# Итератор по всем непересекающимся шаблонам pattern в строке string
# (выдаются match-объекты)
for m in re.finditer(r'\d\d\.\d\d\.\d{4}', r'Эта строка написана 19.01.2018, а могла бы и 01.09.2017'): 
    print('Дата', m[0], 'начинается с позиции', m.start()) 
# -> Дата 19.01.2018 начинается с позиции 20 
# -> Дата 01.09.2017 начинается с позиции 45 

print("\n---re.sub(pattern, repl, string, count=0)")
# Заменить в строке string все непересекающиеся шаблоны pattern на repl
print(re.sub(r'\d\d\.\d\d\.\d{4}', 
             r'DD.MM.YYYY', 
             r'Эта строка написана 19.01.2018, а могла бы и 01.09.2017')) 
# -> Эта строка написана DD.MM.YYYY, а могла бы и DD.MM.YYYY

print("\n---Задача: Сколько слов в строке?")
# Слово — это последовательность из букв (русских или английских),
# внутри которой могут быть дефисы.
# На вход даётся текст, посчитайте, сколько в нём слов.

words = """
Он --- серо-буро-малиновая редиска!! 
>>>:-> 
А не кот. 
www.kot.ru
"""

words = re.findall(r'\b[\w-]{1,}', words)
print(words)
print(len(words))
