# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

# TODO: your code here
import random
n = int(input("n: "))
numb = []
i = 0
while i < n:
    numb.append(random.randint(-100, 100))
    i += 1

total = 0
for el in numb:
    if el > 0 and el% 2 == 0:
        total += el

print(total)
