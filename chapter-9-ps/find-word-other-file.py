with open("d:\python\Python2\chapter-9-ps\poem.txt","r") as f:
    content=f.read().lower()

word=input("Search word : ")

if word in content:
    print("word found")
else:
    print("word not found!!")