# imports debugger
import pdb
# 

cakes = [
    {
      "name": "Brownie",
      "ingredients":[ "chocolate", "cocoa powder", "flour", "eggs", "sugar", "butter" ],
      "rating": 5
    },
    {
      "name": "Carrot Cake",
      "ingredients":[ "carrots", "raisins", "cinnamon", "flour", "eggs", "sugar", "butter" ],
      "rating": 2.5
    },
    {
      "name": "Lemon Drizzle",
      "ingredients":[ "lemon juice", "flour", "eggs", "sugar", "butter" ],
      "rating": 1.5
    }
]

def get_average_rating(cakes):
  # We will add a break point here, as this is where we think the bug starts
    pdb.set_trace()
    # Could also do these on the same line, i.e. import pdb; pdf.set_trace(), personal preference
    ratings = []

    for cake in cakes:
        ratings.append(cake["rating"])

    ratings_total = sum(ratings)
    number_of_cakes = len(cakes)
    average = ratings_total / number_of_cakes
    # Originally this was the final result, i.e. 5 / 3 = 1.67
    # Correct answer should be 9 / 3 = 3

    return average

print(get_average_rating(cakes))



# ------------------------------------------------------------------------
# To debug, run the code with the pdb.set_trace() where we want it
# It'll then run in the terminal and stop at the first line it sees
# type l to see wider context of the program
# type n for next line
# And so on till we see something that isnt right
# Press c to finish the debugging in the current state
# Restart

# *** Type j <number> to go to a specific line e.g. j 29 will go to line 29 immediately 
# *** Type a and it will show a list of all the arguments, also useful to see if they are the problem
# *** Type h for help
# ------------------------------------------------------------------------

# We can see that it just goes through the loop once, and returns the average. This is not what we wanted
# We then changed our indents as they were incorrect
# Run the file again with the debugger active
# See that it now loops through 3 times, before then moving onto calculating the average
