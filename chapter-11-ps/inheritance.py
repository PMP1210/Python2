class name:
    def __init__(self, firstname, lastname, middlename):
        self.firstname = firstname
        self.lastname = lastname
        self.middlename = middlename

    def surname(self):
        print(f"Full name: {self.firstname} {self.middlename} {self.lastname}")

class age(name):
    def __init__(self, firstname, lastname, middlename, number):
        super().__init__(firstname, lastname, middlename)
        self.number = number

    def ummer(self):
        print(f"Age: {self.number}")

class std(age):
    def __init__(self, firstname, lastname, middlename, number, standard):
        super().__init__(firstname, lastname, middlename, number)
        self.standard = standard

    def strudent(self):
        print(f"Standard: {self.standard}")

# Get input
firstname = input("Enter first name: ")
lastname = input("Enter last name: ")
middlename = input("Enter middle name: ")
number = input("Enter age: ")
standard = input("Enter standard: ")

# Create object and call methods
student = std(firstname, lastname, middlename, number, standard)
student.surname()
student.ummer()
student.strudent()