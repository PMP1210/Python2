skill={}

for i in range(1 , 6):
    key=input("Enter name :")
    value=input("Enter skill:")
    skill.update({key : value})

print(skill)