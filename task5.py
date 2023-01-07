# 5 Задайте число. Составьте список чисел 
# Фибоначчи, в том числе для отрицательных индексов.
# *Пример:*
# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 

list_positives = [0,1]
n = input("Номер элемента ряда Фибоначчи: ")
n = int(n)
fib1 = list_positives[0]
fib2 = list_positives[1]
i = 0
while i < n - 1:
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    list_positives.append(fib_sum)
    i = i + 1
 
print("положительные:", list_positives)

list_negatives = [1,-1]
fib_neg_1 = list_negatives[0]
fib_neg_2 = list_negatives[-1]
a = 0
while a > -n + 2:
    fib_neg_sum = fib_neg_1 - fib_neg_2
    fib_neg_1 = fib_neg_2
    fib_neg_2 = fib_neg_sum
    list_negatives.append(fib_neg_sum)
    a = a - 1
print("отрицательные:", list_negatives)
final_list = list_negatives[::-1] + list_positives
print("весь список:", final_list)







# my_list = []
# my_list[0] = 0
# my_list[1] = 1
# # def negatives(x):
# #     x[0] = 1
# #     x[-1] = -1
# #     for a in range(-x(len),0):
# #         x[a] = x[a+2]+x[a+1]
# #     return(x)

# def positives(x):

#     for a in range(0,x(len)):
#         x[a] = x[a-1]+x[a-2]
#     return(x)

# my_list1 = positives(my_list)
# # my_list2 = negatives(my_list)
# print(my_list)