title: Answere quations
date: 2017-11-20 21:54
author: pavel burns
tags: General
category: codding
slug: answere

# Welcome to StackEdit!
https://www.youtube.com/watch?v=070WyS06e-Q
1. Стандартные типы данных
3. Разница между туплами и листами
4. Множества (set)
5. Стандартные библиотеки (sys, os, re, datetime)
6. PEP8
7. variable swap (x, y = y, x)
8. Разница между range() и xrange()
9. Минимальное значение в листе
10. Удалить повторяющиеся элементы в листе
11. str.split()
12. Mutable and immutable types
13. Менеджеры контекста
14. Итераторы и генераторы
15. yield
16. lambda functions
17. Разница между методом класса и статическим методом
18. Анонимные функции
19. Шаблоны проектирования (Singleton, Decorator, etc)
20. Магические методы
21. async/await﻿ (python 3.5)
22. Плюсы и минусы множественного наследования (это зло)
23. New style and old style classes
24. MRO
25. _slots_
26. Дескриптор протокола
27. Multiprocessing and threading
28. Metaclasses
29. Функция type()




#### Стандартные типы данных
Числа: int, float, complex(?)
Строки ' ',  " " 
Кортежи tuple( )
Списки list(help) ['h', 'e', 'l', 'p' ]

Кроме того, для списков определен ряд методов.
>append(x) Добавляет элемент в конец последовательности
	count(x) Считает количество элементов, равных x
	extend(s) Добавляет к концу последовательности последовательность s
	index(x) Возвращает наименьшее i, такое, что s[i] == x. Возбуждает исключение ValueError, если x не найден в s
	insert(i, x) Вставляет элемент x в i-й промежуток
	pop(i) Возвращает i-й элемент, удаляя его из последовательности
	reverse() Меняет порядок элементов s на обратный
	sort([cmpfunc]) Сортирует элементы s. Может быть указана своя функция сравнения cmpfunc

Словари { }
Цикл по паре ключ-значение

     for key, value in h1.items():
         print key, " ", value

Множества a = set('hello') - {'h', 'o', 'l', 'e'}  - "контейнер", содержащий не повторяющиеся элементы в случайном порядке.
File
None
#### Разница между тюплами и листами
tuple не изменяемый
list изменяемый
#### Множества (set)
Множество в python - "контейнер", содержащий не повторяющиеся элементы в случайном порядке.
#### Стандартные библиотеки (sys, os, re, datetime)
####  PEP8
https://pythonworld.ru/osnovy/pep-8-rukovodstvo-po-napisaniyu-koda-na-python.html
* Выровнено по открывающему разделителю
* Пробелы - самый предпочтительный метод отступов.
* Ограничьте длину строки максимум 79 символами.
* Каждый импорт, как правило, должен быть на отдельной строке.
*  Всегда окружайте эти бинарные операторы одним пробелом с каждой стороны: присваивания (=, +=, -= и другие), сравнения (==, <, >, !=, <>, <=, >=, in, not in, is, is not), логические (and, or, not).
* Не используйте пробелы вокруг знака =, если он используется для обозначения именованного аргумента или значения параметров по умолчанию.

#### variable swap (x, y = y, x)
> temp = x
 x = y
 y = temp
#### Разница между range() и xrange()
range в Python3 == xrange в Python2

#### Минимальное значение в листе

     a = [11,8,12,0] 
     min(a) 
     0 
     max(a) 
    12

####  Удалить повторяющиеся элементы в листе
можно вогнать в set 
или

    from itertools import groupby
    x = ['a', 'a', 'a', 'f', 'h', 'k', 'k']
    new_x = [el for el, _ in groupby(x)]
    print(new_x)    # ['a', 'f', 'h', 'k']

Универсальный способ:

    def f(l):
       n = []
        for i in l:
            if i not in n:
                n.append(i)
        return n

#### str.split()
Разбивает строку на части, используя разделитель, и возвращает эти части списком. Направление разбиения: слева направо

#### Mutable and immutable types

mutable - изменяемые, immutable - неизменяемые.
#### Менеджеры контекста
Менеджеры контекста позволяют выделять и освобождать ресурсы строго по необходимости. 

    with open('some_file', 'w') as opened_file:
        opened_file.write('Hola!')

Распространенный паттерн использования контекстных менеджеров - блокирование и разблокирование ресурсов, а также закрытие открытых файлов (как я уже показал выше).

Необходимый минимум функциональности контекстного менеджера требует методов __enter__ и __exit__

#### Итераторы и генераторы
Итератор - Любой обьект. реализующий метод __next__ без аргументов, который возвращает 
следующий элемент или возбуждает исключение StopIteration, если элементов не осталось.
В питоне итераторы реализуют реализуют также метод __iter__ и потому сами являются итерируемумы обьектами

Итератор представляет собой объект перечислитель, который для данного объекта выдает следующий элемент, либо бросает исключение, если элементов больше нет.
Основное место использования итераторов – это цикл for.

Итератором в Python называется объект, который имеет метод next (Python 2) __iter__  и __next__. Вот и все. Это итератор

Генераторы это итераторы, по которым можно итерировать только один раз. Так происходит поскольку они не хранят все свои значения в памяти, а генерируют элементы "на лету". Генераторы можно использовать с циклом for или любой другой функцией или конструкцией, которые позволяют итерировать по объекту. В большинстве случаев генераторы создаются как функции. Тем не менее, они не возвращают значение также как функции (т.е. через return), в генераторах для этого используется ключевое слово yield. Вот простой пример функции-генератора:

    def simple_generator(val):
       while val > 0:
           val -= 1
           yield 1
    
    gen_iter = simple_generator(5)
    print(next(gen_iter))
    print(next(gen_iter))
    print(next(gen_iter))
    print(next(gen_iter))
    print(next(gen_iter))
    print(next(gen_iter))
https://lancelote.gitbooks.io/intermediate-python/content/book/generators.html
#### yield
https://habrahabr.ru/post/132554/
Ключевым моментом для понимания работы генераторов является то, при вызове **yield** функция не прекращает свою работу, а “замораживается” до очередной итерации, запускаемой функцией next(). 


#### lambda functions
По идее, лямбда функции абсолютно то же самое, что и обычные функции, но без имени

####  Разница между методом класса и статическим методом
http://qaru.site/questions/385/what-is-the-difference-between-staticmethod-and-classmethod-in-python
В основном @classmethod создает метод, первым аргументом которого является класс, из которого он вызвал (а не экземпляр класса), @staticmethod не имеет никаких неявных аргументов.

    class A(object):
        def foo(self,x):
            print "executing foo(%s,%s)"%(self,x)
    
        @classmethod
        def class_foo(cls,x):
            print "executing class_foo(%s,%s)"%(cls,x)
    
        @staticmethod
        def static_foo(x):
            print "executing static_foo(%s)"%x    
    
    a=A()

####  Анонимные функции
Анонимные функции это однострочные функции, которые используются в случаях, когда вам не нужно повторно использовать функцию в программе. Они идентичны обыкновенным функциям и повторяют их поведение.

    add = lambda x, y: x + y
    
    print(add(3, 5))
     Вывод: 8


####  Шаблоны проектирования (Singleton, Decorator, etc)
https://ru.wikipedia.org/wiki/%D0%A8%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD_%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F


#### Магические методы
Они всё в объектно-ориентированном Питоне. Это специальные методы, с помощью которых вы можете добавить в ваши классы «магию». Они всегда обрамлены двумя нижними подчеркиваниями (например, __init__ или __lt__).
https://habrahabr.ru/post/186608/

####  async/await﻿ (python 3.5)
https://habrahabr.ru/post/266743/
 #### Плюсы и минусы множественного наследования (это зло)
 
#### New style and old style classes
#### MRO
https://habrahabr.ru/post/62203/
#### _slots_
Он включает использование __slots__, чтобы Python не создавал словари под хранение атрибутов, а выделял заданный объём памяти для ограниченного числа атрибутов.

    Без __slots__:
    class MyClass(object):
        def __init__(self, name, identifier):
            self.name = name
            self.identifier = identifier
            self.set_up()
        # ...
    С использованием __slots__:
    class MyClass(object):
        __slots__ = ['name', 'identifier']
        def __init__(self, name, identifier):
            self.name = name
            self.identifier = identifier
            self.set_up()
        # ...



####  Дескриптор протокола
https://habrahabr.ru/post/122082/
#### Multiprocessing and threading
https://python-scripts.com/threading
#### Metaclasses
https://habrahabr.ru/post/145835/
#### Функция type()
показывает тип 
#### полезные ссылки
https://www.gitbook.com/book/lancelote/intermediate-python/details

#### Функторы
https://habr.com/post/138676/

