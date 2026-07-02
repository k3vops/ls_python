# PEDAC

# problem: modify a list of numbers, so that each subsequent number adds all previous numbers in the list
# inputs: list of numbers
# outputs: list of numbers

# comprehension
# each item tallies the earlier tallies, tally could be a data structure


def running_total(my_list):
    if my_list == []:
        return my_list
    
    new_list = []
    for index in range(0, len(my_list)):
        if index == 0:
            new_list.append(my_list[index])
            continue
        current_tally = sum(my_list[0:index + 1])
        new_list.append(current_tally)
    return new_list

print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True
