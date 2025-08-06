class Programmer:
  company="Microsoft"
  def __init__(self , name , age , salary):
    self.name=name
    self.age=age
    self.salary=salary

p=Programmer("Harsh" , 20 , 10000)
print(p.company , p.name , p.age , p.salary)
j=Programmer("Akash" , 32 , 56000)
print(j.company , j.name , j.age , j.salary)