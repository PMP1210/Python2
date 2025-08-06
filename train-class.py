from random import randint

class train:
    def __init__(self , trainno):
        self.trainno=trainno

    def book(self , date , frome , to):
        self.date=date
        self.frome=frome    
        self.to=to
        print(f"Train {self.trainno} bookded succesfully from {self.frome} to {self.to} on date '''{self.date}'''")

    def status(self):
        print(f"Train {self.trainno} is running on time .")

    def price(self):
        print(f"Train {self.trainno} fare from {self.frome} to {self.to} is {randint(100,1000)}")

t=train(input("Enter train number: "))
# t.trainno(input("Enter train number: "))
# print("Enter train number:".t.trainno)
t.book(input("Enter date: "), input("Enter from: "), input("Enter to: "))
t.status()
t.price()
print("Thank you for using our service!")