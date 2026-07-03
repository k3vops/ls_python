# P given length x of list, return 2 lists each having half (first list gets )
# E 
# D 
# I - 
# O - 
# A 
# C 

def halvsies(my_list):
    length = len(my_list)
    result, remainder = divmod(length, 2)
    list_length_1 = result + remainder
    list_length_2 = result
    result_list_1 = []
    result_list_2 = []
    # note: can use slicing here instead:
    # return [my_list[:list_length_1],my_list[list_length_1:]]
    if (list_length_1 > 0):
        for i in range(0, list_length_1):
            result_list_1.append(my_list[i])
    if (list_length_2 > 0):
        for j in range(list_length_1, len(my_list)):
            result_list_2.append(my_list[j])
    result = [result_list_1, result_list_2]
    return result

# All of these examples should print True
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])