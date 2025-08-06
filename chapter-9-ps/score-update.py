with open("d:\python\Python2\chapter-9-ps\score.txt","w") as f:
    content=f.read().lower()

score=int(input("Enter score :"))

if score in content:
    content=content.replace("highest score is {}".format(score))
    print("Score updated successfully.")
else:
    print("Can't able to update.")