def remove(l,item):
    if item in l:
        l.remove(item)
        return l
    else:
        print("Item not found in the list.")

l1=["harry","potter","harsh","manish"]

item=input("Enter the item to remove: ")
remove(l1, item)
print("Updated list:", l1)
