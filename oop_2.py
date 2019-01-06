##############################################################################
# The program do not nothing special, only shows oop
##############################################################################
import datetime

class Employee:
    def __init__(self,first_name,surname,birthday):
        self.first_name = first_name
        self.surname = surname
        self.full_name = first_name + " " + surname
        self.birthday = birthday #yyyymmdd

    def age(self):
        year = int(self.birthday[0:4])
        month = int(self.birthday[4:6])
        day = int(self.birthday[6:8])
        birth = datetime.date(year, month, day)
        today = datetime.date.today()
        days = (today - birth).days
        age = days // 365
        return age

    def card(self):
        age = str(self.age())
        card = "===========================\n"
        card += "{}: {} age\n".format(self.full_name,age)
        card += "===========================\n"
        return card

porter = Employee("John", "brown","19910115")

print("Surname: {}" .format(porter.surname))
print("Full name: {}".format(porter.full_name))
print("Birthday: {} ; Age: {}".format(porter.birthday, porter.age()))
print(porter.card())
