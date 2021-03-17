# Part 1
# Using single list comprehension, and the following list:
ages = [5, 15, 64, 27, 84, 26]
# Return a list of only the odd ages.
odd_ages = [age for age in ages if age %2 == 1]
print(odd_ages)


# Part 2
# Using single list comprehension, and the following list:
chicken_names = ["Hen Solo", "Cluck Norris", "Hennifer Lopez", "ChewPekka", "Feather Locklear"]
# Return a list with chickens whose name is more than 10 characters
# Return a list of chickens whose name starts with the letter H
chicken_length_10 = [chicken for chicken in chicken_names if len(chicken) > 10]
print(chicken_length_10)

chicken_first_h = [chicken for chicken in chicken_names if chicken[0] == 'H']
print(chicken_first_h)


# Part 3
# Using single list comprehension, and the following list:
words = ["The", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]
# Build a new list, with the first letter from each word
# Convert each letter to lower case
# Expected output: ["t", "q", "b", "f", "j", "o", "t", "l", "d"]

words_first_letter = [word[0].lower() for word in words]
print(words_first_letter)