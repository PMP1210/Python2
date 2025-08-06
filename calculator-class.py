class calculator:
    def __init__(self , a , b , symbol):
        self.a=a
        self.b=b
        self.symbol=symbol

        if symbol=='+':
            self.result=self.a+self.b
        elif symbol=='-':
            self.result=self.a-self.b
        elif symbol=='*':
            self.result=self.a*self.b   
        elif symbol=='/':
            if self.b==0:
                self.result="Error: Division by zero"
            else:
                self.result=self.a/self.b
        else:
            self.result="Error: Invalid operator"

    @staticmethod
    def welcome():
        print("Welcome to the Calculator Program!")

calculator.welcome()
symbol=input("Enter the operator (+, -, *, /): ")
a=float(input("Enter the first number: "))  
b=float(input("Enter the second number: "))
calc=calculator(a , b , symbol)
print("Result: ", calc.result)