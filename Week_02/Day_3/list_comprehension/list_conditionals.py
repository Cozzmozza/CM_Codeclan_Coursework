numbers = range(1, 11)
# Shortcut on making a list, same as doing [1, 2, 3, 4,... upto 10]

evens_squared = []

for number in numbers:
    if number % 2 == 0:
        evens_squared.append(number * number)
        # If the number modulus divided by 2 is 0 (remainder), i.e. if it's even
        # add it to our evens_squared list, and square it

print(evens_squared)


# List comprehension is:
# evens_squared = [expression for item in list if condition]
# This does the same thing, in one line
evens_squared_lc = [number * number for number in numbers if number %2 == 0]

print(evens_squared_lc)
