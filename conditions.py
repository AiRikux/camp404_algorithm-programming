# condition
print("IF ELSE")
a_key = input("Password: ")
if a_key == "test123":
	print("You have successfully logged in")
else:
	print("Please try again")

# elif condition
print("")
print("IF ELIF ELSE")
temperature = int(input("Temperature: "))
if temperature <= 26:
	print("Its cloudy")
elif temperature > 26:
	print("Its sunny")
else:
	print("Weather unknown")

# match case
print("")
print("MATCH CASE")
score = int(input("Your score: "))
match score:
	case 1000:
		print("Awesome")
	case 500:
		print("Great")
	case _:
		print("What?")

# for loop
print("")
print("FOR LOOP")
low = int(input("low number: "))
high = int(input("high number: "))
for item in range(low, high + 1):
	if item % 2 != 0:
		print(item, " ")

# while loop
print("")
print("WHILE LOOP")
x = 20
while x > 0:
	if x % 3 == 0:
		print(x, " ")
	x = x - 1


# simple function
print("")
print("SIMPLE FUNCTION")


def hello():
	print("Hello!")


hello()

# function with input
print("")
print("FUNCTION WITH INPUT")


# print text n times
def hello2(text, no):
	for no in range(no):
		print(text)


hello2("hello", 2)

# function with result
print("")
print("FUNCTION WITH RESULT")


def area(a, b):
	result = a * b
	return result


print(area(1, 2))
