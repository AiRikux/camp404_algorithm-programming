# libraries
import random
from statistics import mode

# functions
# create a list of random integer


def make_numbers(no=10):
	numb = []
	for _ in list(range(1, no)):
		numb.append(random.randint(1, no))
	return numb


search = int(input("Insert 1 - 10 to search: "))

# linear search
print("")
print("LINEAR SEARCH")
# linear search the number from the list
numbers = make_numbers()
count = 0
for i in numbers:
	if i == search:
		count += 1
if count > 0:
	print("found it!")
else:
	print("none here")

# Binary Search
print("")
print("BINARY SEARCH")
numbers = make_numbers()
# sort list
numbers.sort()
count = 0
# find middle value and position in list
middle = mode(numbers)
middle_index = numbers.index(middle)
# if the number we search is equal to the mode
if search == middle:
	print(middle_index)
# if the search is less than mode
elif search < middle:
	for i in numbers[:middle_index]:  # for the list up until the mode
		if i == search:
			count += 1
elif search > middle:
	for i in numbers[middle_index:]:  # for the list from the mode until the end
		if i == search:
			count += 1
else:  # unexpected situation
	print("Can't find")

if count > 0:
	print("found it!")
else:
	print("none here")