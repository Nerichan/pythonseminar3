# 3 Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением 
# дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
nums_list = [1.1, 1.2, 3.1, 5, 10.01]
new_nums = []
for i in range(0, len(nums_list)):
    nums_list[i] = float(nums_list[i]) - int(nums_list[i])
    nums_list[i] = round(nums_list[i], 2)
    if nums_list[i] == 0:
        continue
    else:
        new_nums.append(nums_list[i])
remainder = max(new_nums) - min(new_nums)
print(remainder)
   