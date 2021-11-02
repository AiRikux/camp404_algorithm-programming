# libraries
import random

# functions
# create a list of random integer


def make_numbers(no=10):
	numb = []
	for _ in list(range(1, no)):
		numb.append(random.randint(1, no))
	return numb


# Bubble Sort
print("")
print("BUBBLE SORT ########################################")
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
print("")
print("SELECTIVE SORT ########################################")
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
print("")
print("INSERTION SORT ########################################")
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
print("")
print("MERGE SORT ########################################")

numbers = make_numbers()
print(numbers)


def bubble_sort(numb):
	fixing2 = True
	while fixing2:
		fixing2 = False
		for q in list(range(len(numb))):
			if q + 1 == len(numb):
				continue
			currently = numb[q]
			after2 = numb[q + 1]
			if currently > after2:
				numb[q] = after2
				numb[q + 1] = currently
				fixing2 = True
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
		yes2 = True
		while yes2:
			if left_start < right_start:
				result.append(left_start)
				if len(left) == 0:
					result.append(right_start)
					for r in right:
						result.append(r)
					right = []
					yes2 = False
				else:
					left_start = left.pop(0)
			else:
				result.append(right_start)
				if len(right) == 0:
					result.append(left_start)
					for l in left:
						result.append(l)
					left = []
					yes2 = False
				else:
					right_start = right.pop(0)
	print(f"Resulted in {result}")
	print("")
	return result


print(mergesort(numbers))
