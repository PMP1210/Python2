# from datetime import date
# name=input("Enter name :")
# divas=str(date.today())
# message="Dear <str> You are selected! on <date>"

# print(message, message.replace("<str>",name), message.replace("<date>",divas))
# from datetime import date
from datetime import date
name = input("Enter name: ")
divas = str(date.today())
letter = "Dear <str> You are selected! on <date>"

letter = letter.replace("<str>", name)
letter = letter.replace("<date>", divas)
print(letter)