p1="Make a lot of money"
p2="buy now"
p3="subscribe now"
p4="click this"

comm=input("Enter the comment:")

if((p1 in comm) or (p2 in comm) or (p3 in comm) or (p4 in comm)):
    print("This is a spam comment")
else:
    print("This is not a spam comment")