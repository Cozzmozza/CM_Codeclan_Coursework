

print('Turn the computer on')

boot = input('Did it boot up? ')

if boot == 'yes':
    print('Login with password')
elif boot == 'no':
    plugged_in = input('Is it plugged in? ')
    if plugged_in == 'yes':
            print('Computer is broken')
    elif plugged_in == 'no':
            print('Plug it in')
            fix = input('Did this fix the problem? ')
            if fix == 'no':
                    print('Computer is broken')
            elif fix == 'yes':
                    print('Login with password')
