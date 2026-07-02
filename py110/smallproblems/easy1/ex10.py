DIGITS = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
}

def get_string_key_by_int(my_int):
    return [x for (x, y) in DIGITS.items() if y == my_int][0]

def keep_going(my_num, exponent):
    number, remainder =  divmod(my_num, exponent)
    return not (number == 0 and remainder == 0)

def integer_to_string(my_int):
    EXPONENT = 10
    my_num = my_int
    my_string = ""
    
    if (my_int == 0):
        my_key = get_string_key_by_int(my_int)
        my_string = my_key + my_string
    
    while (keep_going(my_num, EXPONENT)):
        number, remainder = divmod(my_num, EXPONENT)
        my_key = get_string_key_by_int(remainder)
        my_string = my_key + my_string
        my_num = number
    return my_string
    
print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True
