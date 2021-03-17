# In the file, create a simple Python guessing game using:
# User Input
# If-Else statement
# Submit the homework form

# WHAT I WANT:
# Something that takes a users input, and compares it to a target value
# If the value matches, it returns a string saying it's correct
# If wrong, it returns a string saying incorrect
# Start by setting the input as a variable with a set value
# Then create a function that takes an input?

target = 5

print('Guess a number between 0 and 10?')

def guessing_game(val):
    if target == val:
        print('You guessed the right number!')
    else:
        print('Wrong, guess again')

# Couldn't figure out how to call this function with an argument in the terminal. 
# Could call it doing 'python3 precourse_recap.py/guessing_game() or .guessing_game()
# But any argument in the brackets gave an error 'unknown file attribute'
# Or when doing the above without an argument, it then opened 'function>' directory
# Putting in an argument here e.g. 3, would then bind it to the 

guessing_game(5)


