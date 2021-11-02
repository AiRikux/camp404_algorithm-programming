# libraries
import random
from statistics import mode

# functions
# create a list of random integer


def make_numbers(no=10):
	numb = []
	for _ in list(range(1, n)):
		numb.append(random.randint(1, no))
	return numb


# condition
a_key = input("Password: ")
if a_key == "test123":
	print("You have successfully logged in")
else:
	print("Please try again")

# elif condition
temperature = int(input("Temperature: "))
if temperature <= 26:
	print("Its cloudy")
elif temperature > 26:
	print("Its sunny")
else:
	print("Weather unknown")

# match case
score = int(input("Your score: "))
match score:
	case 1000:
		print("Awesome")
	case 500:
		print("Great")
	case _:
		print("What?")

# for loop
low = int(input("low number: "))
high = int(input("high number: "))
for item in range(low, high + 1):
	if item % 2 != 0:
		print(item, " ")

# while loop
x = 20
while x > 0:
	if x % 3 == 0:
		print(x, " ")
	x = x - 1


# simple function
def hello():
	print("Hello!")


# function with input
# print text n times
def hello2(text, no):
	for no in range(no):
		print(text)


# function with result
def area(a, b):
	result = a * b
	return result


print(area(1, 2))


# linear search
search = int(input("Insert 1 - 10 to search: "))
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

# Bubble Sort
numbers = make_numbers()
# try to sort it ascending
print(numbers)
# get the length of the list
n = len(numbers)
fixing = True
while fixing:
	fixing = False
	for i in list(range(n)):
		current = numbers[i]

		# make sure we don't go outside the list index
		if i != n-1:
			after = numbers[i+1]
		else:
			continue

		if current > after:
			print("Fixing....")
			# mark there is fixing
			fixing = True
			# switch places
			numbers[i] = after
			numbers[i+1] = current
			print(numbers)

# when fixing is False the loop will stop and give us the fixed result
print("Here is the result for Bubble Sort")
print(numbers)

# Selective Sort
# try to sort it ascending


numbers = make_numbers()
new_numbers = []
print(numbers, "------>", new_numbers)
while len(numbers) > 0:
	lowest = None
	lowest_index = None
	for i in list(range(len(numbers))):
		if lowest is None:
			lowest = numbers[i]
			lowest_index = i
		else:
			if numbers[i] < lowest:
				lowest = numbers[i]
				lowest_index = i
	new_numbers.append(numbers.pop(lowest_index))
	print(numbers, "------>", new_numbers)


# Insertion Sort
numbers = make_numbers()
print(numbers)
# start from a certain position
n = 0
yes = True
while yes:
	if n == 0:
		if numbers[n] > numbers[n+1]:
			print("Fixing...")
			# switch places
			current = numbers[n]
			after = numbers[n+1]
			numbers[n] = after
			numbers[n+1] = current
	elif n == len(numbers):
		yes = False
	else:
		current = numbers[n]
		for i in list(range(n)):
			versus = numbers[i]
			if current < versus:
				print("Fixing...")
				value = numbers.pop(n)
				numbers.insert(i, value)
				break
	print(f"With n={n} we get {numbers}")
	n += 1

print(f"Result is {numbers}")


# Merge Sort
numbers = make_numbers()
print(numbers)


def bubble_sort(numb):
	fixing = True
	while fixing:
		fixing = False
		for q in list(range(len(numb))):
			if q + 1 == len(numb):
				continue
			currently = numb[q]
			after = numb[q + 1]
			if currently > after:
				numb[q] = after
				numb[q + 1] = currently
				fixing = True
	return numb


def mergesort(numb):
	if len(numb) > 1:
		print("")
		print(f"Breaking {numb} into two")
		middle = int(len(numb) / 2)
		left = numb[:middle]
		right = numb[middle:]
		print(f"Obtained {left} and {right}")
	else:
		return numb

	left = mergesort(left)
	right = mergesort(right)

	if len(left) == 1:
		pass
	else:
		# use Bubble Sort
		left = bubble_sort(left)

	if len(right) == 1:
		pass
	else:
		# use Bubble Sort
		right = bubble_sort(right)

	print(f"Arranging {left} and {right} together")

	if len(right) == 1 and len(left) == 1:
		if right[0] < left[0]:
			result = right + left
		else:
			result = left + right
	else:
		result = []
		left_start = left.pop(0)
		right_start = right.pop(0)
		yes = True
		while yes:
			if left_start < right_start:
				result.append(left_start)
				if len(left) == 0:
					result.append(right_start)
					for r in right:
						result.append(r)
					right = []
					yes = False
				else:
					left_start = left.pop(0)
			else:
				result.append(right_start)
				if len(right) == 0:
					result.append(left_start)
					for l in left:
						result.append(l)
					left = []
					yes = False
				else:
					right_start = right.pop(0)
	print(f"Resulted in {result}")
	print("")
	return result


print(mergesort(numbers))
