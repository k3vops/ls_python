def digit_list(number):
    new_list = []
    my_number = number
    length = len(f"{number}")
    for i in range(0, length):
        result, remainder = divmod(my_number, 10)
        new_list.insert(0, remainder)
        my_number = result
    return new_list

print(digit_list(12345) == [1, 2, 3, 4, 5])       # True
print(digit_list(7) == [7])                       # True
print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
print(digit_list(444) == [4, 4, 4])               # True