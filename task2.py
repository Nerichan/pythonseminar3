#2 Напишите программу, которая 
# найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, 
# второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
my_list = [2, 3, 5, 6]
my_list_end = len(my_list)-1
my_list_start = 0
pairs = []
for i in range (0,my_list_end):
    pair_mult = my_list[my_list_start]*my_list[my_list_end]
    pairs.append(pair_mult)
    my_list_start = my_list_start + 1
    my_list_end = my_list_end - 1
    if my_list_end == my_list_start:
        break
print(pairs)