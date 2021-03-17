# numbers = [1, 2, 3, 4, 5]

# for number in numbers:
#     print(number*3)


# total = 0

# for number in numbers:
#     total += number

# print(total)

chickens = [
  {"name": "Margaret", "age": 2, "eggs": 0},
  {"name": "Hetty", "age": 1, "eggs": 2},
  {"name": "Henrietta", "age": 3, "eggs": 1},
  {"name": "Audrey", "age": 2, "eggs": 0},
  {"name": "Mabel", "age": 5, "eggs": 1},
]

for chicken in chickens:
    print(f"{chicken['name']} is {chicken['age']} and has {chicken['eggs']} eggs")

total_eggs = 0

for chicken in chickens:
    total_eggs += int(chicken['eggs'])
    chicken['eggs'] = 0

print(f'The total number of eggs is {total_eggs}')
print(chickens)
