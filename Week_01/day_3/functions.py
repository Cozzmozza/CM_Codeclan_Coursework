def greet(name, time):
    return f'Good {time}, {name}'

print(greet('Colin', 'day'))
print(greet('Enzo','evening'))
# This is passing by reference

# We can also pass by variable
name_1 = 'Colin'
time_1 = 'day'
name_2 = 'Enzo'
time_2 = 'evening'

print(greet(name_1, time_1))
print(greet(name_2, time_2))