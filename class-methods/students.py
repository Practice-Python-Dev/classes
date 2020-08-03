#------------------------------
# A FUNCTION WITHIN A CLASS
#------------------------------

# Essentially a function we can use inside a class
    # Can modify the objects inside the class
    # Can give us information info about those object

# Create a 'Student' object
class Student:
    def __init__(self, name, major, gpa):
         self.name = name
         self.major = major
         self.gpa = gpa

# Define a function within the 'Student' class, Then all the objects can access it
    # Pass in self parameter (to refer to each students information)
    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False

