# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:
even_integers = []
for number in numbers:
  if number % 2 == 0:
    even_integers.append(number)
print(even_integers)

# 2. Print the difference between the largest and smallest value:
mini = min(numbers)
maxi = max(numbers)
print(maxi - mini)

# 3. Print True if the list contains a 2 next to a 2 somewhere.
# Go through each one, if value = 2, and value of number at index+1 = 2, print true
# index = index + 1, then print true
for num in numbers:
    if num == 2:
        index_1 = numbers.index(num)
        index_2 = index_1 + 1
        num_2 = numbers[index_2]
        if num_2 == 2:
            print('True')
        break

# 3. Solution:
result = False
index = 0
for number in numbers:
    if (number == 2 and numbers[index-1] ==2):
        result = True
    index +=1
print(result)

# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22

total = 0
found_6 = False
for number in numbers:
    if number == 6:
        found_6 = True 
    elif found_6:
        if number ==7:
            found_6 = False
    else:
        total += number

print(total)


# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 







