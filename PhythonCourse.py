import subprocess
import os
import re
##from __future__ import with_statement
from grizzled.os import working_directory

# one = 3 ** 2 + 1 != 30 / 3
#
# # B:
# be = (9 - 4) * 2 == 77 / 7 - 1
#
# print one
# print be
#
#
# # A:
# var1 = 3 ** 2 + 1 != 30 / 3
#
# # B:
# var2 = (9 - 4) * 2 == 77 / 7 - 1
#
# print var1
# print var2


# def in_range(num, lower, upper):
#     if lower <= num <= upper:
#         return True
#     return False
#
#
# # Uncomment these function calls to test your in_range function:
# # print(in_range(10, 10, 10))
# # should print True
# print(in_range(5, 10, 20))


##### Quiz

# Write your twice_as_large function here:
# def twice_as_large(num1, num2):
#     var = num1 / 2
#     if var > num2:
#         return True
#     else:
#         return False
#
#     # Uncomment these function calls to test your twice_as_large function:
#
#
# print(twice_as_large(10, 5))
# # should print False
# print(twice_as_large(11, 5))
# # should print True


##### Quiz


# Write your large_power function here:
# def large_power(base, exponent):
#     if base ** exponent > 5000:
#         return True
#     else:
#         return False
#
#
# # Uncomment these function calls to test your large_power function:
# # print(large_power(2, 13))
# # should print True
# print(large_power(2, 12))
# # should print False

##### Quiz


# def divisible_by_ten(num):
#     return True if num % 10 == 0 else False
#     # if num % 10 >= 0:
#     #     return True
#     # else:
#     #     return False
#
#     # Uncomment these function calls to test your divisible_by_ten function:
#
#
# print(divisible_by_ten(20))
# # should print True
# # print(divisible_by_ten(25))

##### Quiz


# def max_num(num1, num2, num3):
#     if num1 > num2 and num1 > num3:
#         return num1
#     elif num2 > num1 and num2 > num3:
#         return num2
#     elif num3 > num1 and num3 > num2:
#         return num3
#     else:
#         return "It's a tie!"
#
#
# # Uncomment these function calls to test your max_num function:
# print(max_num(-10, 0, 10))
# # should print 10
# print(max_num(-10, 5, -30))
# # should print 5
# print(max_num(-5, -10, -10))
# # should print -5
# print(max_num(2, 3, 3))
# # should print "It's a tie!"

##### Quiz

# def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
#     if budget < (food_bill + electricity_bill + internet_bill + rent):
#         return True
#     else:
#         return False
#
#
# # Uncomment these function calls to test your over_budget function:
# print(over_budget(100, 20, 30, 10, 40))
# # should print False
# # print(over_budget(80, 20, 30, 10, 30))
# # should print True

# def always_false(num):
#     if 0 < num > 1:
#         return True
#     else:
#         return False
#
#
# # Uncomment umthese function calls to test your always_false function:
# print(always_false(0))
# # should print False
# print(always_false(-1))
# # should print False
# print(always_false(1))


# string1 = "The quick brown"
# string2 = "fox jumps over"
# string3 = string1+string2
# print(string3+" the lazy dog.")


######Len, Range

# list1 = range(2, 20, 3)
# list1_len = len(list1)
# print(list1_len)
#
#
# ### Count
# votes = ['Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie', 'Jake', 'Jake', 'Jake', 'Laurie', 'Cassie', 'Cassie',
#          'Jake', 'Jake', 'Cassie', 'Laurie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie']
#
# jake_votes = votes.count('Jake')
# print(jake_votes)
#
# ###Slicyng
#
# >>> fruits = ['apple', 'banana', 'cherry', 'date']
# >>> print(fruits[0:3])
# ['apple', 'banana', 'cherry']
#
# >>> print(fruits[:3])
# ['apple', 'banana', 'cherry']
#
# >>> print(fruits[2:])
# ['cherry' , 'date']
#
# suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']
# start = suitcase[:3]
# end = suitcase[-2:]

#
# ##### Sorted
# games = ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']
# #Option 1
# games.sort()
# #Option 2
# games_sorted = sorted(games)
# gamy = games.count('Portal')
# print(gamy)
#
# ## Zip
# toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']
# prices = [2, 6, 1, 3, 2, 7, 2]
# num_pizzas = len(toppings)
# print("We sell" +' '+ str(num_pizzas) +' '+ "different kinds of pizza!")
# pizzas = list(zip(toppings, prices))
# print(pizzas)

#
# from typing import List
#
# mylist = ['a', 'b', 'c', 'd', 'e']
# print(mylist[1:3])


# Write your function here
# def double_index(lst, index):
#   if index >= len(lst):
#     return lst
#   else:
#     new_lst = lst[0:index]
#     new_lst.append(lst[index]*2)
#     new_lst = new_lst + lst[index+1:]
#     return new_lst
#
# #Uncomment the line below when your function is done
# print(double_index([3, 8, -10, 12], 2))

# list1 = [1,2,3]
# list2 = list1 + list1[2:]
# print(list2)


# #Write your function here
# def remove_middle(lst, start, end):
#
#     #list = lst[end+1:]
#     list = lst[:start] + lst[end+1:]
#     return list
#
# #Uncomment the line below when your function is done
# print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))

# #Write your function here
# def more_than_n(lst, item, n):
#     list1 = lst.count(item)
#     print (list1)
#     if list1 > n:
#         return True
#     else:
#         return False
#
# #Uncomment the line below when your function is done
# print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))


# Write your function here
# def middle_element(lst):
#     lst_len = int(len(lst)/2)
#     lst_len1 = int(len(lst)/2)-1
#     if (lst_len % 2) == 0:
#         return lst_len
#     else:
#         return lst_len1
#
# #Uncomment the line below when your function is done
# print(middle_element([5, 2, -10, -4, 4, 5]))

# def middle_element(lst):
#   if len(lst) % 2 == 0:
#     sum = lst[int(len(lst)/2)] + lst[int(len(lst)/2) - 1]
#     return sum / 2
#   else:
#     return lst[int(len(lst)/2)]
#
# #Uncomment the line below when your function is done
# print(middle_element([5, 2, -10, -4, 4, 5]))


# Write your function here
# def append_sum(lst):
#     lst1 = lst[-1] + lst[-2]
#
#     #print(lst1)
#     lst.append(lst1)
#     lst2 = lst[-1] + lst[-2]
#     lst.append(lst2)
#     #print(lst)
#     lst3 = lst[-1] + lst[-2]
#     lst.append(lst3)
#     return lst
#     #print(lst)
#
# #Uncomment the line below when your function is done
# print(append_sum([1, 1, 2]))
#
#
# def append_sum(lst):
#   lst.append(lst[-1] + lst[-2])
#   lst.append(lst[-1] + lst[-2])
#   lst.append(lst[-1] + lst[-2])
#   return lst
#
# #Uncomment the line below when your function is done
# print(append_sum([1, 1, 2]))


# def larger_list(lst1, lst2):
#     if len(lst1) >= len(lst2):
#         return lst1[-1]
#     else:
#         return lst2[-1]
#
# # Uncomment the line below when your function is done
# print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))


# def combine_sort(lst1, lst2):
#     newlst = lst1 + lst2
#     return sorted(newlst)
#     #Uncomment the line below when your function is done
# print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))


# Write your function here
# def append_size(lst):
#     new_lst = len(lst)
#     lst.append(new_lst)
#     return lst
#
# #Uncomment the line below when your function is done
# print(append_size([23, 42, 108]))


# Write your function here
# def every_three_nums(start):
#   return list(range(start, 101, 3))
#
# #Uncomment the line below when your function is done
# print(every_three_nums(91))


# my_favorite_numbers = [4, 8, 15, 16, 42]
#
# for number in my_favorite_numbers:
#   my_favorite_numbers.append(1)

# students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
# students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]
#
# for student in students_period_A:
#   students_period_B.append(student)
#   print(student)
#   print(students_period_B)


# dog_breeds_available_for_adoption = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']
# for i in dog_breeds_available_for_adoption:
#   print(i)
#   if i == 'dalmatian':
#   	break
# print("They have the dog I want!")
#
# ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]
# for i in ages:
#   if i < 21:
#     continue
#   print(i)


# dog_breeds = ['bulldog', 'dalmation', 'shihtzu', 'poodle', 'collie']
#
# index = 0
# while index < len(dog_breeds):
#   print(dog_breeds[index])
#   index += 1

# all_students = ["Alex", "Briana", "Cheri", "Daniele", "Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]
# students_in_poetry = []
#
# while len(students_in_poetry) < 6:
#   new_student = all_students.pop()
#   students_in_poetry.append(new_student)
#   print(students_in_poetry)

### Nested Loops

# heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
# can_ride_coaster = []
# for element in heights:

#     if element >= 161:
#      can_ride_coaster.append(element)
# print(can_ride_coaster)

# my_upvotes = [192, 34, 22, 175, 75, 101, 97]
# updated_upvotes = [vote_value + 100 for vote_value in my_upvotes]
# print (vote_value)


# celsius = [0, 10, 15, 32, -5, 27, 3]
# #temperature_in_fahrenheit =
# fahrenheit =[temp * 9/5 + 32 for temp in celsius]
# print(fahrenheit)

# single_digits = range(0, 10)
# for i in single_digits:
#     print(i)

# Square
# single_digits = range(0, 10)
# squares = [i ** 2 for i in single_digits]
# print(squares)
#
# #cube
# single_digits = range(0, 10)
# #squares = [i ** 2 for i in single_digits]
# cubes = [oper ** 3 for oper in single_digits]
# print(cubes)

# hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
#
# prices = [30, 25, 40, 20, 20, 35, 50, 35]
#
# last_week = [2, 3, 5, 8, 4, 4, 6, 2]
# total_price = 0
# for price in prices:
#     total_price += price
# print(total_price)
# average_price =  total_price / len(prices)
# #print(average_price)
# new_prices =[new_price - 5 for new_price in prices]
# #print(new_prices)
# total_revenue = 0
# for i in range(len(hairstyles)):
#   total_revenue += prices[i] * last_week[i]
#   #print(total_revenue)
# average_daily_revenue =  total_revenue/7
# print(average_daily_revenue)
# cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if new_prices[i] < 30]
# print(cuts_under_30)

# numbers = [1, 1, 2, 3]
# for number in numbers:
#   if number % 2 == 0:
#     break
#   print(number)

# drink_choices = ["coffee", "tea", "water", "juice", "soda"]
# for drink in drink_choices:
#   print(drink)


# numbers = [1, 1, 2, 3]
# for number in numbers:
#   if number % 2 == 0:
#     continue
#   print(number)

# def divisible_by_ten(nums):
#   count = 0
#   for number in nums:
#     if (number % 10 == 0):
#       count += 1
#   return count
#
# #Uncomment the line below when your function is done
# print(divisible_by_ten([20, 25, 30, 35, 40]))

# def add_greetings(names):
#   new_list = []
#   for name in names:
#     new_list.append("Hello, " + name)
#   return new_list
#
# #Uncomment the line below when your function is done
# print(add_greetings(["Owen", "Max", "Sophie"]))

# def delete_starting_evens(lst):
#   while (len(lst) > 0 and lst[0] % 2 == 0):
#     lst = lst[1:]
#   return lst
#
# #Uncomment the lines below when your function is done
# print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
# print(delete_starting_evens([4, 8, 10]))

# def odd_indices(lst):
#     new_list = []
#     for index in range(1, len(lst), 2):
#         new_list.append(lst[index])
#     return new_list
# #Uncomment the line below when your function is done
# print(odd_indices([4, 3, 7, 10, 11, -2]))

# power = 2**3
# print (power)


# def exponents(bases, powers):
#   new_lst = []
#   for base in bases:
#     for power in powers:
#       new_lst.append(base ** power)
#   return new_lst
#
# #Uncomment the line below when your function is done
# print(exponents([2, 3, 4], [1, 2, 3]))
#
# ### OR THE SAME THING
#

#### Second Example of what above
# import math
# def exponents(bases, powers):
#     new_list = []
#     for base in bases:
#         for power in powers:
#             new_list.append(math.pow(base, power))
#     return new_list
#
# # Uncomment the line below when your function is done
# print(exponents([2, 3, 4], [1, 2, 3]))

# New Loop
"""
Create a function named larger_sum() that takes two lists of numbers as parameters named lst1 and lst2.

The function should return the list whose elements sum to the greater number. If the sum of the elements of each list are equal, return lst1.
"""

# def larger_sum(lst1, lst2):
#     new_lst1 = 0
#     new_lst2 = 0
#     for i in lst1:
#         new_lst1 += i
#     for b in lst2:
#         new_lst2 += b
#     if new_lst1 >= new_lst2:
#         return new_lst1
#     else:
#         return new_lst2
#
# print(larger_sum([1, 9, 5], [2, 3, 7]))


# def over_nine_thousand(lst):
#     new_list = 0
#     if lst == 0:
#         return 0
#     for i in lst:
#         new_list += i
#         if new_list > 9000:
#             break
#     return new_list
#
#
# #Uncomment the line below when your function is done
# print(over_nine_thousand([8000, 900, 120, 5000]))

# def max_num(nums):
#     new = max(nums)
#     return new
# # Uncomment the line below when your function is done
# print(max_num([50, -10, 0, 75, 20]))
#
# ###Max example
# num = [1, 3, 2, 8, 5, 10, 6]
# print('Maximum is:', max(num))


"""
Create a function named max_num() that takes a list of numbers named nums as a parameter.

The function should return the largest number in nums
"""
# def max_num(nums):
#     maximum = nums[0]
#     for i in nums:
#         if i > maximum:
#             maximum = i
#     return maximum
# # Uncomment the line below when your function is done
# print(max_num([50, -10, 0,200,  75, 20,105]))
"""
Write a function named same_values() that takes two lists of numbers of equal size as parameters.

The function should return a list of the indices where the values were equal in lst1 and lst2.

For example, the following code should return [0, 2, 3]
"""

# def same_values(lst1, lst2):
#   new_lst = []
#   for index in range(len(lst1)):
#     if lst1[index] == lst2[index]:
#       new_lst.append(index)
#   return new_lst
#
# #Uncomment the line below when your function is done
# print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

"""
Create a function named reversed_list() that takes two lists of the same size as parameters named lst1 and lst2.

The function should return True if lst1 is the same as lst2 reversed. The function should return False otherwise.

For example, reversed_list([1, 2, 3], [3, 2, 1]) should return True.
"""
# def reversed_list(lst1, lst2):
#     #lst1.reverse()
#     lst1 = lst1[::-1]
#     if lst1 == lst2:
#         return True
#     else:
#        return False
#
# #Uncomment the lines below when your function is done
# print(reversed_list([1, 2, 3], [3, 2, 1]))
# print(reversed_list([1, 5, 3], [3, 2, 1]))
#
# ### Their solution
#
# def reversed_list(lst1, lst2):
#   for index in range(len(lst1)):
#     if lst1[index] != lst2[len(lst2) - 1 - index]:
#       return False
#   return True
# #Uncomment the lines below when your function is done
# print(reversed_list([1, 2, 3], [3, 2, 1]))
# print(reversed_list([1, 5, 3], [3, 2, 1]))


### Strings

# first_name = "Reiko"
# short =first_name[:3-1]
# print (short)
# print (first_name[-3:])


# first_name = "Reiko"
# last_name = "Matsuki"
#
# def password_generator(first_name, last_name):
#   temp_password = first_name[len(first_name)-3:] + last_name[len(last_name)-3:]
#   return temp_password
#
# temp_password = password_generator(first_name, last_name)

"""
Use negative indices to find the the second to last character in company_motto. Save this to the variable second_to_last.
"""
company_motto = "Copeland's Corporate Company helps you capably cope with the constant cacophony of daily life"

# second_to_last = len(company_motto[-90:])
# second_to_last = company_motto[len(company_motto)-90:]
# print (second_to_last)


# def get_length(word):
#   counter = 0
#   for letter in word:
#     counter += 1
#   return counter

# favorite_fruit = "blueberry"
# counter = 0
# for character in favorite_fruit:
#   if character == "b":
#     counter = counter + 1
# print(counter)

# def letter_check(word, letter):
#   for character in word:
#     if character == word:
#       return True
#     #else:
#     return False
#
# print (letter_check("word", "word"))
#
# def contains(big_string, little_string):
#   return little_string in big_string
#
# print (contains("big_string", "little_string"))

### How to find common letter

# def common_letters(string_one, string_two):
#   a = []
#   for i in string_one:
#     if i in string_two and i not in a:
#     	a.append(i)
#   return(a)
#
#
# def common_letters(string_one, string_two):
#   common_letters = []
#   for letter in string_one:
#     if letter in string_two:
#       if letter not in common_letters:
#         common_letters.append(letter)
#   return common_letters


# def common_letters(string_one, string_two):
#   letter =[]
#   for i in string_one:
#     if i in string_two and i not in letter:
#       letter.append(i)
#   return(letter)
# print(common_letters('manhattan', 'san francisco'))


# def username_generator(first_name, last_name):
#
#     usename = first_name + last_name
#     if len(first_name) < 3 and len(last_name) < 4:
#       return first_name + last_name
#     else:
#       #return first_name[:3] + last_name[:4]
#       return usename
#
# print(username_generator("Mike", "Popovich"))


# def username_generator(first_name, last_name):
#     username = first_name + last_name
#     username2 = first_name[:5] + last_name[:5]
#
#     if len(first_name) < 3 and len(last_name) < 4:
#       return username
#     else:
#       return username2
#
#
# print(username_generator("Mik", "Popo"))


"""
Inside password_generator create a for loop that iterates through the indices username by going from 0 to len(username).

To shift the letters right, at each letter the for loop should add the previous letter to the string password.
"""

# def password_generator(user_name):
#   password = ""
#   for i in range(0, len(user_name)):
#     print (i)
#     password += user_name[i-1]
#   return password
#   #print (i)
#
#
# print (password_generator("inkPopap"))


# cool_fruit = "watermelon"
# water = cool_fruit[len(cool_fruit) - 2]
# print (water)

# good_fruit = "Raspberry"

### Split

# authors = "Audre Lorde, William Carlos Williams, Gabriela Mistral, Jean Toomer, An Qi, Walt Whitman, Shel Silverstein, Carmen Boullosa, Kamala Suraiyya, Langston Hughes, Adrienne Rich, Nikki Giovanni"
#
# author_names = authors.split(",")
# #print(author_names)
# last_name =[]
# #for index in range(len(author_names)):
# for index in author_names:
#   last_name.append(index.split()[-1])
#   print (last_name)


#### Split new line \n Split Tab \t

# spring_storm_text = \
# """The sky has given over
# its bitterness.
# Out of the dark change
# all day long
# rain falls and falls
# as if it would never end.
# Still the snow keeps
# its hold on the ground.
# But water, water
# from a thousand runnels!
# It collects swiftly,
# dappled with black
# cuts a way for itself
# through green ice in the gutters.
# Drop after drop it falls
# from the withered grass-stems
# of the overhanging embankment."""
#
# spring_storm_lines =spring_storm_text.split('\n')


# love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms',
#                     '           like flowering mines    ', '\n', '   to conquer me home.    ']
#
# love_maybe_lines_stripped = []
# for line in love_maybe_lines:
#   love_maybe_lines_stripped.append(line.strip())
# love_maybe_full = '\n'.join(love_maybe_lines_stripped)
#
# print(love_maybe_full)


### Replace

# toomer_bio = \
# # """
# # Nathan Pinchback Tomer, who adopted the name Jean Tomer early in his literary career, was born in Washington, D.C. in 1894. Jean is the son of Nathan Tomer was a mixed-race freedman, born into slavery in 1839 in Chatham County, North Carolina. Jean Tomer is most well known for his first book Cane, which vividly portrays the life of African-Americans in southern farmlands.
# # """
# # toomer_bio_fixed = toomer_bio.replace('Tomer','Toomer')
# # print(toomer_bio_fixed)

###Find

# god_wills_it_line_one = "The very earth will disown you"
#
# disown_placement = god_wills_it_line_one.find('disown')
# print(disown_placement)

### Forman
#
# def favorite_song_statement(song, artist):
#   return "My favorite song is {} by {}.".format(song, artist)

#
# def poem_title_card(poet, title):
#     return "The poem {} is written by {}".format(poet, title)
#
#
# print(poem_title_card("I Hear America Singing", "Walt Whitman"))
#
#
# def poem_title_card(poet, title):
#   poem_desc = "The poem \"{}\" is written by {}".format(title, poet)
#   return poem_desc


# def poem_description(publishing_date, author, title, original_work):
#   poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date=publishing_date, author=author, title=title, original_work=original_work)
#   return poem_desc
# my_beard_description = poem_description("1974", "Shel Silverstein", "My Beard", "Where the Sidewalk Ends")
#
# print(my_beard_description)


# .upper(), .title(), and .lower() adjust the casing of your string.
# .split() takes a string and creates a list of substrings.
# .join() takes a list of strings and creates a string.
# .strip() cleans off whitespace, or other noise from the beginning and end of a string.
# .replace() replaces all instances of a character/string in a string with another character/string.
# .find() searches a string for a character/string and returns the index value that c
# haracter/string is found at.
# .format() and f-strings allow you to interpolate a string with variables.


# highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"
#
# #print(highlighted_poems)
# highlighted_poems_list = highlighted_poems.split(",")
# #print(highlighted_poems_list)
#
# highlighted_poems_stripped = []
# for index in highlighted_poems_list:
#     highlighted_poems_stripped.append(index.strip())
# #print(highlighted_poems_stripped)
# highlighted_poems_details =[]
# for poem in highlighted_poems_stripped:
#   highlighted_poems_details.append(poem.split(":"))
# print (highlighted_poems_details)
# titles =[]
# poets =[]
# dates =[]
# for j in highlighted_poems_details:
#     titles.append(j[0])
#     poets.append(j[1])
#     dates.append(j[2])
# print(titles)
# print(poets)
# print(dates)


daily_sales = \
    """Edith Mcbride   ;,;$1.21   ;,;   white ;,; 
09/15/17   ,Herbert Tran   ;,;   $7.29;,; 
white&blue;,;   09/15/17 ,Paul Clarke ;,;$12.52 
;,;   white&blue ;,; 09/15/17 ,Lucille Caldwell   
;,;   $5.13   ;,; white   ;,; 09/15/17,
Eduardo George   ;,;$20.39;,; white&yellow 
;,;09/15/17   ,   Danny Mclaughlin;,;$30.82;,;   
purple ;,;09/15/17 ,Stacy Vargas;,; $1.85   ;,; 
purple&yellow ;,;09/15/17,   Shaun Brock;,; 
$17.98;,;purple&yellow ;,; 09/15/17 , 
Erick Harper ;,;$17.41;,; blue ;,; 09/15/17, 
Michelle Howell ;,;$28.59;,; blue;,;   09/15/17   , 
Carroll Boyd;,; $14.51;,;   purple&blue   ;,;   
09/15/17   , Teresa Carter   ;,; $19.64 ;,; 
white;,;09/15/17   ,   Jacob Kennedy ;,; $11.40   
;,; white&red   ;,; 09/15/17, Craig Chambers;,; 
$8.79 ;,; white&blue&red   ;,;09/15/17   , Peggy Bell;,; $8.65 ;,;blue   ;,; 09/15/17,   Kenneth Cunningham ;,;   $10.53;,;   green&blue   ;,; 
09/15/17   ,   Marvin Morgan;,;   $16.49;,; 
green&blue&red   ;,;   09/15/17 ,Marjorie Russell 
;,; $6.55 ;,;   green&blue&red;,;   09/15/17 ,
Israel Cummings;,;   $11.86   ;,;black;,;  
09/15/17,   June Doyle   ;,;   $22.29 ;,;  
black&yellow ;,;09/15/17 , Jaime Buchanan   ;,;   
$8.35;,;   white&black&yellow   ;,;   09/15/17,   
Rhonda Farmer;,;$2.91 ;,;   white&black&yellow   
;,;09/15/17, Darren Mckenzie ;,;$22.94;,;green 
;,;09/15/17,Rufus Malone;,;$4.70   ;,; green&yellow 
;,; 09/15/17   ,Hubert Miles;,;   $3.59   
;,;green&yellow&blue;,;   09/15/17   , Joseph Bridges  ;,;$5.66   ;,; green&yellow&purple&blue 
;,;   09/15/17 , Sergio Murphy   ;,;$17.51   ;,;   
black   ;,;   09/15/17 , Audrey Ferguson ;,; 
$5.54;,;black&blue   ;,;09/15/17 ,Edna Williams ;,; 
$17.13;,; black&blue;,;   09/15/17,   Randy Fleming;,;   $21.13 ;,;black ;,;09/15/17 ,Elisa Hart;,; $0.35   ;,; black&purple;,;   09/15/17   ,
Ernesto Hunt ;,; $13.91   ;,;   black&purple ;,;   
09/15/17,   Shannon Chavez   ;,;$19.26   ;,; 
yellow;,; 09/15/17   , Sammy Cain;,; $5.45;,;   
yellow&red ;,;09/15/17 ,   Steven Reeves ;,;$5.50   
;,;   yellow;,;   09/15/17, Ruben Jones   ;,; 
$14.56 ;,;   yellow&blue;,;09/15/17 , Essie Hansen;,;   $7.33   ;,;   yellow&blue&red
;,; 09/15/17   ,   Rene Hardy   ;,; $20.22   ;,; 
black ;,;   09/15/17 ,   Lucy Snyder   ;,; $8.67   
;,;black&red  ;,; 09/15/17 ,Dallas Obrien ;,;   
$8.31;,;   black&red ;,;   09/15/17,   Stacey Payne 
;,;   $15.70   ;,;   white&black&red ;,;09/15/17   
,   Tanya Cox   ;,;   $6.74   ;,;yellow   ;,; 
09/15/17 , Melody Moran ;,;   $30.84   
;,;yellow&black;,;   09/15/17 , Louise Becker   ;,; 
$12.31 ;,; green&yellow&black;,;   09/15/17 ,
Ryan Webster;,;$2.94 ;,; yellow ;,; 09/15/17 
,Justin Blake ;,; $22.46   ;,;white&yellow ;,;   
09/15/17,   Beverly Baldwin ;,;   $6.60;,;   
white&yellow&black ;,;09/15/17   ,   Dale Brady   
;,;   $6.27 ;,; yellow   ;,;09/15/17 ,Guadalupe Potter ;,;$21.12   ;,; yellow;,; 09/15/17   , 
Desiree Butler ;,;$2.10   ;,;white;,; 09/15/17  
,Sonja Barnett ;,; $14.22 ;,;white&black;,;   
09/15/17, Angelica Garza;,;$11.60;,;white&black   
;,;   09/15/17   ,   Jamie Welch   ;,; $25.27   ;,; 
white&black&red ;,;09/15/17   ,   Rex Hudson   
;,;$8.26;,;   purple;,; 09/15/17 ,   Nadine Gibbs 
;,;   $30.80 ;,;   purple&yellow   ;,; 09/15/17   , 
Hannah Pratt;,;   $22.61   ;,;   purple&yellow   
;,;09/15/17,Gayle Richards;,;$22.19 ;,; 
green&purple&yellow ;,;09/15/17   ,Stanley Holland 
;,; $7.47   ;,; red ;,; 09/15/17 , Anna Dean;,;$5.49 ;,; yellow&red ;,;   09/15/17   ,
Terrance Saunders ;,;   $23.70  ;,;green&yellow&red 
;,; 09/15/17 ,   Brandi Zimmerman ;,; $26.66 ;,; 
red   ;,;09/15/17 ,Guadalupe Freeman ;,; $25.95;,; 
green&red ;,;   09/15/17   ,Irving Patterson 
;,;$19.55 ;,; green&white&red ;,;   09/15/17 ,Karl Ross;,;   $15.68;,;   white ;,;   09/15/17 , Brandy Cortez ;,;$23.57;,;   white&red   ;,;09/15/17, 
Mamie Riley   ;,;$29.32;,; purple;,;09/15/17 ,Mike Thornton   ;,; $26.44 ;,;   purple   ;,; 09/15/17, 
Jamie Vaughn   ;,; $17.24;,;green ;,; 09/15/17   , 
Noah Day ;,;   $8.49   ;,;green   ;,;09/15/17   
,Josephine Keller ;,;$13.10 ;,;green;,;   09/15/17 ,   Tracey Wolfe;,;$20.39 ;,; red   ;,; 09/15/17 ,
Ignacio Parks;,;$14.70   ;,; white&red ;,;09/15/17 
, Beatrice Newman ;,;$22.45   ;,;white&purple&red 
;,;   09/15/17, Andre Norris   ;,;   $28.46   ;,;   
red;,;   09/15/17 ,   Albert Lewis ;,; $23.89;,;   
black&red;,; 09/15/17,   Javier Bailey   ;,;   
$24.49   ;,; black&red ;,; 09/15/17   , Everett Lyons ;,;$1.81;,;   black&red ;,; 09/15/17 ,   
Abraham Maxwell;,; $6.81   ;,;green;,;   09/15/17   
,   Traci Craig ;,;$0.65;,; green&yellow;,; 
09/15/17 , Jeffrey Jenkins   ;,;$26.45;,; 
green&yellow&blue   ;,;   09/15/17,   Merle Wilson 
;,;   $7.69 ;,; purple;,; 09/15/17,Janis Franklin   
;,;$8.74   ;,; purple&black   ;,;09/15/17 ,  
Leonard Guerrero ;,;   $1.86   ;,;yellow  
;,;09/15/17,Lana Sanchez;,;$14.75   ;,; yellow;,;   
09/15/17   ,Donna Ball ;,; $28.10  ;,; 
yellow&blue;,;   09/15/17   , Terrell Barber   ;,; 
$9.91   ;,; green ;,;09/15/17   ,Jody Flores;,; 
$16.34 ;,; green ;,;   09/15/17,   Daryl Herrera 
;,;$27.57;,; white;,;   09/15/17   , Miguel Mcguire;,;$5.25;,; white&blue   ;,;   09/15/17 ,   
Rogelio Gonzalez;,; $9.51;,;   white&black&blue   
;,;   09/15/17   ,   Lora Hammond ;,;$20.56 ;,; 
green;,;   09/15/17,Owen Ward;,; $21.64   ;,;   
green&yellow;,;09/15/17,Malcolm Morales ;,;   
$24.99   ;,;   green&yellow&black;,; 09/15/17 ,   
Eric Mcdaniel ;,;$29.70;,; green ;,; 09/15/17 
,Madeline Estrada;,;   $15.52;,;green;,;   09/15/17 
, Leticia Manning;,;$15.70 ;,; green&purple;,; 
09/15/17 ,   Mario Wallace ;,; $12.36 ;,;green ;,; 
09/15/17,Lewis Glover;,;   $13.66   ;,;   
green&white;,;09/15/17,   Gail Phelps   ;,;$30.52   
;,; green&white&blue   ;,; 09/15/17 , Myrtle Morris 
;,;   $22.66   ;,; green&white&blue;,;09/15/17"""

# daily_sales_replaced = daily_sales.replace(';,;','*')
# #print(daily_sales_replaced)
# daily_transactions = daily_sales_replaced.split(',')
# #print(daily_transactions)
# daily_transactions_split = []
# for transaction in daily_transactions:
#     daily_transactions_split.append(transaction.split('*'))
# #print (daily_transactions_split)
#
# transactions_clean = []
# for word in daily_transactions_split:
#     transaction_clean = []
#     for data_point in word:
#         transaction_clean.append(data_point.replace("\n","").strip(" "))
#         transactions_clean.append(transaction_clean)
# #print (transactions_clean)
#
#
# customers =[]
# sales = []
# thread_sold = []
# for data in transactions_clean:
#     customers.append(data[0])
#     sales.append(data[1])
#     thread_sold.append(data[2])
# # print (customers)
# #print (sales)
# # print (thread_sold)
#
#
# total_sales = 0
# for i in sales:
#     total_sales += float(i.strip("$"))
# # print(total_sales)
#
#
# #print(thread_sold)
# thread_sold_split = []
# for sale in thread_sold:
#     for color in sale.split('&'):
#         thread_sold_split.append(color)
# #print(thread_sold_split)
#
# def color_count(color):### NOT WORKING
#     color_total = 0
#     for thread_color in thread_sold_split:
#         if color == thread_color:
#             color_total += 1
#         return color_total
# #print (color_count('white'))
#
#
# colors = ['red','yellow','green','white','black','blue','purple']
#
# for color in colors:
#     print (
#         "Thread Shed sold {0} threads of {1} thread today ".format(color_count(color), color)
#     )


# total_sales += float(i.strip())

#open("email_one.txt", "r").read()


# with working_directory("~/censor_dispenser/"):
#     subprocess.call("ls")


#def cd_to_folder():
    #os.chdir("/Users/jshakespeare/Documents/Python/censor_dispenser")
    #subprocess.call("ls")



#     email_one = open("email_one.txt", "r").read()
#     for word in email_one:
#             #re.match('we', 'we')
#
#             print(word)
# cd_to_folder()





# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained
# in and the .read() method is allowing us to save their contexts to the following variables:
# os.chdir("/Users/jshakespeare/Documents/Python/censor_dispenser")
# email_one = open("email_one.txt", "r").read()
# email_two = open("email_two.txt", "r").read()
# email_three = open("email_three.txt", "r").read()
# email_four = open("email_four.txt", "r").read()



# def censor_one(input_text, censor):
#   censored_item = ""
#   for x in range(0,len(censor)):
#     if censor[x] == " ":
#       censored_item = censored_item + " "
#     else:
#     	censored_item = censored_item + "X"
#   return input_text.replace(censor, censored_item)
#
# print(censor_one(email_one, "learning algorithm"))

#proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself", "Helena"]
#
# def censor_two(input_text, censored_list):
#   for word in censored_list:
#     censored_word = ""
#     for x in range(0,len(word)):
#       if word[x] == " ":
#         censored_word = censored_word + " "
#       else:
#         censored_word = censored_word + "X"
#     input_text = input_text.replace(word, censored_word)
#   return input_text
#
# print(censor_two(email_two, proprietary_terms))







# negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]
#
# def censor_three(input_text, censored_list, negative_words):
#   input_text_words = []
#   for x in input_text.split(" "):
#     #print x # will split on space and print each word new line
#     x1 = x.split("\n")
#     #print x1 # will split each word in the list
#     for word in x1:
#       input_text_words.append(word)
#   #print (input_text_words)
#   for i in range(0,len(input_text_words)):
#     if (input_text_words[i] in censored_list) == True:
#       word_clean = input_text_words[i]
#       censored_word = ""
#       for x in range(0,len(word_clean)):
#         censored_word = censored_word + "X"
#       input_text_words[i] = input_text_words[i].replace(word_clean, censored_word)
#     count = 0
#     for i in range(0,len(input_text_words)):
#       if (input_text_words[i] in negative_words) == True:
#         count += 1
#         if count > 2:
#           word_clean = input_text_words[i]
#           for x in word_clean:
#             word_clean = word_clean.strip(x)
#           censored_word = ""
#           for x in range(0,len(word_clean)):
#             censored_word = censored_word + "X"
#           input_text_words[i] = input_text_words[i].replace(word_clean, censored_word)
#   return " ".join(input_text_words)
#
# print(censor_three(email_three, proprietary_terms, negative_words))

# punctuation = [",", "!", "?", ".", "%", "/", "(", ")"]
#
# def censor_four(input_text, censored_list):
#   input_text_words = []
#   for x in input_text.split(" "):
#     x1 = x.split("\n")
#     for word in x1:
#       input_text_words.append(word)
#   for i in range(0,len(input_text_words)):
#     checked_word = input_text_words[i].lower()
#     for x in punctuation:
#       checked_word = checked_word.strip(x)
#     if checked_word in censored_list:
#
#       # Censoring the targeted word
#       word_clean = input_text_words[i]
#       censored_word = ""
#       for x in punctuation:
#         word_clean = word_clean.strip(x)
#       for x in range(0,len(word_clean)):
#         censored_word = censored_word + "X"
#       input_text_words[i] = input_text_words[i].replace(word_clean, censored_word)
#
#       # Censoring the word before the targeted word
#       word_before = input_text_words[i-1]
#       for x in punctuation:
#         word_before = word_before.strip(x)
#       censored_word_before = ""
#       for x in range(0,len(word_before)):
#         censored_word_before = censored_word_before + "X"
#       input_text_words[i-1] = input_text_words[i-1].replace(word_before, censored_word_before)
#
#       # Censoring the word after the targeted word
#       word_after = input_text_words[i+1]
#       for x in punctuation:
#         word_after = word_after.strip(x)
#       censored_word_after = ""
#       for x in range(0,len(word_after)):
#         censored_word_after = censored_word_after + "X"
#       input_text_words[i+1] = input_text_words[i+1].replace(word_after, censored_word_after)
#   return " ".join(input_text_words)
#
# censor_all = proprietary_terms + negative_words
#
# print(censor_four(email_four, censor_all))

#========================================

#letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Write your unique_english_letters function here:

#def unique_english_letters(word):

"""Solution One"""
#     number = 0
#     for letter in letters:
#         if letter in word:
#             number += 1
#     return number
# print(unique_english_letters("mississippi"))
# #should print 4
# print(unique_english_letters("Apple"))
# # should print 4
"""Solution Two"""

#     uniques = []
#     for letter in word:
#         if letter in letters and not letter in uniques:
#             uniques.append(letter)
#     return len(uniques)
# print(unique_english_letters("mississippi"))
# # #should print 4
# print(unique_english_letters("Apple"))
# # # should print 4
#=====================================

# Write your count_char_x function here:
# def count_char_x(word, x):
#     num = 0
#     for letter in word:
#         if letter == x:
#             num += 1
#            #num.append(letter)
#     return num

# Uncomment these function calls to test your tip function:
#print(count_char_x("mississippi", "s"))
# should print 4
#print(count_char_x("mississippi", "m"))
# should print 1


# print(count_multi_char_x("mississippi", "iss"))

# def count_multi_char_x(word, x):
#     splits = word.split(x)
#     print splits
#     return(len(splits)-1)
#
# print(count_multi_char_x("mississippi", "iss"))
# print(count_multi_char_x("apple", "pp"))


# def substring_between_letters(word, start, end):
#     start = word.find(start)
#     end = word.find(end)
#     if start and end != -1:
#         #print(word[start + 1 : end])
#         return word[start + 1: end]
#     else:
#         return word
#
# print(substring_between_letters("apple", "p", "e"))
# # should print "pl"
# print(substring_between_letters("apple", "p", "c"))
# # should print "apple"


# def x_length_words(sentence, x):
#     count = 0
#     arry = sentence.split(' ')
#     for word in arry:
#         for letter in word:
#             if letter >= x:
#                 count += 1
#         if count >= x:
#             return True
#         else:
#             return False
#
#
# print(x_length_words("i like apples", 2))
# # should print False
# print(x_length_words("he likes apples", 2))
# # should print True
# print(x_length_words("I go home", 2))

"""Write a function called check_for_name that takes two strings as parameters named sentence and name. The function 
should return True if name appears in sentence in all lowercase letters, all uppercase letters, or with any mix of 
uppercase and lowercase letters. The function should return False otherwise.

For example, the following three calls should all return True:"""
# def check_for_name(sentence, name):
#     return name.lower() in sentence.lower()
#
#
# print(check_for_name("My name is Jamie", "Jamie"))
# # should print True
# print(check_for_name("My name is jamie", "Jamie"))
# # should print True
# print(check_for_name("My name is Samantha", "Jamie"))
# # should print False

"""Create a function named every_other_letter that takes a string named word as a parameter. The function should return
 a string containing every other letter in word."""

# def every_other_letter(word):
#     every_second_letter = ''
#     for i in range(0, len(word), 2):
#         every_second_letter += word[i]
#     return every_second_letter
#
#
#
# print(every_other_letter("Codecademy"))
# # should print Cdcdm
# print(every_other_letter("Hello world!"))
# # should print Hlowrd
# print(every_other_letter(""))
# # should print


"""Write a function named reverse_string that has a string named word as a parameter. The function should return word in reverse."""

# def reverse_string(word):
#     return word[::-1]
#
# print(reverse_string("Codecademy"))
# # should print ymedacedoC
# print(reverse_string("Hello world!"))
# # should print !dlrow olleH
# print(reverse_string(""))
# # should print


# def make_spoonerism(word1, word2):
#     if word1 == word1[0]:
#         if word2 == word2[0]:
#             return word2 +' '+ word1
#     w1_first = word1[0]
#     w1_all = word1[1:]
#     w2_first = word2[0]
#     w2_all = word2[1:]
#     new_word1 = w1_first + w2_all
#     new_word2 = w2_first + w1_all
#     return   new_word2+' '+new_word1
#
#
#
# print(make_spoonerism("Codecademy", "Learn"))
# # should print Lodecademy Cearn
# print(make_spoonerism("Hello", "world!"))
# # should print wello Horld!
# print(make_spoonerism("a", "b"))
# # should print b a

""".
Create a function named add_exclamation that has one parameter named word. This function should add exclamation points
 to the end of word until word is 20 characters long. If word is already at least 20 characters long, just return word."""

# def add_exclamation(word):
#     while len(word) < 20:
#         word += '!'
#     return word
#
# ### 2nd Solution
# # def add_exclamation(word):
# #   word += "!"*(20-len(word))
# #   return word
#
#
# print(add_exclamation("Codecademy"))
# # should print Codecademy!!!!!!!!!!
# print(add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn



import random

# Create random_list below:
#
# random_list = [random.randint(1,101) for i in range(101)]
# # Create randomer_number below:
# randomer_number = random.choice(random_list)
# print(randomer_number)



# import codecademylib3_seaborn
# from matplotlib import pyplot as plt
# import random
### New task
# Add your code below:
#import codecademylib3_seaborn
# from matplotlib import pyplot as plt
# import random
#
# # Add your code below:
# numbers_a = range(1,13)
# numbers_b = random.sample(range(1000), 12)
# plt.plot(numbers_a, numbers_b)
# plt.show()



# from decimal import Decimal
#
# # Fix the floating point math below:
# two_decimal_points = Decimal('0.2') + Decimal('0.69')
# print(two_decimal_points)
#
#
# four_decimal_points = Decimal('0.53') * Decimal('0.65')
# print(four_decimal_points)


###Dictionary

# menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
# ###   Add a key by using syntax like:
# menu["newVal"] = 4
# print (menu)
#
# ### Update Dictionary
#
# menu.update({"supValu": 5, "kompot": 8})
# print (menu)
# #### Examples how to replace value
# oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
# oscar_winners["Supporting Actress"] = "Viola Davis"
# oscar_winners["Best Picture"] = "Moonlight"
# print(oscar_winners)


# drinks = ["espresso", "chai", "decaf", "drip"]
# caffeine = [64, 40, 0, 120]
# zipped_drinks = zip(drinks, caffeine)
#print(zipped_drinks)
# zipped_drinks = {key:value for key, value in zip(drinks, caffeine)}
# drinks_to_caffeine = {key:value for key, value in zipped_drinks}
# print(drinks_to_caffeine)


##### Antoer dictionary examples 

# songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
# playcounts = [78, 29, 44, 21, 89, 5]
#
# plays = {key:value for key, value in zip(songs, playcounts)}
# print(plays)
# plays["Purple Haze"] = 1
# plays["Respect"] = 94
# library = {"The Best Songs": plays, "Sunday Feelings": {}}
# print(library)


##### Try/Except to Get a Key
# key_to_check = "Landmark 81"
# try:
#   print(building_heights[key_to_check])
# except KeyError:
#   print("That key doesn't exist!")

#### Another Try Except example
  # caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120}
  # caffeine_level.update({"matcha": 30})
  # try:
  #     print(caffeine_level["matcha"])
  # except KeyError:
  #     print("Unknown Caffeine Level")


#### .get

# >>> building_heights.get('Shanghai Tower', 0)
# 632
# >>> building_heights.get('Mt Olympus', 0)
# 0
# >>> building_heights.get('Kilimanjaro', 'No Value')
# 'No Value'

###### Pop Key

# >>> raffle.pop(320291, "No Prize")
# "Gift Basket"
# >>> raffle
# {223842: "Teddy Bear", 872921: "Concert Tickets", 412123: "Necklace", 298787: "Pasta Maker"}
# >>> raffle.pop(100000, "No Prize")
# "No Prize"
# >>> raffle
# {223842: "Teddy Bear", 872921: "Concert Tickets", 412123: "Necklace", 298787: "Pasta Maker"}
# >>> raffle.pop(872921, "No Prize")
# "Concert Tickets"
# >>> raffle
# {223842: "Teddy Bear", 412123: "Necklace", 298787: "Pasta Maker"}

#### Anothr .pop() Example
# available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
# health_points = 20
# health_points += available_items.get("stamina grains")
# available_items.pop("stamina grains", 0)
# health_points += available_items.get("power stew", 0)
# available_items.pop("power stew", 0)
# health_points += available_items.get("mystic bread", 0)
# available_items.pop("mystic bread", 0)
# print (available_items)
# print (health_points)

### Get All Keys .key()

# test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}
#
# list = list(test_scores)
# print (list)
#
# for student in test_scores.keys():
#     print(student)



# user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
# num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}
# users = user_ids.keys()
# lessons = num_exercises.keys()
# print users


### Get All Values .value()

#test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}
#list = list(test_scores.keys())
# list = list(test_scores.values())
# print list
# for score_list in test_scores.values():
#   print(score_list)


### Exercise
# num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}
# total_exercises = 0
#
# for value in num_exercises.values():
#     total_exercises += value
# print (total_exercises)


# biggest_brands = {"Apple": 184, "Google": 141.7, "Microsoft": 80, "Coca-Cola": 69.7, "Amazon": 64.8}
#
# for company, value in biggest_brands.items():
#   print(company + " has a value of " + str(value) + " billion dollars. ")


# pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}
#
# for title, age in pct_women_in_occupation.items():
#     print ("Women make up " + str(age) + " percent of " +title+'.')


# letters = { "A": 10, "B": 20, "C": 30, "D": 4x0 }
#
# for data in letters.items():
#     print(data[0])
#     print(data[1])

#### FInal Test

# tarot = {1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"}
# spread = {}
# spread["past"] = tarot.pop(13)
# spread["present"] = tarot.pop(22)
# spread["future"] = tarot.pop(10)
# for key, value in spread.items():
#     print ('Your ' + key + ' is the ' + value + 'card.')

#
# ls = ['Mike', 'Bob', 'Vitaliy']
# ls.pop(1)
# print ls




#### Project
# letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
# points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
#
# letter_to_points = {key:value for key, value in zip(letters, points)}
# letter_to_points[" "] = 0
# #print (letter_to_points)
#
# def score_word(word):
#     point_total = 0
#     for letter in word:
#         point_total += letter_to_points.get(letter, 0) #.get() function only returns the value associated with the key
#     return point_total
#
# print(score_word('GOOD'))

#brownie_points = (score_word('BROWNIE'))
#print brownie_points
# player_to_words = {
#     'player1': ['BLUE', 'TENNIS', 'EXIT'],
#     'wordNerd': ['EARTH', 'EYES', 'MACHINE'],
#     'Lexi Con': ['ERASER', 'BELLY', 'HUSKY'],
#     'Prof Reader': ['ZAP',' COMA', 'PERIOD']
# }
# player_to_points = {}
# ###print(player_to_words.items())
# for player, words in player_to_words.items():
#     player_points = 0
#     for word in words:
#         player_to_words =+ score_word(word)
#     player_to_points[player] = player_points
#     print(player_to_points)

###End of the projecrt
##### KeyError
# combo_meals = {1: ["hamburger", "fries"], 2: ["hamburger", "fries", "soda"], 4: ["veggie burger", "salad", "soda"], 6: ["hot dog", "apple slices", "orange juice"]}
# print(combo_meals[2])


# inventory = {"iron spear": 12, "invisible knife": 30, "needle of ambition": 10, "stone glove": 20, "the peacemaker": 65, "demonslayer": 50}
#
# print(12 in inventory)
# print("iron spear" in inventory)


# oscars = {"Best Picture": "Moonlight", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
#
# for element in oscars:
#   print(element)


# inventory = {"iron spear": 12, "invisible knife": 30, "needle of ambition": 10, "stone glove": 20, "the peacemaker": 65, "demonslayer": 50}
#
# print("the peacemaker" in inventory)


# combo_meals = {1: ["hamburger", "fries"], 2: ["hamburger", "fries", "soda"], 4: ["veggie burger", "salad", "soda"], 6: ["hot dog", "apple slices", "orange juice"]}
# print(combo_meals.get(3, ["hamburger", "fries"])) #if 3 does not exist add value you need after it


# raffle = {223842: "Teddy Bear", 872921: "Concert Tickets", 320291: "Gift Basket", 412123: "Necklace", 298787: "Pasta Maker"}
#
# raffle.pop(561721, "No Value")
# print(raffle)


###### NEW CONTENT

""".
Create a function named add_ten that takes a dictionary with integer values named my_dictionary as a parameter. 
The function should add 10 to every value in my_dictionary and return my_dictionary"""

# def add_ten(my_dictionary):
#     #my_dictionaryy = 0
#     for key in my_dictionary.keys():
#         my_dictionary[key] += 10
#     return my_dictionary
#
# print(add_ten({1:5, 2:2, 3:3}))
# # should print {1:15, 2:12, 3:13}
# print(add_ten({10:1, 100:2, 1000:3}))
# should print {10:11, 100:12, 1000:13}


### Values That Are Keys

"""Write a function named max_key that takes a dictionary named my_dictionary as a parameter. 
The function should return the key associated with the largest value in the dictionary."""


# def max_key(my_dictionary):
#   for key, value in my_dictionary.items():
#     if value == max(my_dictionary.values()):
#       return key
#
# print(max_key({1:100, 2:1, 3:4, 4:10}))
# # should print 1
# print(max_key({"a":100, "b":10, "c":1000}))
# # should print "c"

#### Logn and nah way to go

# def max_key(my_dictionary):
#   lst1=[]
#   for keys in my_dictionary.keys():
#     lst1.append(my_dictionary[keys])
#   newlst=sorted(lst1)
#   print(newlst)
#   maxkey=newlst[-1]
#   print(maxkey)
#   for keys in my_dictionary.keys():
#     if my_dictionary[keys]==maxkey:
#       return keys
#
# print(max_key({1:100, 2:1, 3:4, 4:10}))
# # should print 1
# print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"


# def max_key(my_dictionary):
#     max_val = []
#     for value in my_dictionary.values():
#         max_val.append(value)
#         max_valnew = max(max_val)
#         #return max_valnew
#     for key in my_dictionary.keys():
#         if my_dictionary[key] == max_valnew:
#             return key
#
# print(max_key({1:100, 2:1, 3:4, 4:10}))

### Word Length Dict

"""Write a function named word_length_dictionary that takes a list of strings named words as a parameter. 
The function should return a dictionary of key/value pairs where every key is a word in words and every value is the length of that word."""

# def word_length_dictionary(words):
#     data = ['a','p','l','e','d','o','g','c','a','t','']
#     dict = {}
#     key = ""
#     for word in words:
#         # if word == '':
#         #    dict.update({'': 0})
#
#         key = ""
#         for letter in word:
#             if letter in data:
#                 key += letter
#                 value = len(key)
#         dict.update({key: value})
#     return dict
#
#
# #print(word_length_dictionary(["apple", "dog", "cat"]))
# # should print {"apple":5, "dog": 3, "cat":3}
# print(word_length_dictionary(["a", ""]))
# # should print {"a": 1, "": 0}


"""
Another solution 
word_lengths = {}
for word in words:
    word_lengths[word] = len(word)
return word_lengths
"""


### Shorter solution

# def word_length_dictionary(words):
#   return {word:len(word) for word in words}
#
# print(word_length_dictionary(["apple", "dog", "cat"]))
# # should print {"apple":5, "dog": 3, "cat":3}
# print(word_length_dictionary(["a", ""]))
# # should print {"a": 1, "": 0}


"""Write a function named frequency_dictionary that takes a list of elements named words as a parameter.
 The function should return a dictionary containing the frequency of each element in words."""


# def frequency_dictionary(words):
#     dict = {}
#     for word in words:
#         dict[word] = words.count(word)
#     return dict
#
#
# print(frequency_dictionary(["apple", "apple", "cat", 1]))
# # should print {"apple":2, "cat":1, 1:1}
# print(frequency_dictionary([0,0,0,0,0]))
# # should print {0:5}
#
#
# apple = ['one', 'one', 'two', 'three']
# total = apple.count('one')
# print(total)

### Unique Values
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

### Original Version

# def count_first_letter(names):
#   letters = {}
#   for key in names:
#     first_letter = key[0]
#     if first_letter not in letters:
#       letters[first_letter] = 0
#     letters[first_letter] += len(names[key])
#   return letters
#
# # Uncomment these function calls to test your  function:
# print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# # should print {"S": 4, "L": 3}
# print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# # should print {"S": 7}



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
# # should print 6

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
# # should print 6

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
# # should print {10:11, 100:12, 1000:13}


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

def max_key(my_dictionary):
    larg_val = 0




print(max_key({1: 100, 2: 1, 3: 4, 4: 10}))
# should print 1
print(max_key({"a": 100, "b": 10, "c": 1000}))
# should print "c"




