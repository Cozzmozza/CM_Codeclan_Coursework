counter = 0
my_number = 5

# while(counter < my_number):
#     print(f'Counter is {counter}')
#     # This is a formatted string
#     counter += 1
#     # This is the shorthand equivalent of, counter = counter + 1


# Guessing Game

# user_input = int(input('Guess a number between 1 and 10? '))

# while (user_input != my_number):
#     user_input = int(input('WRONG. Guess again pls: '))

# print("Nailed it!")


while(True):
    line = input('Type something, or type q to quit ')
    if (line.lower() == 'q'):
        break
# This will break/quit the loop
    print(f'You typed {line}')

print('Bye felicia')