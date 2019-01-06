##############################################################################
# The program do not nothing special, only shows oop
##############################################################################

class Employee:
    pass

emp1 = Employee()
emp2 = Employee()

emp1.first_name = "John"
emp1.surname = "Green"

emp2.first_name = "George"
emp2.surname = "Black"


def full_name(instance):
    print(instance.first_name, instance.surname)

full_name(emp1)
full_name(emp2)
