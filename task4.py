# 4 Напишите программу, которая будет 
# преобразовывать десятичное число в двоичное.
# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
decimal_num = int(input('please write decimal number: '))
binary_num = []
while decimal_num > 0:
    n = decimal_num%2
    binary_num.append(n)
    decimal_num = int(decimal_num/2)
print(''.join((map(str, binary_num))))
