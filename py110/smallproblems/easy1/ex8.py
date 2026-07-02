# Your code goes here

def get_ascii(my_char):
    return ord(my_char)-48 # - ord('0')

def string_to_integer(string):
    my_return_int = 0
    string_length = len(string)
    for i in range(0, string_length):
      my_exponent = (string_length - i) - 1 # for ones column, exponent must be 0
      my_return_int += get_ascii(string[i]) * (10 ** my_exponent)
    return my_return_int

print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True
