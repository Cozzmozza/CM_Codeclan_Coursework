# BEFORE IMPORTING:
# We need to create a file called <__init__.py> to allow imports
# This may? Not be required anymore

# Import the calculator.py file
# If in the same folder, import calculator is enough
# As it's a different folder, we need import package.module
import modules.calculator
print(modules.calculator.add(10,20))

# OR, import all you need at the start
from modules.calculator import add

# Should really just choose one instead of mixing the two, better for DRY code
from modules.calculator import add, subtract, multiply, divide
# Only import what you need though

# If you want to import everything, use asterisk
from modules.calculator import *

# Another tip is to locally name the file you have imported, as an alias
import modules.calculator as calc
# More useful for e.g. calculator_main_project_1_version_12 as calc
# If this is done in the first header at the top, it's then EASY to change file

