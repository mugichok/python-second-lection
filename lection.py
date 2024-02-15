# list1 = [] - создание пустого списка
# list2 = list() создание пустого списка
# list1 = [1,2,3,4,5,6,6]
# print(*list1) - *убирает квадратные скобки, то есть выводит только содержимое списка

# for i in list1:
#     print(i)

# print(list1.append(9)) - добавляет элемент в конец списка

# print(list1.pop(4)) усдаляет элемент с номером аргумента 

# print(list1.insert(0,8)) меняет элемент с номером первого аргумента на элемент, равный второму аргументу 

# t = ()
# print(type(t))

# t = (1, 2, 3,)

# v = [1,7,6]
# print(v)
# print(type(v))

# v = tuple(v)
# print(v)
# print(type(v))

# a, b, c = v
# print(a, b, c)

# t = (1,2,3,4,5,) - кортеж

# for i in t:
#     print(i)

# d = {} - словари
# d = dict()

# d['q'] = 'qwerty'
# print(d)

# d['2'] = '2werty'
# print(d)


# print(d['2'])

# dictonary = {}
# dictonary = {'up': '↑', 'left': '←', 'right': '→', 'down': '↓'}
# print(dictonary)
# print(dictonary['left'])
# типы ключей могут отличаться
# print(dictonary['up'])
# dictonary['left'] = '⇦' 
# print(dictonary['left'])
# print(dictonary['type'])
# del dictonary ['left']
# for item in dictonary:
#     print('{}: {}', format(item, dictonary[item]))
# for (k,v) in dictonary.items():
#     print(k,v)


# множества

# colors = {'red', 'blue', 'gray', 'black'}
# print(colors)
# colors.add('red')
# print(colors)
# colors.add('orange')
# print(colors)
# colors.remove('red')
# print(colors)
# colors.discard('red')
# print(colors)
# colors.clear()
# print(colors)

# a = {1,2,3,4,5}
# b= {1,5,6,3,4,8}
# c = a.copy() #копирует элементы множества
# р = a.union(b) # объединяет множества, оставляю только уникальные значения
# i = a.intersection(b) # пересечние, находит элементы, которые есть в обоих множествах
# k = a.difference(b) # вычитает множество b из множества a
# k1 = b.difference(a) # вычитает множество b из множества a
# q = a.union(b).difference(a.intersection(b))

# замороженное множество 
# a = {1,4,5,3,7}
# b = frozenset(a)

# создать список, состоящий из чётных значений от 1 до 100
list1 = []
for i in range(1,100):
    if i%2 == 0:
        list1.append(i)
print(list1)

list1 = [i for i in range(1,101) if i%2 == 0]
# создание кортежа чисел
list1 = [(i,i) for i in range(1,101) if i%2 == 0]
list1 = [i*2 for i in range(1,101) if i%2 == 0]

