# Сортировка списка /количество перестановок / дефах/10,100,1000,10 000/ не повторяющиеся
# Лабораторная работа по сортировкам
import copy
import random
import time

N = 100  # int(input('Number'))    # Задаётся в процессе исследования разным
M = 11  # int(input('Number'))    # Задается в процессе исследований разным

arr = [random.randint(1, N) for x in range(1, M)]
arr2 = copy.copy(arr)
arr3 = copy.copy(arr)
arr4 = copy.copy(arr)
arr5 = copy.copy(arr)
arr6 = copy.copy(arr)
arr7 = copy.copy(arr)


# 1 пузырек (bubble)
def bubble(array):
    total = time.perf_counter()
    counter = 0
    n = len(array)
    for i in range(n):
        for j in range(n - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                counter += 1
    total = time.perf_counter() - total
    print(array, counter, total)


# bubble(arr)


# 2 усовершенствованный пузырек
def bubble_up(array):
    n = len(array)
    k = 1  # переменная, которая показывает, что во внутреннем цикле были перестановки
    total = time.perf_counter()
    counter = -1
    while k > 0:
        k = 0
        for j in range(n - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                k = 1
        counter += 1
        total = time.perf_counter() - total
    print(array, counter, total)


# bubble_up(arr)


# 3	шейкер
def sheiker(array):
    counter = 0
    total = time.perf_counter()
    left = 0  # Задаем левую границу сортируемой области массива
    right = len(array) - 1  # Задаем правую границу сортируемой области массива
    remember = 0  # Переменная для запоминания индекса переставленного элемента
    while left <= right:  # Выполнение цикла - пока левая граница не сомкнётся с правой
        for i in range(left, right, +1):  # Цикл движения слева направо
            if array[i] > array[i + 1]:  # Проверка: если следующий элемент меньше текущего, то
                array[i], array[i + 1] = array[i + 1], array[i]  # меняем их местами
            right -= 1  # запоминаем индекс переставленного элемента

            for v in range(right, left, -1):  # Цикл движения справа налево
                if array[v - 1] > array[v]:  # Проверка: если предыдущий элемент больше текущего, то
                    array[v], array[v - 1] = array[v - 1], array[v]  # меняем их местами
            left += 1  # запоминаем индекс переставленного элемента
            counter += 1

    total = time.perf_counter() - total
    print(array, counter, total)


# sheiker(arr)


# 4 Выбора
def choice(array):
    total = time.perf_counter()
    counter = 0
    for i in range(0, len(arr) - 1):
        min = i     # переменная с минимальным значением
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min]:   # Условие поиска меньшего значения
                min = j
        arr[i], arr[min] = arr[min], arr[i]

        counter += 1
        total = time.perf_counter() - total
    print(array, counter, total)
# choice(arr)

# 5 Вставки Шелла («с дыркой»)
def SortInsertHole(array):
    counter = 0
    total = time.perf_counter()
    for i in range(0, len(array)):
        tmp = array[i]
        hole = i
        while hole > 0 and array[hole - 1] > tmp:
            hole -= 1
            array[hole + 1] = array[hole]
        array[hole] = tmp
        counter += 1
    total = time.perf_counter() - total
    print(array, counter, total)


# SortInsertHole(arr)

# 6 Шелла
def shell(array):
    counter = 0
    total = time.perf_counter()
    interval = len(arr) // 2    # разделение эл-ов на группы
    while interval > 0:
        for i in range(interval, len(arr)):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
            array[j] = temp
        interval //= 2
        counter += 1
    total = time.perf_counter() - total
    print(array, counter, total)
# shell(arr)

# 7 Qsort
def QSort(array):
    mean = len(arr) // 2     # в качестве опорной точки берем средний элемент
    start = arr[0]
    finish = arr[-1]
    left = start
    right = finish
    while left < right:
        while array[left] < mean:
            left += 1
        while array[right] > mean:
            right -= 1
        if left <= right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
        if start < right:
            QSort(array)
        if left < finish:
            QSort(array)
        print(arr)
QSort(arr)



