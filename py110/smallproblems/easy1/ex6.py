# Your code goes here
# Your code goes here


# PEDAC
# split a sentence into its 'words' (space-separated) and count the letters of each word, show the tallied result

# inputs: string
# outputs: dictionary {number_of_letters: count}
# unordered

# d --> dictionary, list of words
# a --> comprehension, sub-function

# given a list_of_words
# for each word, count how many letters it has
# if doesn't exist, add to dictionary
# if exists, increment

def word_sizes(sentence):
    if len(sentence) == 0:
        return {}
    
    list_of_words = sentence.split(" ")
    my_dictionary = {}
    for word in list_of_words:
        my_alnum_word = "".join([letter for letter in word if letter.isalnum()])
        current_key=len(my_alnum_word)
        current_value= 1 if current_key not in my_dictionary.keys() else (my_dictionary[current_key] + 1) 
        my_dictionary.update({current_key: current_value})
    return my_dictionary

# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})
