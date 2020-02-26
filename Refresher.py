#### EXERSISE ################################## EXERSISE ################################## EXERSISE ##############################


### 1
"""Write a function named sum_values that takes a dictionary named my_dictionary as a parameter.
The function should return the sum of the values of the dictionary"""


# def sum_values(my_dictionary): # !!! Forgot how to set val = 0. Set val = '' and []
#     val = 0
#     for value in my_dictionary.values():
#         val += value
#     return val
#
#
# print(sum_values({"milk": 5, "eggs": 2, "flour": 3}))
# # should print 10
# print(sum_values({10:1, 100:2, 1000:3}))
# should print 6

### 2
"""Create a function called sum_even_keys that takes a dictionary named my_dictionary, with all integer keys and values, as a parameter.
 This function should return the sum of the values of all even keys."""

# def sum_even_keys(my_dictionary): # !!! Forgot key %  2 == 0: Put key %  2
#     sum_val = 0
#     for key, value in my_dictionary.items():
#         if key %  2 == 0:
#             sum_val += value
#     return sum_val
#
#
#
# print(sum_even_keys({1: 5, 2: 2, 3: 3}))
# # should print 2
# print(sum_even_keys({10: 1, 100: 2, 1000: 3}))
# should print 6

### 3
"""Create a function named add_ten that takes a dictionary with integer values named my_dictionary as a parameter.
 The function should add 10 to every value in my_dictionary and return my_dictionary"""

# def add_ten(my_dictionary): # !!! Forgot how to do it
#     for key in my_dictionary.keys():
#         my_dictionary[key] += 10
#     return my_dictionary
#
#
# print(add_ten({1: 5, 2: 2, 3: 3}))
# # should print {1:15, 2:12, 3:13}
# print(add_ten({10: 1, 100: 2, 1000: 3}))
# should print {10:11, 100:12, 1000:13}


### 4
"""Create a function named values_that_are_keys that takes a dictionary named my_dictionary as a parameter. 
This function should return a list of all values in the dictionary that are also keys."""

# def values_that_are_keys(my_dictionary):
#     val_list = []
#     for key, values in my_dictionary.items():
#         if values in my_dictionary.keys():
#             val_list.append(values)
#
#     return val_list
#
#
#
# print(values_that_are_keys({1: 100, 2: 1, 3: 4, 4: 10}))
# # should print [1, 4]
# print(values_that_are_keys({"a": "apple", "b": "a", "c": 100}))
# # should print ["a"]

### 5
"""Write a function named max_key that takes a dictionary named my_dictionary as a parameter.
 The function should return the key associated with the largest value in the dictionary."""

# def max_key(my_dictionary):
#     larg_val = []
#     for keys, values in my_dictionary.items():
#         larg_val.append(values)
#         max_val = max(larg_val)
#     for keys, values in my_dictionary.items():
#         if values == max_val:
#             return keys
#
#
# print(max_key({1: 100, 2: 1, 3: 4, 4: 10}))
# # should print 1
# print(max_key({"a": 100, "b": 10, "c": 1000}))
# # should print "c"

### 6 Word Length Dict

"""Write a function named word_length_dictionary that takes a list of strings named words as a parameter. 
The function should return a dictionary of key/value pairs where every key is a word in words and every value is the length of that word."""

# def word_length_dictionary(words):
#     return {word: len(word) for word in words}
#
# print(word_length_dictionary(["apple", "dog", "cat"]))
# # should print {"apple":5, "dog": 3, "cat":3}
# print(word_length_dictionary(["a", ""]))
# # should print {"a": 1, "": 0}

### 7
"""Write a function named frequency_dictionary that takes a list of elements named words as a parameter.
 The function should return a dictionary containing the frequency of each element in words."""


# def frequency_dictionary(words):
#     return {word: words.count(word) for word in words}
#     # dict = {} # longer solution
#     # for word in words:
#     #     dict[word] = words.count(word)
#     # return dict
#
#
# print(frequency_dictionary(["apple", "apple", "cat", 1]))
# # should print {"apple":2, "cat":1, 1:1}
# print(frequency_dictionary([0,0,0,0,0]))
# # should print {0:5}

### 8 Unique Values
"""Create a function named unique_values that takes a dictionary named my_dictionary as a parameter. 
The function should return the number of unique values in the dictionary."""


# def unique_values(my_dictionary):
#     seen_values = []
#     for value in my_dictionary.values():
#         if value not in seen_values:
#             seen_values.append(value)
#     return len(seen_values)
#
#
# print(unique_values({0:3, 1:1, 4:1, 5:3}))
# # should print 2
# print(unique_values({0:3, 1:3, 4:3, 5:3}))
# # should print 1

### 9
"""Create a function named count_first_letter that takes a dictionary named names as a parameter. names should be a
 dictionary where the key is a last name and the value is a list of first names. For example, the dictionary might look like this:"""

### my version
# def count_first_letter(names):
#     letters = {}
#     for key in names.keys():
#         if key[0] not in letters:
#             letters[key[0]] = len(names[key])
#     if key[0] in letters:
#         letters[key[0]] += len(names[key])
#
#     return letters
#
#
# print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# # should print {"S": 4, "L": 3}
# print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# # should print {"S": 7}