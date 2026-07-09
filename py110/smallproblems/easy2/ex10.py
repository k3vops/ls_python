import math

def average(my_list):
    my_sum = sum(my_list)
    return math.floor(my_sum / len(my_list))

print(average([1, 5, 87, 45, 8, 8]) == 25)        # True
print(average([9, 47, 23, 95, 16, 52]) == 40)     # True
print(average([7]) == 7)                          # True