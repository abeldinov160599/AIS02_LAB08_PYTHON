#!/usr/bin/env python3
# coding=utf-8

# Имеется таблица в два столбца и 10 строк. В первом сттолбце исходные данные,
# во втором нужно выполнить расчет значений по формуле:
# y = sqrt((Proizv(K(i))-Summ(K(i-1))/sin^2(K(i)+K(i-1)))/abs(K(i))
# Вычисления произвести используя классы.

import math  # для вычислений
from random import randint  # для заполнения таблицы


def print_array(array):  # для красивого вывода на экран
    for i in array:
        print("%d\t%.2f" % (i[0], i[1]))


class Complex(object):  # объявляем класс
    # Аргумент self обязателен для всех методов всех классов
    def __init__(self):  # конструктор класса
        self.values = []  # инициализируем массив

    def add_value(self, value):  # метод добавления чисел
        self.values.append(value)

    def get_value(self, index):  # геттер
        return self.values[index]

    def proizv_minus(self, index):  # метод подсчета произведений
        prod = 1
        for i in range(index):
            if self.values[i] < 0:
                prod *= self.values[i]
        return prod

    def summ_plus(self, index):  # метод посчета сумм
        summa = 0
        for i in range(index):
            if self.values[i] > 0:
                summa += self.values[i]
        return summa

    def summ_trg(self, index):
        summa = 0
        for i in range(index):
            summa += (math.sin(self.values[i])-math.cos(self.values[i]))
        return summa

    def result_for(self, i):  # метод для решения основного задания
        y = self.proizv_minus(i) + self.summ_plus(i)
        y = y / math.sqrt(self.summ_trg(i))
        return y


def main():
    array = []  # массив для хранения таблицы
    task = Complex()  # создаем объект
    for i in range(10):
        task.add_value(randint(1, 10))  # добавляем 10 разных значений
        # Записываем все в массив
        array.append([task.get_value(i), task.result_for(i)])
    print_array(array)  # выводим на экран


if __name__ == '__main__':
    main()
