#У меня вариант 1!

from random import randint
import sorts
from prettytable import PrettyTable
import time

import copy



N = int(input("Введите N: "))
massiv = []

for i in range(N):
    massiv.append(randint(1, 10000)) # Случайные значения не превышающие 10000

massiv_cop1 = copy.copy(massiv)
massiv_cop2 = copy.copy(massiv)
sorted(massiv_cop1)
sorted(massiv_cop2, reverse=True)


mytable = PrettyTable()
mytable.field_names = ["Метод", "Отсортированная","Случайная", "Отсортированная в обратном порядке"]


tm2 = sorts.bubble(massiv,N )
tm1 = sorts.bubble(massiv_cop1,N )
tm3 = sorts.bubble(massiv_cop2,N )


mytable.add_row(["Метод пузырьком", tm1, tm2, tm3])


tm2 = sorts.insertion(massiv)
tm1 = sorts.insertion(massiv_cop1)
tm3 = sorts.insertion(massiv_cop2)


mytable.add_row(["Метод вставками", tm1, tm2, tm3])


s2 = time.perf_counter()
sorts.quick(massiv)
tm2 = time.perf_counter()

s1= time.perf_counter()
sorts.quick(massiv_cop1)
tm1 = time.perf_counter()

s3 = time.perf_counter()
sorts.quick(massiv_cop2)
tm3 = time.perf_counter()
#print ("QQQ =  ",tm3 - s3,"  ", s3, " ", tm3  ) # проверка кода

mytable.add_row(["Быстрая сортировка", tm1-s1, tm2-s2, tm3-s3])

table = mytable.get_string()

f = open("output.txt", "w")
f.write(table)
f.write('\n')
f.close()
