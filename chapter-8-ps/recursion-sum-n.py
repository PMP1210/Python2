n=int(input("Enter a number: "))
sum=0
def sum_n(n):
    if n>0:
        return n+sum_n(n-1)
    else:
        return 0

print(f"The sum of first {n} natural numbers is: {sum_n(n)}")

