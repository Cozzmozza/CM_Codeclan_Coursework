fruits = ['apple', 'banana', 'grape', 'orange']

# print(fruits[0])
# print(fruits[-1])

fruits[1] = 'mango'
# print(fruits)

# my_list = [], this is the general syntax
# my_list = list() also works, but not as common with other languages

num_items = len(fruits) 
# The number of items in the fruits. The length
print(num_items)

fruits.append('pear')
print(fruits)

fruits.pop()
print(fruits)

nested_list = [1, 2, 3, [4, 5, 10]]
print(nested_list)