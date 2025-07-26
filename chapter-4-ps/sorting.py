marks=[]

for i in range(1,7):
    mark=int(input("Enter {} student marks:".format(i)))
    marks.append(mark)

print("Marks of students:", marks)
print("Sorted marks in disending order:",sorted(marks,reverse=True))