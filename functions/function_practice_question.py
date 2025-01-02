""".................................function practice questions..............................."""       

#Write a function that takes a string and returns the number of characters in it.

def this_string(string):
    return len(string)

print(this_string("sudip"))




"""..............................................................................................."""


#Create a function that takes a list of numbers and returns a new list with each number squared.


def square_list(list_1):
    return [x**2 for x in list_1]

print(square_list([1,2,3,4,5]))




"""..............................................................................................."""


#Write a function that checks if a given number is prime.


def is_prime(num):
    if num<=1:
        return False
    for i in range (2,num):
        if num%i==0:
            return False
    return True

num=int(input("enter number: "))

print(is_prime(num))


"""..............................................................................................."""


#Define a function that takes a list and returns the largest element in the list.

def largest_element(list_1):
    return max(list_1)

print(largest_element([1,2,3,4,5]))


"""..............................................................................................."""



#Implement a function that calculates the sum of all even numbers in a given range.

def sum_of_even_numbers(start, end):
    return sum(x for x in range(start, end+1) if x%2==0)

print(sum_of_even_numbers(1,10))


"""................................................................................................"""


#Write a function that takes a dictionary and returns a list of its keys.


def keys_of_dict(dict_1):
    return list(dict_1.keys())

print(keys_of_dict({"type":"car", "brand":"honda", "electric":"False"}))


#Write a function that takes a dictionary and returns a list of its values.
def values_of_dict(dict_1):
    return list(dict_1.values())

print(values_of_dict({"type":"car", "brand":"honda", "electric":"False"}))


"""..............................................................................................."""



#Create a function that takes a string and returns the string with all vowels removed.


def remove_vowels_func(string_1):
    vowels="aeiouAEIOU"
    result=""
    for i in string_1:
        if i not in vowels:
            result=result+i
    return result

print(remove_vowels_func("the quick brown fox jumps over the lazy dog"))


"""..............................................................................................."""



#Write a function that takes a list of strings and returns the longest string in the list.

def longest_string_func(list_of_strings):
     return max(list_of_strings, key=len)

print(longest_string_func(["apple", "banana", "cherry", "date", "watermelon", "pineapple"]))


"""..............................................................................................."""




#Implement a function that takes a string and counts how many times each character appears in it.

def count_characters_func(string_1):
    this_string={}
    for i in string_1.lower().replace(" ",""):
        if i in this_string:
         this_string[i]+=1
        else:
            this_string[i]=1
    return this_string

print(count_characters_func("the quick brown fox jumps over the lazy dog"))



"""..........................................................................................................."""



#Write a function that accepts a list and returns a new list with duplicate elements removed.

def remove_duplicates_func(list_1):
    return list(set(list_1))

print(remove_duplicates_func([1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10]))


"""..........................................................................................................."""



#Create a function that takes a list of numbers and returns their average.

def average_func(list_1):
    return sum(list_1)/len(list_1)

print(average_func([1,2,3,4,5]))



"""........................................................................................................"""


#Write a function that accepts a string and a character and counts how many times the character appears in the string.

def count_character_func(string_1,character):
    return string_1.count(character)

print(count_character_func("the quick brown fox jumps over the lazy dog","o"))



"""........................................................................................................"""


#Define a function that reverses a list without using built-in reverse methods.

def reverse_list(list_1):
    return list(sorted(list_1,reverse=True))   

print(reverse_list([1,2,3,4,5]))


"""this code reverses the list by sorting it in descending order,
but this approach may not give the desired results in all scenarios
where you simply want to reverse the list's order"""



"""best method is"""


def reverse_list(list_1):
    return list_1[::-1]

print(reverse_list([1,2,3,4,5]))


"""........................................................................................................"""



#Write a function that takes two lists and returns their intersection.

def intersection_func(list_1, list_2):
    return list(set(list_1) .intersection (set(list_2)))

print(intersection_func([1,2,3,4,5], [4,5,6,7,8]))


"""........................................................................................................"""



#Implement a function that takes a string and returns the number of words in it.


def count_words_func(string_1):
    return len(string_1.split())

print(count_words_func("the quick brown fox jumps over the lazy dog"))




"""........................................................................................................"""



#Create a function that accepts a list of tuples and sorts them based on the second element of each tuple.

def sort_tuples_func(list_1):
    return sorted(list_1, key=lambda x: x[1])

print(sort_tuples_func([(1,0),(3,8),(5,2),(4,9),(9,1)]))



"""........................................................................................................"""



#Write a function that calculates the greatest common divisor (GCD) of two numbers.

def gcd_func(num_1, num_2):
    while num_2 != 0:
        num_1, num_2 = num_2, num_1 % num_2    #euclidean algorithm [gcd(a,b)=gcd(b,a%b)]
    return num_1


print(gcd_func(10,15))



"""........................................................................................................"""


#Implement a function that generates all permutations of a given string.

def permutations_func(string_1):
    pass













"""........................................................................................................"""


#Define a function that converts a given temperature from Celsius to Fahrenheit.


def celsius_to_fahrenheit(celsius):
    fahrenheit= (celsius * 9/5) + 32
    return fahrenheit

print(celsius_to_fahrenheit(98))



"""........................................................................................................"""


#Write a function that flattens a nested list into a single-level list.

def flatten_list_func(list_1):
    list_2=[]
    for i in list_1:
        list_2.extend(i)
    return list_2

print(flatten_list_func([[1,2,3], [4,5,6], [7,8,9]]))



    







