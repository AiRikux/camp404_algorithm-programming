# # condition
# a_key = input("Password: ")
# if a_key == "test123":
# 	print("You have successfully logged in")
# else:
# 	print("Please try again")
#
# # elif condition
# temperature = int(input("Temperature: "))
# if temperature <= 26:
# 	print("Its cloudy")
# elif temperature > 26:
# 	print("Its sunny")
# else:
# 	print("Weather unknown")
#
# # match case
# score = int(input("Your score: "))
# match score:
# 	case 1000:
# 		print("Awesome")
# 	case 500:
# 		print("Great")
# 	case _:
# 		print("What?")
#
# # for loop
# low = int(input("low number: "))
# high = int(input("high number: "))
# for item in range(low, high + 1):
# 	if item % 2 != 0:
# 		print(item, " ")
#
# # while loop
# x = 20
# while x > 0:
# 	if x % 3 == 0:
# 		print(x, " ")
# 	x = x - 1
#
#
# # simple function
# def hello():
# 	print("Hello!")
#
#
# # function with input
# # print text n times
# def hello2(text, n):
# 	for no in range(n):
# 		print(text)
#
#
# # function with result
# def area(a, b):
# 	result = a * b
# 	return result
#
#
# print(area(1, 2))
#
#
# # linear search
import random

search = int(input("Insert 1 - 10 to search: "))
# create a list of random integer
numbers = []
for r in list(range(1, 10)):
	numbers.append(random.randint(1, 10))
# # linear search the number from the list
# count = 0
# for i in numbers:
# 	if i == search:
# 		count += 1
# if count > 0:
# 	print("found it!")
# else:
# 	print("none here")
#
#
# from statistics import mode
# # sort list
# numbers.sort()
# count = 0
# # find middle value and position in list
# middle = mode(numbers)
# middle_index = numbers.index(middle)
# # if the number we search is equal to the mode
# if search == middle:
# 	print(middle_index)
# # if the search is less than mode
# elif search < middle:
# 	for i in numbers[:middle_index]: # for the list up until the mode
# 		if i == search:
# 			count += 1
# elif search > middle:
# 	for i in numbers[middle_index:]: # for the list from the mode until the end
# 		if i == search:
# 			count += 1
# else: # unexpected situation
# 	print("Can't find")
#
# if count > 0:
# 	print("found it!")
# else:
# 	print("none here")
#
# Bubble Sort
# get the length of the list
n = len(numbers)
for i in list(range(n)):
	print(i)

