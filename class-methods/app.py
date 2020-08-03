#------------------------------
# IMPORT STUDENT CLASS
#------------------------------

# From the 'students' module import the 'Student' class
from students import Student

#------------------------------
# CREATE STUDENT OBJECTS
#------------------------------

# Note the syntax:
    # variable = class(parameter, parameter, parameter)
student1 = Student("James", "Economics", 3.7)
student2 = Student("John", "Psychology", 3.4)
student3 = Student("Brendan", "General Studies", 2.7)
student4 = Student("Jamie", "Law", 4.0)

# print (variable.class-function())
print(student1.on_honor_roll())
