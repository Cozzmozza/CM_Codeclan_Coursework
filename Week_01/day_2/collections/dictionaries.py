# my_first_dictionary = {}
# my_second_ditionary = dict()

# meals = {'breakfast' : 'cereal', 'lunch' : 'pita'}

# print(meals)

# Finds the matched key to the value breakfast
# print(meals['breakfast'])

# Checks if there is an entry for 'breakfast' in the dictionary
# print('breakfast' in meals)

# # Add a new item
# meals['supper'] = 'pancakes' 

# print(meals)

# # Prints a list of the values in the dictionary
# print(list(meals))

# # Prints a view object of the kets in the dictionary
# print(meals.keys())


# countries = {
#     'UK' : 'London',
#     'Germany' : 'Berlin'
# }

# print(countries)


countries = {
    'UK' : {
        'Capital' : 'London',
        'Population' : 1000
    },
    'Germany' : {
        'Capital' : 'Berlin',
        'Population' : 1500,
        'Languages' : ['German', 'English']
    }
}

# print(countries)

# To just access the Germany one:
# print(countries['Germany'])

# # To access Population, in germany:
# print(countries['Germany']['Population'])

# To print the 'English' language for germany, we need to access:
# 1) The Countries dictionary
# 2) The German dictionary
# 3) The Languages key pair, which has a List
# 4) Then accessing the index for English
print(countries['Germany']['Languages'][1])
