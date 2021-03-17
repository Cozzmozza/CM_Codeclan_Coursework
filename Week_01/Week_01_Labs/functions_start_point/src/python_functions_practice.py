
def return_10():
    return 10

def add(val1, val2):
    return (val1 + val2)

def subtract(val_1, val_2):
    return (val_1 - val_2)

def multiply(val_1, val_2):
    return (val_1 * val_2 )

def divide(val_1, val_2):
    return (val_1 / val_2)

def length_of_string(string):
    return len(string)
    
def join_string(string_1, string_2):
    return (string_1 + string_2)
   
def add_string_as_number(string_1, string_2):
    return (int(string_1) + int(string_2))
      
months = {  1 : 'January', 
            2 : 'February', 
            3 : 'March', 
            4 : 'April',    
            5 : 'May', 
            6 : 'June', 
            7 : 'July', 
            8 : 'August', 
            9 : 'September', 
            10 : 'October' , 
            11 : 'November', 
            12 : 'December'
            }

def number_to_full_month_name(month):
    return months[month]

def number_to_short_month_name(month):
    return months[month][0:3]

def volume_of_cube(val):
    return val**3
    # To the power of 3

def reverse_string(string):
    string_reversed = ''
    index = len(string)
    while index > 0:
        string_reversed += string[index-1]
        index = index -1
    return string_reversed

def convert_temp(value):
    result = (value - 32)*(5/9)
    return round(result, 2)