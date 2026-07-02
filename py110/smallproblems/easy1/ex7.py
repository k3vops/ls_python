# Your code goes here

# P
# given a sentence, split it into words and swap the first and last letters, retaining case, return reconstructed sentence

# D
# list of words, first and last letter

# A
# 

# C
# 


def swap(sentence):
    list_of_words = sentence.split(" ")
    
    list_of_swapped_words=[]
    for word in list_of_words:
        
        if len(word) == 1:
            list_of_swapped_words.append(word)
            continue
            
        last_char = word[len(word)-1]
        first_char = word[0]
        
        if len(word) == 2:
            list_of_swapped_words.append(last_char + first_char)
            continue
    
        inner_chars = word[1:len(word)-1]
        list_of_swapped_words.append(last_char + inner_chars + first_char)
    return " ".join(list_of_swapped_words)

print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True
