s=set ()

for i in range(1, 6):
    value=int(input("Enter value {}: ".format(i)))
    s.add(value)

print("Set of values:", s)
print(type(s))
print("Length : ",len(s))