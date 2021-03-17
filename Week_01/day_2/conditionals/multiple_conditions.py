# Logical Operators
# These are used if we want to check for multiple conditions

cozza_hungry = True
cozza_tired = True

if cozza_hungry and cozza_tired:
    print('Cozza is HANGRY')

# Likewise we can do OR. As long as one of them is true, we are good
# IMPORTANT - It'll execute the action as soon as one condition read is true
# Say we had 10 variables, it'll run through till the first one is true, then stop, and execute the print

cozza_tired = False

if cozza_hungry or cozza_tired:
    print('Cozza is one of them')