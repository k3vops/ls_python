vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

def print_dict(my_dict):
    for (key,value) in my_dict.items():
        print(f"{key} => {value}")

def count_occurrences(my_list):
    my_dict = dict()

    for item in my_list:
        if item in my_dict:
            my_dict[item] += 1
        else:
            my_dict[item] = 1

    print_dict(my_dict)

count_occurrences(vehicles)

# your output sequence may appear in a different sequence
# car => 4
# truck => 3
# SUV => 1
# motorcycle => 2