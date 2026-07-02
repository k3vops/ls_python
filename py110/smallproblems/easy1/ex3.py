# Your code goes here

def is_real_palindrome(string_arg):
    my_temp_list = list(string_arg)
    my_temp_list.reverse()
    my_temp_list = [letter for letter in my_temp_list if letter.isalnum()]
    my_reversed_string = "".join(my_temp_list)
    my_original_arg_modified = [letter for letter in string_arg if letter.isalnum()]
    my_original_arg_modified = "".join(my_original_arg_modified)
    return my_original_arg_modified.casefold() == my_reversed_string.casefold()

print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True

# case doesn't matter
print(is_real_palindrome('Madam') == True)           # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True) # True
