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

def isNegative(string):
    return string[0] == '-'

def string_to_signed_integer(s):
    trimmed_string = [c for c in s if c.isnumeric()]
    
    value = 0
    for char in trimmed_string:
        value = (10 * value) + DIGITS[char]

    if (isNegative(s)):
        value *= -1
        
    return value

print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True
