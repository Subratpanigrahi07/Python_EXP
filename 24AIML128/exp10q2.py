# write a program to crerate four base ckasses having individual method addion(),multiplcaion (),divisiom(), respectivly.
#  create a derived class for all above (multiple inheritance ) having member data = data 1,data2,create an object and then perform operation 
# on the data and  data1 and data2.

class Addition:
    def addition(self, a, b):
        return a + b

class Multiplication:
    def multiplication(self, a, b):
        return a * b

class Division:
    def division(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Division by zero not allowed"

class Subtraction:
    def subtraction(self, a, b):
        return a - b

class Calculator(Addition, Multiplication, Division, Subtraction):
    def __init__(self, data1, data2):
        self.data1 = data1
        self.data2 = data2

    def perform_operations(self):
        print(f"Addition: {self.addition(self.data1, self.data2)}")
        print(f"Subtraction: {self.subtraction(self.data1, self.data2)}")
        print(f"Multiplication: {self.multiplication(self.data1, self.data2)}")
        print(f"Division: {self.division(self.data1, self.data2)}")

data1 = float(input("Enter first number (data1): "))
data2 = float(input("Enter second number (data2): "))
 
calc = Calculator(data1, data2)
calc.perform_operations()